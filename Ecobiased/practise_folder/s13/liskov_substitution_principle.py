class Bird:
    def fly(self):
        return "Flying in the sky"


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("penguins can't fly!")


def make_bird_fly(bird: Bird):
    print(bird.fly())


make_bird_fly(Bird())
# make_bird_fly((Penguin())) this will fail.


# correct use case is

class Bird:
    def make_sound(self):
        return "Generic bird sound"


class FlyingBird(Bird):
    def fly(self):
        return 'Flying'


class NonFlyingBird(Bird):
    def walk(self):
        return 'Walking'


# Now subclass

class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow is flying."


class Penguin1(NonFlyingBird):
    def walk(self):
        return "Penguin is walking."


print(Sparrow().fly())
print(Penguin1().walk())