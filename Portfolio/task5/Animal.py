class Animal:
    def __init__(self, name, gen, view, average_life_expectancy, average_height,
                 average_body_weight, habitat, country):
        self._name = name
        self._gen = gen
        self._view = view
        self._average_life_expectancy = average_life_expectancy
        self._average_height = average_height
        self._average_body_weight = average_body_weight
        self._habitat = habitat
        self._country = country

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def gen(self):
        return self._gen

    @gen.setter
    def gen(self, gen):
        self._gen = gen

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, view):
        self._view = view

    @property
    def average_life_expectancy(self):
        return self._average_life_expectancy

    @average_life_expectancy.setter
    def average_life_expectancy(self, average_life_expectancy):
        self._average_life_expectancy = average_life_expectancy

    @property
    def average_height(self):
        return self._average_height

    @average_height.setter
    def average_height(self, average_height):
        self._average_height = average_height

    @property
    def average_body_weight(self):
        return self._average_body_weight

    @average_body_weight.setter
    def average_body_weight(self, average_body_weight):
        self._average_body_weight = average_body_weight

    @property
    def habitat(self):
        return self._habitat

    @habitat.setter
    def habitat(self, habitat):
        self._habitat = habitat

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country
        