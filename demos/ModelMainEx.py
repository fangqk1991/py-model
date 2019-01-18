from demos.ModelSubEx import ModelSubEx
from fc_model import FCModel


class ModelMainEx(FCModel):

    # xxx is not in fc_property_mapper
    xxx = None

    xyy = None
    xxxYYY = None

    subObj = None
    subItems = None

    def fc_property_mapper(self):
        return {
            'xyy': 'xyy',
            'xxxYYY': 'xxx_yyy',
            'subObj': 'sub_obj',
            'subItems': 'sub_items',
        }

    def fc_property_class_mapper(self):
        return {
            'subObj': ModelSubEx,
        }

    def fc_array_item_class_mapper(self):
        return {
            'subItems': ModelSubEx,
        }
