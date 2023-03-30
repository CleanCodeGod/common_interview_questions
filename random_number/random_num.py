from random import Random
from typing import List


class RandomNumberGenerator:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.rng = Random()
        return cls.__instance

    def generate_number(self, range_start: int = 1, range_end: int = 100) -> int:
        number = self.rng.randint(range_start, range_end)
        self.notify_observers(number)
        return number

    def attach_observer(self, observer) -> None:
        self.observers.append(observer)

    def detach_observer(self, observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self, number: int) -> None:
        for observer in self.observers:
            observer.update(number)


class RandomNumberObserver:
    def update(self, number: int) -> None:
        print(f"A new random number has been generated: {number}")


class RangeDecorator:
    def __init__(self, rng: RandomNumberGenerator, range_start: int, range_end: int):
        self.rng = rng
        self.range_start = range_start
        self.range_end = range_end

    def generate_number(self) -> int:
        return self.rng.generate_number(self.range_start, self.range_end)


rng = RandomNumberGenerator()
rng.attach_observer(RandomNumberObserver())

rng_with_range = RangeDecorator(rng, 50, 150)
print(rng_with_range.generate_number())

