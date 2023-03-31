from abc import ABC, abstractmethod


class HourglassBuilder(ABC):
    """
    Abstract class for building hourglass
    """
    @abstractmethod
    def build_top_half(self, height: int):
        pass

    @abstractmethod
    def build_bottom_half(self, height: int):
        pass

    @abstractmethod
    def build_hourglass(self, height: int):
        pass


class Hourglass:
    """
    Hourglass class which builds the hourglass using given hourglass builder
    """
    def __init__(self, hourglass_builder: HourglassBuilder):
        self.hourglass_builder = hourglass_builder

    def construct_hourglass(self, height: int):
        self.hourglass_builder.build_hourglass(height)


class AsteriskHourglassBuilder(HourglassBuilder):
    """
    Hourglass builder that creates an hourglass made of asterisks
    """
    def build_top_half(self, height: int):
        for i in range(height, 0, -1):
            print(" "*(height-i), "* "*i)

    def build_bottom_half(self, height: int):
        for i in range(2, height+1):
            print(" "*(height-i), "* "*i)

    def build_hourglass(self, height: int):
        self.build_top_half(height)
        self.build_bottom_half(height)

class DollarHourglassBuilder:
    """
    Time is money, GTM is important
    """
    def __init__(self, size):
        self.size = size
        self.grid = []
        self.build_grid()

    def build_grid(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if j < i or j >= self.size - i:
                    row.append(" ")
                else:
                    row.append("$")
            self.grid.append(row)
        for i in range(self.size-2, -1, -1):
            self.grid.append(self.grid[i])

    def display(self):
        for row in self.grid:
            print("".join(row))

builder = (lambda size: (lambda self: (lambda _:(lambda _: self.build_grid())(self))(self))(
    DollarHourglassBuilder(size)))(5)

# builder.display()


class HourglassPrinter:
    """
    Class for printing hourglass
    """
    def print_hourglass(self, hourglass: Hourglass, height: int):
        print(f"Symmetrical hourglass of height {height}:")
        hourglass.construct_hourglass(height)


if __name__ == "__main__":
    # Example usage
    height = 5
    asterisk_hourglass_builder = AsteriskHourglassBuilder()
    hourglass = Hourglass(asterisk_hourglass_builder)
    hourglass_printer = HourglassPrinter()
    hourglass_printer.print_hourglass(hourglass, height)

