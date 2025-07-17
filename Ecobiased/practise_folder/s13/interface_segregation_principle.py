from abc import ABC, abstractmethod


class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class HumanWorker(WorkerInterface):

    def work(self):
        print("working")

    def eat(self):
        print("eating")


class RobotWorker(WorkerInterface):

    def work(self):
        print("working")

    def eat(self):
        raise NotImplementedError('robots do not eat')


# with ISP


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass


class HumanWorker1(Workable):

    def work(self):
        print("work")

    def eat(self):
        print("eat")


class RobotWorker1(Workable):

    def work(self):
        print("eat")


# Example Two


class PrintScan:

    def printer(self):
        pass

    def scanner(self):
        pass


class MultiPrinter(PrintScan):

    def printer(self):
        print("printing")

    def scanner(self):
        print("scanning")


class SimplePrinter(PrintScan):

    def printer(self):
        print("printing")

    def scanner(self):
        raise NotImplementedError("Simple printer not able to scan")


# fix with ISP


class Printer(ABC):

    @abstractmethod
    def printer(self):
        pass


class Scanner(ABC):

    @abstractmethod
    def scanner(self):
        pass


class MultiPrinter1(Printer, Scanner):

    def printer(self):
        print("Printing")

    def scanner(self):
        print("Scanning")


class SimplePrinter1(Printer):

    def printer(self):
        print("Printing")