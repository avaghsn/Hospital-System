from Final.data_structures.array import Array
from Final.data_structures.hash_table import DynamicHash


class Patient:
    def __init__(self, first_name, last_name, national_id, phone_num, password, gender, city, insurance_num):
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.phone_num = phone_num
        self.password = password
        self.gender = gender
        self.city = city
        self.full_name = f"{self.first_name} {self.last_name}"
        self.insurance_num = insurance_num
        self.appointments = Appointments()

    def __str__(self):
        info = (f"\n-Patient: \n name: {self.first_name} {self.last_name} \n id: {self.national_id} "
                f"\n gender: {self.gender} \n contact info: {self.phone_num} \n city: {self.city} "
                f"\n insurance number: {self.insurance_num} \n password: {self.password}\n")
        return info


class Appointments:
    def __init__(self):
        self.appointments = DynamicHash()  # table of days -> array sized 12 (time - 1 == index, doctor id == val)
        self.canceled = DynamicHash()

    def make_appointment(self, day, time, doctor_id):
        time = int(time) - 1
        if day not in self.appointments:
            self.appointments[day] = Array(12)
        self.appointments[day][time] = doctor_id

    def appointments_history(self):
        return self.appointments

    def cancel_appointment(self, day, time):
        if day in self.appointments:
            if self.appointments[day][int(time) - 1]:
                dr_id = self.appointments[day][int(time) - 1]
                self.create_cancelled(day, time, dr_id)
                self.appointments[day][int(time) - 1] = None
                del self.appointments[day][int(time) - 1]
                return dr_id

    def canceled_by_doctor(self, day, doctor_id):
        if day in self.appointments:
            for time in range(len(self.appointments[day])):
                if self.appointments[day][time] == doctor_id:
                    return int(time) + 1

    def create_cancelled(self, day, time, doctor_id):
        if day not in self.canceled:
            self.canceled[day] = DynamicHash()
        self.canceled[day][str(time)] = doctor_id

    def cancelled_appointments(self):
        return self.canceled
