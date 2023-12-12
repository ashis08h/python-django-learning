#from unittest import
import math
from abc import ABC, abstractmethod


def add_num(a, b):
    return a + b


class Vehicle(ABC):

    @abstractmethod
    def can_run(self):
        pass


class Car(Vehicle):

    def can_run(self):
        print("Yes it can run")


c = Car()
c.can_run()


def atm_amount(given_amount):

    number_of_2_hundred_note = 0
    number_of_1_hundred_note = 0
    number_of_5_hundred_note = 0
    if given_amount >= 500:
        number_of_5_hundred_note = math.floor(given_amount / 500)
        given_amount = given_amount - (number_of_5_hundred_note * 500)
    if given_amount >= 200:
        number_of_2_hundred_note = math.floor(given_amount / 200)
        given_amount = given_amount - (number_of_2_hundred_note * 200)
    if given_amount >= 100:
        number_of_1_hundred_note = math.floor(given_amount / 100)
        given_amount = given_amount - (number_of_1_hundred_note * 100)
    domination_dict = {"500": number_of_5_hundred_note, "200": number_of_2_hundred_note, "100": number_of_1_hundred_note}

    return domination_dict

#print(atm_amount(1900))
print(atm_amount(1300))
print(atm_amount(300))
print(atm_amount(700))