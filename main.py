from Final.data_access.patients import Patients
from Final.data_access.doctors import Doctors
from Final.data_access.cities import Cities
from Final.data_access.specialities import Specialities

from Final.logic.management import Manage
from Final.logic.user_session import UserSession

from Final.presentation.doctors_interface import DoctorsInterface
from Final.presentation.patients_interface import PatientsInterface
from Final.presentation.admin_interface import AdminInterface

from Final.presentation.commands import Start, AdminCommands, DoctorsCommands, PatientsCommands


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
