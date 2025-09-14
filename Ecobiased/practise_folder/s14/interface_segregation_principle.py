from abc import ABC, abstractmethod


class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class HumanInterface(WorkInterface):

    def work(self):
        print("Working")

    def eat(self):
        print("Eating")


class RobotInterface(WorkInterface):

    def work(self):
        print("Robot can work")

    def eat(self):
        raise NotImplementedError("Robot can not eat")


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable):

    def work(self):
        print("Working")

    def eat(self):
        print("Eating")


class RobotWorker(Workable):

    def work(self):
        print("Working")


class PrintScan(ABC):

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass


class MultiPrinter(PrintScan):

    def print(self):
        print("Printing")

    def scan(self):
        print("Scanning")


class SimplePrinter(PrintScan):

    def print(self):
        print("printing")

    def scan(self):
        raise NotImplementedError("Simple printer can not scan")


# fix with interface segregation principle.


class Printer(ABC):

    @abstractmethod
    def print(self):
        pass


class Scanner(ABC):

    @abstractmethod
    def scan(self):
        pass


class MultiPrinter1(Printer, Scanner):

    def print(self):
        print("printing")

    def scan(self):
        print("Scanning")


class SimplePrinter1(Printer):

    def print(self):
        print("Printing")