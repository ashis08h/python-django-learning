from abc import ABC, abstractmethod


class AtmMachine(ABC):

    @abstractmethod
    def withdraw(self):
        pass


class SimpleAtmMachine(AtmMachine):

    def withdraw(self, given_amount):
        notes = {500: 0, 200: 0, 100: 0}
        if given_amount % 100:
            print("Please enter amount multiple of 100.")
        else:
            while given_amount > 0:
                if given_amount >= 500:
                    notes[500] += 1
                    given_amount -= 500
                elif given_amount >= 200:
                    notes[200] += 1
                    given_amount -= 200
                else:
                    notes[100] += 1
                    given_amount -= 100
        return notes


sam = SimpleAtmMachine()
print(sam.withdraw(3300))
