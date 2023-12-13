# TODO Написать 3 класса с документацией и аннотацией типов

from abc import ABC, abstractmethod


class MaterialObject(ABC):
    def __init__(self, material, weight):
        self.material = material
        self.weight = weight

    @abstractmethod
    def describe(self):
        pass

    @abstractmethod
    def move(self, destination):
        pass


class LivingBeing(ABC):
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

    @abstractmethod
    def eat(self, food):
        pass

    @abstractmethod
    def reproduce(self):
        pass


class AbstractConcept(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def define(self):
        pass

    @abstractmethod
    def apply(self, context):
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
