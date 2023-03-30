from abc import ABC, abstractmethod

class GreetingStrategy(ABC):
    @abstractmethod
    def greet(self, name: str) -> str:
        pass

class FormalGreetingStrategy(GreetingStrategy):
    def greet(self, name: str) -> str:
        return f"Good day, {name}."

class InformalGreetingStrategy(GreetingStrategy):
    def greet(self, name: str) -> str:
        return f"Hey, {name}! What's up?"

class GreetingService:
    def __init__(self, strategy: GreetingStrategy):
        self._strategy = strategy

    def greet(self, name: str):
        return self._strategy.greet(name)

class ConsoleIO:
    def read_input(self) -> str:
        return input("Please enter your name: ")

    def write_output(self, message: str):
        print(message)

def main():
    io = ConsoleIO()
    strategy = InformalGreetingStrategy()
    service = GreetingService(strategy)

    name = io.read_input()
    message = service.greet(name)
    io.write_output(message)

if __name__ == "__main__":
    main()

