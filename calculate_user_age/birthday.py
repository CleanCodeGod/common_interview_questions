class BirthDateSingleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if BirthDateSingleton.__instance == None:
            BirthDateSingleton()
        return BirthDateSingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if BirthDateSingleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            BirthDateSingleton.__instance = self

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def get_birth_date(self):
        return self.birth_date

class App:
    def __init__(self, birth_date_singleton):
        self.birth_date_singleton = birth_date_singleton

    def run(self):
        birth_date_str = input("Please enter your birth date (in YYYY-MM-DD format): ")
        year, month, day = map(int, birth_date_str.split("-"))
        birth_date = BirthDate(year=year, month=month, day=day)
        self.birth_date_singleton.set_birth_date(birth_date)

        age_calculator = AgeCalculator(self.birth_date_singleton)
        age_calculator.calculate_age()

class AgeCalculator:
    def __init__(self, birth_date_singleton):
        self.birth_date_singleton = birth_date_singleton

    def calculate_age(self, algorithm="standard"):
        birth_date = self.birth_date_singleton.get_birth_date()
        current_date = datetime.datetime.now()

        if algorithm == "standard":
            age = current_date.year - birth_date.year
        elif algorithm == "leap_year":
            age = (current_date - birth_date).days / 365.2425
        elif algorithm == "dog_years":
            age = (current_date.year - birth_date.year) * 7
        else:
            raise ValueError("Invalid algorithm type")

        print(f"Your age is: {age}")
