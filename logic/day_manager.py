from Final.tools.file_handling import File


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DayManager(metaclass=Singleton):
    def __init__(self):
        self.file = File("C:\\Users\\AVA\\PycharmProjects\\pythonProject\\Data_Structure\\Final\\test_files\\Days.txt")
        self.curr_day = self.load_day()

    def load_day(self):
        if self.file.is_exist():
            return int(self.file.read())
        else:
            return 1  # starting from day 1

    def save_day(self):
        self.file.write(str(self.curr_day))

    def next_day(self):
        self.curr_day += 1
        self.save_day()

    def get_curr_day(self):
        return self.curr_day
