from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def check(self):
        pass


class WindowsButton(Button):

    def click(self):
        print("I am from windows button.")


class WindowsCheckbox(Checkbox):

    def check(self):
        print("I am from windows checkbox.")


class FactoryClass(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class AbstractFactoryClass(FactoryClass):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


afc = AbstractFactoryClass()
afc.create_button().click()
afc.create_checkbox().check()
