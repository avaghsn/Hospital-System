from Final.data_structures.array import Array
from Final.tools.sorts import insertion_sort
from Final.logic.day_manager import DayManager


class Manage:
    def __init__(self, doctors, patients, specialities, cities):
        self.cities = cities
        self.specialities = specialities
        self.patients = patients
        self.doctors = doctors
        self.day_manager = DayManager()

    # ******************************* admin ******************************** #

    def admin_display_doctors(self):  # phase 1
        result = self.doctors.display_all()
        return result

    def admin_search_id(self, dr_id):  # phase 1
        result = self.doctors.search_id(dr_id)
        return result

    def admin_display_speciality(self, name):  # phase 1
        result = self.doctors.display_speciality(name)
        return result

    def admin_add_city(self, name):
        boolean = self.cities.add_city(name=name)
        return boolean

    def admin_add_speciality(self, name):
        boolean = self.specialities.add_speciality(name=name)
        return boolean

    def display_cities(self):
        return self.cities.get_cities()

    def display_specialities(self):
        return self.specialities.get_specialities()

    def validate_city(self, city):
        return self.cities.validate(city)

    def validate_speciality(self, name):
        return self.specialities.validate(name)

    def delete_patient(self, national_id):
        return self.patients.delete_patient(national_id)

    def delete_doctor_id(self, national_id):
        return self.doctors.delete_doctor_id(national_id)

    def delete_doctor_med_num(self, med_num):
        return self.doctors.delete_doctor_id(med_num)

    def display_all_patients(self):
        return self.patients.display_all_patients()

    # ******************************* doctor ******************************** #

    def get_doctor(self, password):
        return self.doctors.get_doctor(password)

    def get_doctor_obj(self, national_id):
        return self.doctors.get_doctor_obj(national_id)

    def register_doctor(self, first_name, last_name, national_id, medical_num, phone_num, address, city, speciality,
                        password):
        boolean = self.doctors.register_doctor(first_name, last_name, national_id, medical_num, phone_num, address,
                                               city, speciality, password)
        return boolean

    def doctor_login(self, phone_num, password):
        result = self.doctors.login(phone_num=phone_num, password=password)
        return result

    def view_patient_records(self, national_id):
        patient = self.patients.get_patient_obj(national_id)
        if patient:
            return patient.appointments.appointments_history()

    def set_appointment(self, day, queue, curr_user):
        today = self.day_manager.get_curr_day()
        if int(day) != int(today) and int(today) + 1 <= int(day) <= int(today) + 7:
            doctor = self.get_doctor_obj(curr_user)
            if doctor:
                doctor.schedule.set_schedule(day, queue)
                return True
        return False

    def doctor_cancel_appointment(self, day, curr_user):
        doctor = self.get_doctor_obj(curr_user)
        if doctor:
            doctor.decrement_visits()
            doctor.schedule.cancel_appointment(day)
            ids = doctor.appointments.cancel_appointment(day)
            if ids:
                while not ids.is_empty():
                    patient_id = ids.dequeue()
                    patient = self.get_patient_obj(patient_id)
                    time = patient.appointments.canceled_by_doctor(day, curr_user)
                    patient.appointments.cancel_appointment(day, time)
                return True

    def appointments_details(self, curr_user):
        doctor = self.get_doctor_obj(curr_user)
        if doctor:
            return doctor.schedule.get_schedule()

    def doctor_canceled_appointments(self, curr_user):
        doctor = self.get_doctor_obj(curr_user)
        if doctor:
            return doctor.appointments.get_canceled()

    # ******************************* patient ******************************** #

    def get_patient(self, password):
        return self.patients.get_patient(password)

    def get_patient_obj(self, national_id):
        return self.patients.get_patient_obj(national_id)

    def register_patient(self, first_name, last_name, national_id, phone_num, password, gender, city,
                         insurance_num):  # phase 2
        boolean = self.patients.register_patient(first_name, last_name, national_id, phone_num, password, gender, city,
                                                 insurance_num)
        return boolean

    def patient_login(self, phone_num, password):  # phase 2
        result = self.patients.login(phone_num=phone_num, password=password)
        return result

    def doctors_by_city(self, city):  # phase 2
        queue = self.doctors.doctors_by_city(city)
        arr_size = len(queue)
        arr = Array(arr_size)
        for i in range(len(arr)):
            doctor = queue.dequeue()
            arr[i] = doctor

        sorted_arr = insertion_sort(arr, lambda dr: dr.visits)
        return sorted_arr

    def doctors_by_speciality(self, spc):  # phase 2
        queue = self.doctors.doctors_by_speciality(spc)
        arr_size = len(queue)
        arr = Array(arr_size)
        for i in range(len(arr)):
            doctor = queue.dequeue()
            arr[i] = doctor

        sorted_arr = insertion_sort(arr, lambda dr: dr.visits)
        return sorted_arr

    def speciality_city(self, city, speciality):  # phase 2
        queue = self.doctors.speciality_city(city, speciality)
        return queue

    def patient_search_name(self, name):
        return self.doctors.search_name(name)

    def make_appointment(self, day, time, patient_id, doctor_id):
        doctor = self.doctors.get_doctor_obj(doctor_id)
        patient = self.patients.get_patient_obj(patient_id)
        patient.appointments.make_appointment(day, time, doctor_id)
        doctor.appointments.add_appointment(day, time, patient_id)
        doctor.increment_visits()
        return doctor.schedule.remove_availability(day, time)

    def view_appointments_history(self, patient_id):
        patient = self.patients.get_patient_obj(patient_id)
        return patient.appointments.appointments_history()

    def patient_cancel_appointments(self, day, time, patient_id):  # patient cancels an appointment
        today = self.day_manager.get_curr_day()
        if today != int(day):
            patient = self.patients.get_patient_obj(patient_id)
            doctor_id = patient.appointments.cancel_appointment(day, time)
            doctor = self.doctors.get_doctor_obj(doctor_id)
            doctor.decrement_visits()
            doctor.schedule.restore_availability(day, time)
            doctor.appointments.create_canceled(day, time, patient_id)
            return True
        return False

    def display_cancelled_appointments(self, patient_id):
        patient = self.get_patient_obj(patient_id)
        return patient.appointments.cancelled_appointments()

    def auto_reservation(self, doctors, patient_id):
        self.patients.auto_reservation(doctors, patient_id)

    # ******************************* any ******************************** #

    def save_data(self):
        self.doctors.save_data()
        self.patients.save_data()
        self.cities.save_data()
        self.specialities.save_data()

    def next_day(self):
        self.doctors.next_day()
