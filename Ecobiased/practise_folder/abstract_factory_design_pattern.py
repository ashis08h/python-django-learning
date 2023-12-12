class Button:

    def click(self):
        pass


class Checkbox:

    def check(self):
        pass


class WindowsButton(Button):

    def click(self):
        print("Windows button click.")


class WindowsCheckbox(Checkbox):

    def check(self):
        print("Windows checkbox checked.")


class MacOsButton(Button):

    def click(self):
        print("MacOs button click.")


class MacOsCheckBox(Checkbox):

    def check(self):
        print("MacOs checkbox checked.")


class GUIFactory:

    def create_button(self):
        pass

    def create_checkbox(self):
        pass


class WindowsGUIFactory(GUIFactory):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacOsGUIFactory(GUIFactory):

    def create_button(self):
        return MacOsButton()

    def create_checkbox(self):
        return MacOsCheckBox()


def create_gui(factory):

    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return button, checkbox


windows_factory = WindowsGUIFactory()
macos_factory = MacOsGUIFactory()

windows_button, windows_checkbox = create_gui(windows_factory)
macos_button, macos_checkbox = create_gui(macos_factory)

windows_button.click()
windows_checkbox.check()
macos_button.click()
macos_checkbox.check()
