class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, number):
        if self._successor:
            return self._successor.handle(number)


class FizzBuzzHandler(Handler):
    def handle(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        else:
            return super().handle(number)


class FizzHandler(Handler):
    def handle(self, number):
        if number % 3 == 0:
            return "Fizz"
        else:
            return super().handle(number)


class BuzzHandler(Handler):
    def handle(self, number):
        if number % 5 == 0:
            return "Buzz"
        else:
            return super().handle(number)


class NumberHandler(Handler):
    def handle(self, number):
        return str(number)


class FizzBuzz:
    def __init__(self):
        self._handler = FizzBuzzHandler(FizzHandler(BuzzHandler(NumberHandler())))

    def play(self, n):
        for i in range(1, n+1):
            print(self._handler.handle(i))

