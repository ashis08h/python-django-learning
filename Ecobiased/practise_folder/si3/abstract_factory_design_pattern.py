class Button:

    def click(self):
        pass


class Checkbox:

    def checkbox(self):
        pass


class WindowsButton(Button):

    def click(self):
        print("I am in windows button click.")


class WindowsCheckbox(Checkbox):

    def checkbox(self):
        print("I am in windows checkbox.")


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
afc.create_checkbox().checkbox()