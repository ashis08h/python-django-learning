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
        print("I am from windows click.")


class WindowsCheckbox(Checkbox):

    def check(self):
        print("I am from windows check")


class FactoryClass(ABC):

    @abstractmethod
    def create_button(self):
        pass

    def create_checkbox(self):
        pass


class AbstractFactoryClass(FactoryClass):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


afc = AbstractFactoryClass()
afc.create_checkbox().check()
afc.create_button().click()