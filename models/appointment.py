class Node:
    def __init__(self, doctor, day, hour):
        self.doctor = doctor
        self.day = day
        self.hour = hour

    def __lt__(self, other):
        if self.day == other.day:
            return self.hour > other.hour

    def __repr__(self):
        return f"Day {self.day}\nTime: {self.hour}\nDoctor: {self.doctor}"