import abc
import json
from abc import ABCMeta


class FCModel(metaclass=ABCMeta):

    def __init__(self):
        self.fc_default_init()

    @abc.abstractmethod
    def fc_property_mapper(self):
        pass

    def fc_default_init(self):
        pass

    def fc_after_generate(self, data):
        pass

    def fc_generate(self, data):

        property_map = self.fc_property_mapper()
        property_class_map = self.fc_property_class_mapper()
        item_class_map = self.fc_array_item_class_mapper()

        for prop, json_key in property_map.items():
            if json_key in data and hasattr(self, prop):
                if prop in property_class_map and isinstance(data[json_key], list):
                    clazz = property_class_map[prop]
                    obj = clazz()
                    obj.fc_generate(data[json_key])
                    setattr(self, prop, obj)
                elif prop in item_class_map and isinstance(data[json_key], list):
                    arr = []
                    clazz = item_class_map[prop]
                    for dic in data[json_key]:
                        obj = clazz()
                        if isinstance(obj, FCModel):
                            obj.fc_generate(dic)
                            arr.append(obj)
                        else:
                            arr.append(None)
                    setattr(self, prop, arr)
                else:
                    setattr(self, prop, data[json_key])

        self.fc_after_generate(data)
        return self

    def fc_encode(self):
        property_map = self.fc_property_mapper()
        property_class_map = self.fc_property_class_mapper()
        item_class_map = self.fc_array_item_class_mapper()

        data = {}

        for prop, json_key in property_map.items():
            if hasattr(self, prop):
                entity = getattr(self, prop)
                if prop in property_class_map and isinstance(entity, FCModel):
                    data[json_key] = entity.fc_ret_map()
                elif prop in item_class_map and isinstance(entity, list):
                    data[json_key] = [item.fc_ret_map() for item in entity]
                else:
                    data[json_key] = entity
        return data

    def fc_ret_map(self):
        return self.fc_encode()

    def fc_property_class_mapper(self):
        return {}

    def fc_array_item_class_mapper(self):
        return {}

    def __repr__(self):
        description = json.dumps(self.fc_encode(), ensure_ascii=False, default=str)
        return "<%s instance at %s>: %s" % (self.__class__.__name__, id(self), description)


