class PatientsInterface:
    def __init__(self, manage, user_session):
        self.manage = manage
        self.user_session = user_session

    def register_patient(self):  # phase 2
        print("available cities: ")
        cities = self.manage.display_cities()
        cities.print()
        print()

        first_name = input("first name: ")
        last_name = input("last name: ")
        national_id = input("national ID: ")
        gender = input("gender: ")
        phone_num = input("phone number: ")
        city = input("city: ")
        insurance_num = input("insurance number: ")
        password = input("password: ")

        if self.manage.validate_city(city):
            result = self.manage.register_patient(first_name, last_name, national_id, phone_num, password, gender,
                                                  city, insurance_num)
            if result is True:
                print(f"Patient with national ID {national_id} has been registered.")
            elif result is False:
                print(f"Patient with national ID {national_id} already exists.")
        else:
            print("choose city from the list.")

    def login(self):  # phase 2
        phone_num = input("enter phone number: ")
        password = input("enter password: ")
        print()
        result = self.manage.patient_login(phone_num=phone_num, password=password)
        if result is False:
            print("register to the system.")
            return False
        else:
            national_id = self.manage.get_patient(password)
            self.user_session.login(national_id)
            print(f"... logged-in ...")
            return True

    def display_doctors(self):  # phase 2
        print("1. -By city")
        print("2. -By speciality")
        print("3. -By city and speciality")

        command = int(input(">>> ").strip())
        if command == 1:
            city = input("enter city name: ").strip()
            print()
            result = self.manage.doctors_by_city(city)
            if result is None:
                print(f"not found.")
            print(f"Doctors in {city}:")
            for doctor in result:
                print(doctor)

        elif command == 2:
            spc = input("enter speciality: ").strip()
            print()
            result = self.manage.doctors_by_speciality(spc)
            if result is None:
                print(f"not found.")
            print(f"Doctors in {spc} field:")
            for doctor in result:
                print(doctor)

        elif command == 3:
            city = input("enter city name: ").strip()
            spc = input("enter speciality: ").strip()
            result = self.manage.speciality_city(city, spc)
            print()
            if result is None:
                print(f"not found.")
            print(f"Doctors in {spc} field in {city}: ")
            for doctor in result:
                print(doctor)

    def search_name(self):  # phase 2 search doctor by name
        name = input("enter doctor name: ").strip()
        doctor = self.manage.patient_search_name(name)
        if doctor is not None:
            print(doctor)
        else:
            print("no doctor found !")

    def make_appointment(self):
        print()
        print("********** making an appointment **********")
        print()
        city = input("enter city name: ").strip()
        spc = input("enter speciality: ").strip()
        print()
        result = self.manage.speciality_city(city, spc)
        for i in range(len(result)):
            print(i + 1, result[i])

        print("please select a doctor: ")
        index = int(input(">>> ").strip())
        print()

        if 0 <= index - 1 <= len(result):
            selected_doctor = result[index - 1]
            print("Schedule: \n -None : unknown\n -Available : reachable\n -Not available : booked\n")
            schedule = selected_doctor.schedule.get_schedule()

            for day in schedule:
                print(f"Day {day}:\nHour | Status")  # should be sorted in logic then passed to interface
                for i in range(len(schedule[day])):
                    print(f"{i + 1}\t  {schedule[day][i]}")
                print()

            day = input("enter day to make an appointment at: ").strip()
            time = input("enter time to make an appointment at: ").strip()
            available = selected_doctor.schedule.is_available(day, time)

            if available:
                patient_id = self.user_session.get_current_user()
                if self.manage.make_appointment(day, time, selected_doctor.national_id, patient_id):
                    print(f"Made an appointment with Dr.{selected_doctor.full_name} in day {day} at {time}.")
                else:
                    print("Try again.")

            else:
                print("No available appointment at this time.")

        else:
            print("Try again.")

    def view_appointments_history(self):
        patient_id = self.user_session.get_current_user()
        appointments = self.manage.view_appointments_history(patient_id)

        if appointments:
            for day in appointments:
                for time in range(len(appointments[day])):
                    if appointments[day][time]:
                        doctor_id = appointments[day][time]
                        doctor = self.manage.get_doctor_obj(doctor_id)
                        print(f"\nDay {day}:\nTime: {time + 1}\n{doctor}")
        else:
            print("Nothing to display.")

    def patient_cancel_appointments(self):
        print()
        day = input("day to cancel appointment: ")
        time = input("time to cancel appointment: ")
        print()

        patient_id = self.user_session.get_current_user()
        result = self.manage.patient_cancel_appointments(day, time, patient_id)
        if result:
            print("canceled.")
        else:
            print("try again.")

    def display_canceled_appointments(self):
        patient_id = self.user_session.get_current_user()
        canceled = self.manage.display_cancelled_appointments(patient_id)
        if canceled:
            for day in canceled:
                for time in canceled[day]:
                    if canceled[day][time]:
                        dr_id = canceled[day][time]
                        doctor = self.manage.get_doctor_obj(dr_id)
                        print(f"\nDay {day}:\nTime: {time}\n{doctor}")
        else:
            print("Nothing to display.")

    def auto_reservation(self):
        city = input("enter city name: ").strip()
        spc = input("enter speciality: ").strip()

        patient_id = self.user_session.get_current_user()
        result = self.manage.speciality_city(city, spc)  # result is an array of all doctors in specific city and spc
        self.manage.auto_reservation(result, patient_id)

    def save_data(self):
        self.manage.save_data()
