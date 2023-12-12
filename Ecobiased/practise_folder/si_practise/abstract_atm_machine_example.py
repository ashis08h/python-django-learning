from abc import ABC, abstractmethod


class AtmMachine(ABC):

    def withdraw(self, given_money):
        pass


class SimpleAtmMachine(AtmMachine):

    def withdraw(self, given_money):
        notes = {500: 0, 200: 0, 100: 0}
        if (given_money % 100) != 0:
            print("The amount should be multiple of 100.")
        else:
            print("test1")
            while given_money > 0:
                if given_money >= 500:
                    print("test1")
                    notes[500] += 1
                    given_money -= 500
                elif given_money >= 200:
                    print("test2")
                    notes[200] += 1
                    given_money -= 200
                else:
                    print("test3")
                    notes[100] += 1
                    given_money -= 100
            return notes


si = SimpleAtmMachine()
print(si.withdraw(1900))
print(si.withdraw(1950))
