from Final.data_structures.array import Array
from Final.data_structures.hash_table import DynamicHash
from Final.data_structures.queue import Queue
from Final.logic.day_manager import DayManager
from Final.tools.sorts import insertion_sort2


class Doctor:
    def __init__(self, first_name, last_name, national_id, medical_num, phone_num, address, city, speciality,
                 password):
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.medical_num = medical_num
        self.phone_num = phone_num
        self.address = address
        self.city = city
        self.speciality = speciality
        self.password = password
        self.visits = 0
        self.full_name = f"{self.first_name} {self.last_name}"
        self.schedule = Schedule()
        self.appointments = Appointments()

    def __repr__(self):
        info = (f"-Doctor: \n name: {self.first_name} {self.last_name} \n id: {self.national_id} "
                f"\n medical number: {self.medical_num} \n contact info: {self.phone_num} \n city: {self.city} "
                f"\n address: {self.address} \n specialization: {self.speciality} \n number of visits: {self.visits} "
                f"\n password: {self.password}\n")
        return info

    def increment_visits(self):
        self.visits += 1

    def decrement_visits(self):
        self.visits -= 1


class Schedule:
    def __init__(self):
        self.schedule = DynamicHash()
        self.day_manager = DayManager()

    def set_schedule(self, day, queue):
        today = self.day_manager.get_curr_day()
        while not queue.is_empty():
            time = queue.dequeue()
            time = int(time) - 1
            if int(today) != int(day) and int(today) + 1 <= int(day) <= int(today) + 7 and 0 <= time <= 11:
                if day not in self.schedule:
                    self.schedule[day] = Array(12)
                self.schedule[day][time] = "Available"

    def get_schedule(self):
        return self.schedule

    def is_available(self, day, time):
        time = int(time) - 1
        if self.schedule[day]:
            if self.schedule[day][time] == "Available":
                return True
            else:
                return False

    def remove_availability(self, day, time):
        time = int(time) - 1
        if self.schedule[day]:
            if self.schedule[day][time] == "Available":
                self.schedule[day][time] = "Not Available"
                return True
        return False

    def restore_availability(self, day, time):
        time = int(time) - 1
        if self.schedule[day]:
            if self.schedule[day][time] == "Not Available":
                self.schedule[day][time] = "Available"
                return True
        return False

    def cancel_appointment(self, day):
        if self.schedule[day]:
            for i in range(len(self.schedule[day])):
                if self.schedule[day][i] == "Available" or self.schedule[day][i] == "Not Available":
                    self.schedule[day][i] = "canceled"
            return True
        return False

    def delete_out_of_range(self):
        to_delete = Queue()
        today = self.day_manager.get_curr_day()
        for day in self.schedule:
            if today > int(day):
                for i in range(len(self.schedule[day])):
                    to_delete.enqueue(day)

        while not to_delete.is_empty():
            day = to_delete.dequeue()
            del self.schedule[day]

    def sort_days(self):
        queue = Queue()
        schedule = self.schedule
        length = len(schedule)
        days = Array(length)

        for day in schedule:
            queue.enqueue(day)

        while not queue.is_empty():
            for i in range(len(days)):
                days[i] = queue.dequeue()

        sorted_days = insertion_sort2(days)

        return sorted_days

    def find_nearest(self):
        sorted_days = self.sort_days()
        for i in range(len(sorted_days)):
            if sorted_days[i] in self.schedule:
                index = sorted_days[i]
                for time in range(len(self.schedule[index])):
                    if self.schedule[index][time] is not None and self.schedule[index][time] != "Not Available":
                        return sorted_days[i], time + 1  # sorted_days[i] == day


class Appointments:
    def __init__(self):
        self.appointments = DynamicHash()  # table of days -> array sized 12 (time - 1 == index)
        self.canceled = DynamicHash()

    def add_appointment(self, day, time, patient_id):
        time = int(time) - 1
        if 0 <= time <= 11:
            if day not in self.appointments:
                self.appointments[day] = Array(12)
            self.appointments[day][time] = patient_id
        return False

    def create_canceled(self, day, time, patient_id):
        time = str(time)
        if day not in self.canceled:
            self.canceled[day] = DynamicHash()
        self.canceled[day][time] = patient_id

    def cancel_appointment(self, day):
        queue = Queue()
        if day in self.appointments:
            for time in range(len(self.appointments[day])):
                if self.appointments[day][int(time) - 1]:
                    patient_id = self.appointments[day][int(time) - 1]
                    queue.enqueue(patient_id)
                    self.create_canceled(day, int(time) + 1, patient_id)
                    self.appointments[day][int(time) - 1] = None
            return queue

    def get_canceled(self):
        return self.canceled
