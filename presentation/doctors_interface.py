from Final.data_structures.queue import Queue
from Final.logic.day_manager import DayManager


class DoctorsInterface:
    def __init__(self, manage, user_session):
        self.manage = manage
        self.user_session = user_session
        self.day_manager = DayManager()

    def register_doctor(self):
        print("Available cities: ")
        cities = self.manage.display_cities()
        cities.print()
        print()
        print("Available specialties: ")
        spc = self.manage.display_specialities()
        spc.print()
        print()

        first_name = input("first name: ")
        last_name = input("last name: ")
        national_id = input("national ID: ")
        medical_num = input("medical number: ")
        phone_num = input("phone number: ")
        address = input("address: ")
        city = input("city: ")
        speciality = input("speciality: ")
        password = input("password: ")

        if self.manage.validate_city(city) and self.manage.validate_speciality(speciality):
            result = self.manage.register_doctor(first_name, last_name, national_id, medical_num, phone_num,
                                                 address, city, speciality, password)
            if result is True:
                print(f"Doctor with national ID {national_id} has been registered.")
            elif not result:
                print(f"Doctor with national ID {national_id} already exists.")
        else:
            print("Choose speciality and city from the list.")

    def login(self):
        phone_num = input("enter phone number: ").strip()
        password = input("enter password: ").strip()
        print()
        result = self.manage.doctor_login(phone_num=phone_num, password=password)
        if result is False:
            print("Register to the system.")
            return False
        else:
            national_id = self.manage.get_doctor(password)
            self.user_session.login(national_id)
            print(f"... Logged in ...")
            return True

    def view_patient_records(self):
        national_id = input("enter patient's national id: ").strip()
        records = self.manage.view_patient_records(national_id)
        if records:
            for day in records:
                for i in range(len(records[day])):
                    if records[day][i]:
                        dr_id = records[day][i]
                        doctor = self.manage.get_doctor_obj(dr_id)
                        print(doctor)
                print()
        else:
            print("Nothing to display.")

    def set_appointment(self):
        queue = Queue()  # stores doctor appointment time in a row
        day = input("enter day: ").strip()
        time = input("enter time(e.g. 1,2,3): ").split(",")
        for i in time:
            queue.enqueue(i)

        curr_user = self.user_session.get_current_user()
        success = self.manage.set_appointment(day, queue, curr_user)  # queue contains doctor available time
        if success:
            print("Sat new appointment.")
        else:
            print("Try again.")

    def doctor_cancel_appointment(self):
        day = input("enter day: ")
        curr_user = self.user_session.get_current_user()
        success = self.manage.doctor_cancel_appointment(day, curr_user)

    def appointments_details(self):
        curr_user = self.user_session.get_current_user()
        appointments = self.manage.appointments_details(curr_user)
        if appointments:
            for day in appointments:
                print(f"\nDay {day}:\nHour | Status")  # should be sorted in logic then passed to interface
                for i in range(len(appointments[day])):
                    print(f"{i + 1}\t  {appointments[day][i]}")
                print()
        else:
            print("Nothing to display.")

    def canceled_appointments(self):
        curr_user = self.user_session.get_current_user()
        appointments = self.manage.doctor_canceled_appointments(curr_user)
        if appointments:
            for day in appointments:
                for time in appointments[day]:
                    patient_id = appointments[day][time]
                    patient = self.manage.get_patient_obj(patient_id)
                    print(f"\nDay {day}:\nTime: {time}{patient}")
        else:
            print("Nothing to display.")

    def save_data(self):
        self.manage.save_data()

    def next_day(self):
        self.day_manager.next_day()

    def today(self):
        return self.day_manager.get_curr_day()
