####
##
#
#


__version__ = "0.1.16-alpha1"

import re

import more_itertools as mit
from deta import Base as DetaBase
from deta import Deta
from hashlib import sha256

# class KVModel(dict, BaseModel):
class KVModel(dict):
    class Config:  # (BaseModel.Config):
        deta_key: str = DETA_BASE_KEY if "DETA_BASE_KEY" in globals() else None
        deta = (
            Deta(DETA_BASE_KEY)
            if "Deta" in globals() and "DETA_BASE_KEY" in globals()
            else None
        )
        table_name: str = None
        hash = lambda x: sha256(bytes(x, 'utf8')).hexdigest()

        # def __init__(self, *args, **kwargs):
        #    super(__class__, BaseModel).__init__(*args, **kwargs)
        #    self._set_table_name()
        #    self._set_db()

        # for name, field in cls.__fields__.items():
        #    setattr(cls, name, DetaField(field=field))

        pass

    @property
    def _db(cls):
        return getattr(cls.Config, "deta", cls._set_db())

    @classmethod
    def _set_db(cls, dbname: DetaBase = None):
        cls.Config.deta = (Deta(cls.Config.deta_key)).Base(
            getattr(cls.Config, "table_Name", cls._set_table_name())
        )
        return cls.Config.deta

    @classmethod
    def _set_table_name(cls, table_name: str = None) -> str:
        if table_name:
            setattr(cls.Config, "table_Name", table_name)
        if getattr(cls.Config, "table_name", None) is None:
            setattr(
                cls.Config,
                "table_name",
                re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower(),
            )
        return cls.Config.table_name

    def _put_many(self, kv_list):
        [  # instead map()
            self._db.put_many(chunk)
            for chunk in mit.chunked(
                [
                    {"key": self.Config.hash(key), "value": val, "path": key}
                    for key, val in kv_list.items()
                ],
                25,
            )
        ]
        return

    def _put(self, param, value=None):
        if value is None and isinstance(param, list):
            item = self._put_many(param)
        if value is None and isinstance(param, dict):
            item = self._db.put(
                {
                    "key": self.Config.hash(param["key"]),
                    "value": param["value"],
                    "path": param["key"],
                }
            )
        if isinstance(param, str):
            item = self._db.put(
                {"key": self.Config.hash(param), "value": value, "path": param}
            )
        return item

    def _update(self, updates: dict, key: str):
        self._db.update({"path": key}.update(updates), key=self.Config.hash(key))
        return self

    def __read__(self):
        pass

    # __getitem__ __setitem__
    # def __delitem__(self, name: str):
    #    print("__del__item__", name)
    #    pass

    def get(self, key: str, default=None):
        key = str(key)
        item = self._db.get(self.Config.hash(key))
        self.setdefault(key, default if item is None else item["value"])

        # return self[key]
        return super().get(key)

    def incr(self, key: str, quantity=1):
        key = str(key)
        hkey = self.Config.hash(key)
        try:
            self._db.update({"value": self._db.util.increment(quantity)}, hkey)
            item = self._db.get(hkey)
        except Exception as e:  # "Key '{}' not found".format(key)
            # print("Exception", str(e))
            if f"Key '{hkey}' not found" == str(e):
                item = self._put(key, quantity)
                pass
            else:
                raise Exception("Unhandled Exception: " + str(e))
                return
        self[key] = item["value"]
        return self[key]

    def incr2(self, key: str, quantity=1):
        key = str(key)
        hkey = self.Config.hash(key)
        try:
            item = self._put(key, value=self._db.get(hkey)["value"] + quantity)

        except TypeError as e:
            emessage = str(e)

            if emessage.find("subscriptable") > -1:
                # TypeError: 'NoneType' object is not subscriptable
                item = self._put(key, value=quantity)
            if (
                emessage.find("concatenate") > -1
                # TypeError: can only concatenate str (not "NoneType") to str
                or emessage.find("unsupported operand") > -1
                # TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
                # or 1
                # smthng else
            ):
                raise ValueError()
                return
            # print(e)
            pass
        except Exception as e:  # NoneTyoe
            print("Unknown Exception", str(e))
            return

        self[key] = item["value"]
        return self[key]

    def decr(self, key: str, quantity=1):
        return self.incr(key, -quantity)

    def rename(key: str, new_key: str):
        self._update({"key": self.Config.hash(new_key), "path": new_key}, key)
        return self

    def save(self):
        self._put_many(self)

        return self

    def query(self, param=None, limit=1000, last=None) -> dict:
        items = {}
        res = self._db.fetch(query=param, limit=limit, last=last)
        while True:
            # print(res.count, res.last)
            items.update(
                tuple(map(lambda item: (item["path"], item["value"]), res.items))
            )

            # for item in res.items:
            #    yield {item["path"]: item["value"]}

            if res.last is None:
                break

            res = self._db.fetch(query=param, limit=limit, last=res.last)

        return items

    def keys(self, param=None):
        return list(self.query(param).keys())

    @classmethod
    def put_many(cls, *args, **kwargs) -> None:
        raise Exception(
            (
                f"class {cls.__name__} have not put many data, use method `.save()` instead"
            )
        )
        pass
