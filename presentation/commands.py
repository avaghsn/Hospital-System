import os
import Final.presentation.CLI as CLI
from Final.logic.day_manager import DayManager


class AdminCommands:
    def __init__(self, admin_interface):
        self.admin_interface = admin_interface

    def admin_panel(self):
        while True:
            print(CLI.admin_panel)
            command = input("Enter your choice (0-8): ")

            if command == "0":
                self.admin_interface.save_data()
                break
            elif command == "1":
                self.admin_interface.display_doctors()
            elif command == "2":
                self.admin_interface.search_id()
            elif command == "3":
                self.admin_interface.display_speciality()
            elif command == "4":
                self.admin_interface.add_city()
            elif command == "5":
                self.admin_interface.add_speciality()
            elif command == "6":
                self.admin_interface.delete_patient()
            elif command == "7":
                self.admin_interface.delete_doctor()
            elif command == "8":
                self.admin_interface.display_all_patients()
            else:
                print("Invalid choice.")
                continue

    def next_day(self):
        self.admin_interface.next_day()


class DoctorsCommands:
    def __init__(self, doctors_interface):
        self.doctors_interface = doctors_interface

    def entrance(self):
        while True:
            print(CLI.login_menu)
            command = input("Enter your choice (0-2): ")

            if command == "0":
                break
            elif command == "1":
                self.doctors_interface.register_doctor()
            elif command == "2":
                boolean = self.doctors_interface.login()
                if boolean:
                    self.doctor_panel()
                    break
                else:
                    continue
            else:
                print("Invalid choice.")
                continue

    def doctor_panel(self):
        while True:
            print(CLI.doctor_panel)
            command = input("Enter your choice (0-5): ")

            if command == "0":
                self.doctors_interface.save_data()
                break
            elif command == "1":
                self.doctors_interface.view_patient_records()
            elif command == "2":
                self.doctors_interface.set_appointment()
            elif command == "3":
                self.doctors_interface.doctor_cancel_appointment()
            elif command == "4":
                self.doctors_interface.appointments_details()
            elif command == "5":
                self.doctors_interface.canceled_appointments()
            else:
                print("Invalid choice.")
                continue


class PatientsCommands:
    def __init__(self, patients_interface):
        self.patients_interface = patients_interface

    def entrance(self):
        while True:
            print(CLI.login_menu)
            command = input("Enter your choice (0-2): ")

            if command == "0":
                break
            elif command == "1":
                self.patients_interface.register_patient()
            elif command == "2":
                boolean = self.patients_interface.login()
                if boolean:
                    self.patient_panel()
                    break
                else:
                    continue
            else:
                print("Invalid choice.")
                continue

    def patient_panel(self):
        while True:
            print(CLI.patient_panel)
            command = input("Enter your choice (0-6): ")

            if command == "0":
                self.patients_interface.save_data()
                break
            elif command == "1":
                self.patients_interface.display_doctors()
            elif command == "2":
                self.patients_interface.search_name()
            elif command == "3":
                self.patients_interface.make_appointment()
            elif command == "4":
                self.patients_interface.view_appointments_history()
            elif command == "5":
                self.patients_interface.patient_cancel_appointments()
            elif command == "6":
                self.patients_interface.display_canceled_appointments()
            elif command == "7":
                self.patients_interface.auto_reservation()
            else:
                print("Invalid choice.")
                continue


class Start:
    def __init__(self, admin_commands, doctor_commands, patient_commands):
        self.admin_commands = admin_commands
        self.doctor_commands = doctor_commands
        self.patient_commands = patient_commands
        self.day_manager = DayManager()
        self.day_manager.load_day()
        print("Day:", self.day_manager.get_curr_day())

    @staticmethod
    def cls_screen():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def run(self):
        while True:
            print(CLI.main_menu)
            command = int(input("Enter your choice (0-2): "))

            if command == 0:
                self.day_manager.next_day()
                break
            elif command == 1:
                self.admin_commands.admin_panel()
            elif command == 2:
                self.doctor_commands.entrance()
            elif command == 3:
                self.patient_commands.entrance()
            elif command == 4:
                self.day_manager.next_day()
                print("Day:", self.day_manager.get_curr_day())
                self.admin_commands.next_day()
            else:
                print("Invalid choice.")
                continue
