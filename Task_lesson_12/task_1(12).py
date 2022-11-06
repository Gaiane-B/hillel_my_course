# Program "City"
import random
from random import randint


class Street:
    def __init__(self, number_of_houses: int, number_street: int):
        self.houses = []
        self.number_of_houses = number_of_houses
        self.number_street = number_street
        for house in range(self.number_of_houses):
            self.houses.append(House(len(self.houses) + 1))


class House:
    def __init__(self, number_of_house: int):
        self.population = randint(1, 100)
        self.number_of_house = number_of_house


class City:
    def __init__(self, name_of_city: str = 'Kyiv', minimum_house_par=5, maximum_house_par=20, minimum_street_par=1,
                 maximum_street_par=12):
        self.name_of_city = name_of_city
        self.streets = []
        self.number_of_streets = randint(minimum_street_par, maximum_street_par)
        self.count_all_houses = randint(minimum_house_par, maximum_house_par)

    @property
    def population(self):
        population = 0
        for street in self.streets:
            for house in street.houses:
                population += house.population
        return population

    def fill_my_city(self):
        for street in range(self.number_of_streets):
            self.streets.append(Street(len(self.streets) + 1, random.randint(5, 20)))

    def add_street(self):
        self.streets.append(Street(len(self.streets) + 1, self.count_all_houses))

    def delete_street(self, street_num: int):
        self.streets.pop(street_num - 1)

    def print_table_city(self):
        print('Street', 'House', 'Population')
        for street in self.streets:
            for house in street.houses:
                print(street.number_street, house.number_of_house, house.population, sep='  ')


if __name__ == '__main__':
    city = City()
    city.fill_my_city()
    city.print_table_city()
    print(f'Total population in {city.name_of_city} is {city.population} people')
