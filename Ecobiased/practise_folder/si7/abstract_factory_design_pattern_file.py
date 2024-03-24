from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def checkbox(self):
        pass


class WindowBoutton(Button):

    def click(self):
        print('I am from windows button')


class WindowCheckbox(Checkbox):

    def checkbox(self):
        print('I am from windows checkbox.')


class FactoryClass:

    def create_button(self):
        pass

    def create_checkbox(self):
        pass


class AbstractFactoryClass(FactoryClass):

    def create_button(self):
        return WindowBoutton()

    def create_checkbox(self):
        return WindowCheckbox()


afc = AbstractFactoryClass()
afc.create_button().click()
afc.create_checkbox().checkbox()