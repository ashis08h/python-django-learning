from abc import ABC, abstractmethod


class AtmMachine(ABC):

    @abstractmethod
    def withdraw(self, given_amount):
        pass


class SimpleAtmMachine(AtmMachine):

    def withdraw(self, given_amount):
        if given_amount % 100 != 0:
            return "Please enter amount multiple of 100"
        else:
            notes = {500:0, 200:0, 100:0}
            while given_amount > 0:
                if given_amount >= 500:
                    given_amount -= 500
                    notes[500] += 1
                elif given_amount >= 200:
                    given_amount -= 200
                    notes[200] += 1
                else:
                    given_amount -= 100
                    notes[100] += 1
            return notes


sam = SimpleAtmMachine()
print(sam.withdraw(2300))
