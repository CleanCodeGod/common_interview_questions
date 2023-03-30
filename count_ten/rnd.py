from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, value):
        for observer in self._observers:
            observer.update(value)


class Observer(ABC):
    @abstractmethod
    def update(self, value):
        pass


class EvenNumberObserver(Observer):
    def update(self, value):
        if value % 2 == 0:
            print(value)


class Counter:
    def __init__(self):
        self.subject = Subject()

    def count_up_to_ten(self):
        for i in range(1, 11):
            self.subject.notify(i)


if __name__ == '__main__':
    counter = Counter()
    even_number_observer = EvenNumberObserver()
    counter.subject.attach(even_number_observer)
    counter.count_up_to_ten()

