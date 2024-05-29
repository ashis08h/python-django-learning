from abc import ABC, abstractmethod


class Button(ABC):
    def click(self):
        pass


class Checkbox(ABC):
    def check(self):
        pass


class WindowsButton(Button):
    def click(self):
        print('I am from windows button.')


class WindowsCheckbox(Checkbox):
    def check(self):
        print('I am from windows checkbox.')


class FactoryClass:

    def create_button(self):
        pass

    def create_checkbox(self):
        pass


class AbstractFactoryClass:

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


afc = AbstractFactoryClass()
afc.create_button().click()
afc.create_checkbox().check()