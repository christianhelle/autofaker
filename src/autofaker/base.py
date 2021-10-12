from abc import abstractmethod


class TypeDataGeneratorBase:
    @abstractmethod
    def generate(self):
        pass
