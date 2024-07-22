from Final.data_structures.hash_table import DynamicHash
from Final.data_structures.heap import MinHeap

from Final.models.appointment import Node
from Final.models.patient import Patient

from Final.tools.file_handling import File


class Patients:
    def __init__(self):
        self.patients = DynamicHash()  # national id -> patient obj
        self.signed_in = DynamicHash()  # password -> national id
        self.load_data()

    def get_patient(self, password):  # returns patient national id
        return self.signed_in[password]

    def get_patient_obj(self, national_id):
        return self.patients[national_id]

    def load_data(self):
        path = "C:\\Users\\AVA\\PycharmProjects\\pythonProject\\Data_Structure\\Final\\test_files\\Patients.txt"
        lines = File(path).read_line()
        for line in lines:
            line = line.replace("\n", "")
            item = line.split('-')

            first_name, last_name, national_id, phone_num, password, gender, city, insurance_num = \
                item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7],

            self.register_patient(first_name, last_name, national_id, phone_num, password, gender, city, insurance_num)

    def save_data(self):
        path = "C:\\Users\\AVA\\PycharmProjects\\pythonProject\\Data_Structure\\Final\\test_files\\Patients.txt"
        file = File(path)
        file.write("")
        for ids in self.patients:
            patient = self.patients[ids]
            line = (f"{patient.first_name}-{patient.last_name}-{patient.national_id}-{patient.phone_num}"
                    f"-{patient.password}-{patient.gender}-{patient.city}-{patient.insurance_num}")
            file.append(line)

    def register_patient(self, first_name, last_name, national_id, phone_num, password, gender, city, insurance_num):
        patient = Patient(first_name, last_name, national_id, phone_num, password, gender, city, insurance_num)

        if patient.national_id not in self.patients:
            self.patients[patient.national_id] = patient
            self.signed_in[patient.password] = patient.national_id
            return True
        else:
            return False

    def login(self, phone_num, password):
        national_id = self.signed_in[password]
        if national_id is not None:
            patient = self.patients[national_id]
            if patient.phone_num == phone_num:
                return True
            else:
                return False
        return False

    def delete_patient(self, national_id):
        if national_id in self.patients:
            del self.patients[national_id]
            return True
        else:
            return False

    def display_all_patients(self):
        return self.patients

    # ******************************* phase 3 ******************************** #

    def find_nearest_appointment(self, doctors):
        min_heap = MinHeap()
        for i in range(len(doctors)):
            doctor = doctors[i]
            day, hour = doctor.schedule.find_nearest()
            node = Node(doctor, day, hour)
            min_heap.insert(node)
            nearest = min_heap.extract_min()
            return nearest

    def auto_reservation(self, doctors, patient_id):
        patient = self.get_patient_obj(patient_id)
        nearest = self.find_nearest_appointment(doctors)
        patient.appointments.make_appointment(nearest.day, nearest.hour, nearest.doctor.national_id)
        nearest.doctor.schedule.remove_availability(nearest.day, nearest.hour)
