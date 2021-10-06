import random
import uuid
from abc import abstractmethod


class Fixture:
    def __init__(self):
        pass

    @staticmethod
    def create(t):
        generator = TypeFactory.create(t)
        return generator.create()


class TypeDataGenerator:
    @abstractmethod
    def create(self):
        pass


class TypeFactory:
    @staticmethod
    def create(t) -> TypeDataGenerator:
        instance = t()
        if instance is 0:
            print('Creating IntegerGenerator')
            return IntegerGenerator()
        elif instance is '':
            print('Creating StringGenerator')
            return StringGenerator()
        else:
            print('Creating ClassGenerator')
            return ClassGenerator(t)


class ClassGenerator(TypeDataGenerator):
    def __init__(self, cls):
        self.instance = cls()

    def create(self):
        members = [
            attr for attr in dir(self.instance)
            if not callable(getattr(self.instance, attr)) and not attr.startswith("__")
        ]
        print(members)
        for member in members:
            t = type(getattr(self.instance, member))
            generator = TypeFactory.create(t)
            value = generator.create()
            setattr(self.instance, member, value)
        return self.instance


class IntegerGenerator(TypeDataGenerator):

    def create(self):
        return random.randint(0, 2147483647)


class StringGenerator(TypeDataGenerator):
    def create(self):
        return str(uuid.uuid4())
