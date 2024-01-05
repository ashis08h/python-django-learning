class Button:

    def click(self):
        pass


class CheckBox:

    def checkbox(self):
        pass


class WindowsButton(Button):

    def click(self):
        print("I am from windows button.")


class WindowsCheckbox(CheckBox):

    def checkbox(self):
        print("I am from windows checkbox.")


class FactoryClass:

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
afc.create_button().click()
afc.create_checkbox().checkbox()