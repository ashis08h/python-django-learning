from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def check(self):
        pass


class WindowButton(Button):

    def click(self):
        print("I am from click method from windowbutton class")


class WindowCheckBox(Checkbox):

    def check(self):
        print("I am from check method from windowcheckbox class")


class FactoryClass(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class AbstractFactoryClass(FactoryClass):

    def create_button(self):
        return WindowButton()

    def create_checkbox(self):
        return WindowCheckBox()


afc = AbstractFactoryClass()
afc.create_button().click()
afc.create_checkbox().check()