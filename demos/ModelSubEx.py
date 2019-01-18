from fc_model import FCModel


class ModelSubEx(FCModel):

    name = None

    def fc_property_mapper(self):
        return {
            'name': 'name',
        }
