from abc import ABC, abstractmethod


class ATMmachine(ABC):

    def withdraw(self, given_amount):
        pass


class SimpleATMmachine(ATMmachine):

    def withdraw(self, given_amount):
        if given_amount % 100 != 0:
            return "Please enter amount multiple of 100 only."
        else:
            notes = {500: 0, 200: 0, 100: 0}

            while given_amount > 0:
                if given_amount >= 500:
                    notes[500] += 1
                    given_amount -= 500
                elif given_amount >= 200:
                    notes[200] += 1
                    given_amount -= 200
                else:
                    given_amount -= 100
                    notes[100] += 1
            return notes


sam = SimpleATMmachine()
print(sam.withdraw(2800))