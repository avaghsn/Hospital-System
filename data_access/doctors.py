from Final.data_structures.hash_table import DynamicHash
from Final.data_structures.queue import Queue
from Final.data_structures.linked_list import SLL
from Final.data_structures.array import DynamicArray

from Final.models.doctor import Doctor

from Final.tools.file_handling import File


class Doctors:
    def __init__(self):
        self.doctors = DynamicHash()  # national id -> doctor obj
        self.signed_in = DynamicHash()  # password -> national id
        self.table = DynamicHash()  # table of cities -> table of specialties -> sll of ids

        self.load_data()

    # ******************************* phase 1 ******************************** #

    def load_data(self):
        path = "C:\\Users\\AVA\\PycharmProjects\\pythonProject\\Data_Structure\\Final\\test_files\\Doctors.txt"
        lines = File(path).read_line()
        for line in lines:
            line = line.replace("\n", "")
            item = line.split('-')

            first_name, last_name, national_id, medical_num, phone_num, address, city, speciality, password = item[0], \
                item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8]

            self.register_doctor(first_name, last_name, national_id, medical_num, phone_num, address, city,
                                 speciality, password)

    def save_data(self):
        path = "C:\\Users\\AVA\\PycharmProjects\\pythonProject\\Data_Structure\\Final\\test_files\\Doctors.txt"
        file = File(path)
        file.write("")
        for ids in self.doctors:
            doctor = self.doctors[ids]
            line = (f"{doctor.first_name}-{doctor.last_name}-{doctor.national_id}-{doctor.medical_num}-"
                    f"{doctor.phone_num}-{doctor.address}-{doctor.city}-{doctor.speciality}-{doctor.password}")
            file.append(line)

    def register_doctor(self, first_name, last_name, national_id, medical_num, phone_num, address, city, speciality,
                        password):

        doctor = Doctor(first_name, last_name, national_id, medical_num, phone_num, address, city, speciality,
                        password)

        # national ids inside specialty in each city
        if doctor.city not in self.table:
            self.table[doctor.city] = DynamicHash()

        if doctor.speciality not in self.table[doctor.city]:
            self.table[doctor.city][doctor.speciality] = SLL()
        self.table[doctor.city][doctor.speciality].add_first(doctor.national_id)

        # insert doctor obj
        if doctor.national_id not in self.doctors:
            self.doctors[doctor.national_id] = doctor
            self.signed_in[doctor.password] = doctor.national_id
            return True
        return False

    def display_all(self):
        queue = Queue()
        for doctor in self.doctors:
            queue.enqueue(self.doctors[doctor])
        return queue

    def search_id(self, dr_id):
        return self.doctors[dr_id]

    def display_speciality(self, speciality):
        queue = Queue()
        for city in self.table:
            if speciality in self.table[city]:
                if self.table[city][speciality]:
                    sll = self.table[city][speciality]
                    for ids in sll:
                        if ids.data in self.doctors:
                            queue.enqueue(self.doctors[ids.data])
        return queue

    # ******************************* phase 2 ******************************** #

    def doctors_by_city(self, city):  # displays doctors to patient by city name
        queue = Queue()
        if city in self.table:
            for speciality in self.table[city]:
                if self.table[city][speciality]:
                    sll = self.table[city][speciality]
                    for ids in sll:
                        if ids.data in self.doctors:
                            queue.enqueue(self.doctors[ids.data])
        return queue

    def doctors_by_speciality(self, speciality):  # displays doctors by speciality
        queue = Queue()
        for city in self.table:
            if speciality in self.table[city]:
                if self.table[city][speciality]:
                    sll = self.table[city][speciality]
                    for ids in sll:
                        if ids.data in self.doctors:
                            queue.enqueue(self.doctors[ids.data])
        return queue

    def speciality_city(self, city, speciality):  # displays doctors by city and speciality
        array = DynamicArray()
        if city in self.table:
            if speciality in self.table[city]:
                if self.table[city][speciality]:
                    sll = self.table[city][speciality]
                    for node in sll:
                        if node.data in self.doctors:
                            array.append(self.doctors[node.data])
        return array

    def search_name(self, name):  # returns a doctor by full name
        for ids in self.doctors:
            doctor = self.doctors[ids]
            if doctor is not None or "deleted":
                if doctor.full_name == name:
                    return doctor
        return None

    def login(self, phone_num, password):
        national_id = self.signed_in[password]
        if national_id is not None:
            doctor = self.doctors[national_id]
            if phone_num == doctor.phone_num:
                return True
            else:
                return False
        return False

    def delete_doctor_id(self, national_id):  # deletes a doctor by national id
        if national_id in self.doctors:
            doctor = self.doctors[national_id]
            del self.signed_in[doctor.password]
            del self.doctors[national_id]
            return True
        else:
            return None

    def delete_doctor_med_num(self, med_num):  # deletes a doctor by medical num
        for ids in self.doctors:
            if med_num == self.doctors[ids].mediacal_num:
                doctor = self.doctors[ids]
                del self.signed_in[doctor.password]
                del self.doctors[ids]
                return True
        return False

    # ******************************* any ******************************** #

    def get_doctor(self, password):  # returns national id of doctor
        return self.signed_in[password]

    def get_doctor_obj(self, dr_id):  # returns doctor obj
        if self.doctors[dr_id]:
            return self.doctors[dr_id]

    def get_all_doctors(self):
        return self.doctors

    def next_day(self):
        for ids in self.doctors:
            if self.doctors[ids]:
                if self.doctors[ids].schedule:
                    self.doctors[ids].schedule.delete_out_of_range()
        return None
