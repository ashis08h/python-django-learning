from abc import abstractmethod, ABC


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
        print("I am from click")


class WindowCheckbox(Checkbox):

    def check(self):
        print("I am from checkbox")


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
        return WindowCheckbox()


afc = AbstractFactoryClass()
afc.create_checkbox().check()
afc.create_button().click()