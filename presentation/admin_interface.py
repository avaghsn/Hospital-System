class AdminInterface:
    def __init__(self, manage):
        self.manage = manage

    def display_doctors(self):  # phase 1
        result = self.manage.admin_display_doctors()
        while not result.is_empty():
            print(result.dequeue())

    def search_id(self):  # phase 1
        dr_id = input("enter national id: ")
        result = self.manage.admin_search_id(dr_id)
        if result is not None:
            print(result)
        else:
            print(f"Not found doctor with {dr_id} id.")

    def display_speciality(self):  # phase 1
        speciality = input("enter speciality: ")
        result = self.manage.admin_display_speciality(speciality)
        if result.dequeue() is None:
            print(f"Not found doctor in {speciality} field.")
        while not result.is_empty():
            print(result.dequeue())

    def add_city(self):  # phase 1
        name = input("city name: ")
        boolean = self.manage.admin_add_city(name)
        if boolean:
            print("city added.")
        else:
            print("duplicate city.")

    def add_speciality(self):  # phase 1
        name = input("speciality name: ")
        boolean = self.manage.admin_add_speciality(name)
        if boolean is True:
            print("Speciality added.")
        if boolean is False:
            print("Duplicate speciality.")

    def delete_patient(self):  # phase 2
        national_id = input("enter patient national id: ").strip()
        result = self.manage.delete_patient(national_id)
        if result:
            print("Patient has been deleted.")
        else:
            print("Patient does not exist.")

    def delete_doctor(self):  # phase 2
        print()
        print("1) -Delete by national ID")
        print("2) -Delete by medical number")
        print()

        command = input(">>> ")
        if command == "1":
            national_id = input("enter national id: ").strip()
            result = self.manage.delete_doctor_id(national_id)
            if result:
                print("Doctor has been deleted.")
            else:
                print("Doctor does not exist.")

        elif command == "2":
            national_id = input("enter medical number: ").strip()
            result = self.manage.delete_doctor_med_num(national_id)
            if result:
                print("Doctor has been deleted.")
            else:
                print("Doctor does not exist.")

    def display_all_patients(self):  # phase 2
        print("*********** List of Registered Patients ***********")
        patients = self.manage.display_all_patients()
        for ids in patients:
            print(patients[ids])

    def save_data(self):
        self.manage.save_data()

    def next_day(self):
        self.manage.next_day()
