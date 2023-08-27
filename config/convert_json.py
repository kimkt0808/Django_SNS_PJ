import json


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return {"__set__": True, "values": tuple(obj)}
        return obj


class JSONDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs.setdefault("object_hook", self._object_hook)
        super().__init__(**kwargs)

    @staticmethod
    def _object_hook(dct):
        if "__set__" in dct:
            return set(dct["values"])
        return dct
