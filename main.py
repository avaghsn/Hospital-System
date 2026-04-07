from data_access.cities import Cities
from data_access.doctors import Doctors
from data_access.patients import Patients
from data_access.specialities import Specialities
from logic.management import Manage
from logic.user_session import UserSession
from presentation.admin_interface import AdminInterface
from presentation.commands import Start, AdminCommands, DoctorsCommands, PatientsCommands
from presentation.doctors_interface import DoctorsInterface
from presentation.patients_interface import PatientsInterface

if __name__ == "__main__":
    # data access layer
    doctors = Doctors()
    patients = Patients()
    specialities = Specialities()
    cities = Cities()

    # logic layer
    manage = Manage(doctors, patients, specialities, cities)
    user_session = UserSession()

    # UI layer
    doctors_interface = DoctorsInterface(manage, user_session)
    patients_interface = PatientsInterface(manage, user_session)
    admin_interface = AdminInterface(manage)

    admin_commands = AdminCommands(admin_interface)
    doctor_commands = DoctorsCommands(doctors_interface)
    patient_commands = PatientsCommands(patients_interface)

    start = Start(admin_commands, doctor_commands, patient_commands)
    start.run()
