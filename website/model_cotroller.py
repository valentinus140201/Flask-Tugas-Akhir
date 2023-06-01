class ModelController(object):
    element = []

    @staticmethod
    def add_element(x):
        ModelController.element.append(x)

    @staticmethod
    def get_element():
        return ModelController.element