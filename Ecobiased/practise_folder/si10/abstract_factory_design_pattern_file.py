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
        print(f"I am from window button.")


class WindowCheckbox(Checkbox):

    def check(self):
        print(f"I am from window Check box.")


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


afc = AbstractFactoryClass()
afc.create_button().click()
afc.create_checkbox().check()