def greet(fx):
    def mfx():
        print("good morning.")
        fx()
        print("thanks for coming.")
    return mfx


@greet
def hello():
    print("say hello to everyone.")


hello()


def greet1(fx):
    def mfx(*args, **kwargs):
        print("Good afternoon.")
        fx(*args, **kwargs)
        print("Thanks for info")
    return mfx


@greet1
def add(a, b):
    print(a+b)


add(6,8)
