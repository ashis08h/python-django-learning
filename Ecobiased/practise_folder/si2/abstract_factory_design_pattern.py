class Button:

    def click(self):
        pass


class Checkbox:

    def check(self):
        pass


class WindowsButton(Button):

    def click(self):
        print("Windows button clicked.")


class WindowsCheck(Button):

    def check(self):
        print("Windows checkbox checked.")


class FactoryClass:

    def create_button(self):
        pass

    def create_checkbox(self):
        pass


class AbstractFactoryClass(FactoryClass):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheck()


abs = AbstractFactoryClass()
abs.create_button().click()
abs.create_checkbox().check()