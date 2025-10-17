from abc import ABC, abstractmethod


# Example 1
# violates isp
class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class HumanInterface(WorkInterface):

    def work(self):
        print("working")

    def eat(self):
        print("eating")


class RobotInterface(WorkInterface):

    def work(self):
        print("Robot can work")

    def eat(self):
        raise NotImplementedError("Robot can not work")


# follow isp


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable, Eatable):

    def work(self):
        print("working")

    def eat(self):
        print("eating")


class RobotWorker(Workable):

    def work(self):
        print("working")


# Example 2
# violates ISP


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
        print("scanning")


class SimplePrinter(PrintScan):

    def print(self):
        print("Printing")

    def scan(self):
        raise NotImplementedError("Can not scan")



# follow isp


class Printable(ABC):

    @abstractmethod
    def print(self):
        pass


class Scannable(ABC):

    @abstractmethod
    def scan(self):
        pass


class MultiPrint(Printable, Scannable):

    def print(self):
        print("printing")

    def scan(self):
        print("scanning")


class SimplePrint(Printable):

        def print(self):
            print("printing")