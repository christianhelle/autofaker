

class Attributes:
    def __init__(self, instance):
        self.instance = instance

    def get_members(self):
        return [
            attr for attr in dir(self.instance)
            if not callable(getattr(self.instance, attr)) and not attr.startswith("__")
        ]

    def get_attribute(self, member):
        return getattr(self.instance, member)

    def get_typename(self, member):
        return type(self.get_attribute(member)).__name__

    def set_value(self, member, value):
        setattr(self.instance, member, value)
