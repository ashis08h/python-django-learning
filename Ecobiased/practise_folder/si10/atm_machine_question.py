from abc import ABC, abstractmethod


class AtmMachine(ABC):

    @abstractmethod
    def withdraw(self):
        pass


class SampleAtmMachine(AtmMachine):

    def withdraw(self, given_amount):
        notes = {100: 0, 200: 0, 500: 0}

        if given_amount % 100 != 0:
            print(f"Please enter amount multiple of 100.")
        else:
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
        print(notes)


sam = SampleAtmMachine()
sam.withdraw(2100)
