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
        print(f"I am from WindowButton class")


class WindowCheckbox(Checkbox):

    def check(self):
        print(f"I am from WindowCheckbox class")


class FactoryClass(ABC):

    @abstractmethod
    def create_button(self):
        pass

    def create_checkbox(self):
        pass


class AbstractFactoryClass(FactoryClass):

    def create_button(self):
        return WindowButton()

    def create_checkbox(self):
        return WindowCheckbox()


abfc = AbstractFactoryClass()
abfc.create_button().click()
abfc.create_checkbox().check()