from abc import ABC, abstractmethod


class AtmMachine(ABC):

    def withdraw(self, given_money):
        pass


class SimpleAtmMachine(AtmMachine):

    def withdraw(self, given_money):
        notes = {500: 0, 200: 0, 100: 0}
        if (given_money % 100) != 0:
            print("Amount should be multiple of 100.")
        else:
            while given_money > 0:
                if given_money >= 500:
                    notes[500] += 1
                    given_money -= 500
                elif given_money >= 200:
                    notes[200] += 1
                    given_money -= 200
                else:
                    notes[100] += 1
                    given_money -= 100
        return notes


simple_atm = SimpleAtmMachine()
print(simple_atm.withdraw(700))
