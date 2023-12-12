class Button:

    def click(self):
        pass


class Checkbox:

    def check(self):
        pass


class WindowsButton(Button):

    def click(self):
        print(f"I am in button click")


class WindowsCheckbox(Checkbox):

    def check(self):
        print(f"I am in checkbox")


class FactoryMethod:

    def create_button(self):
        pass

    def create_checkbox(self):
        pass


class AbstractFactoryMethod(FactoryMethod):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


win_factory = AbstractFactoryMethod()
win_factory.create_button().click()
win_factory.create_checkbox().check()
