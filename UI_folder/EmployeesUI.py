from models.PilotsModel import PilotsModel
from models.CabinCrewModel import CabinCrewModel
import datetime
class EmployeesUI():
    LENGTH_STAR = 20
    CREW = "cabin crew member"
    PILOT = "pilot"
    
    def __init__(self , llapi):
        self.llapi = llapi

    def choose_action(self, valid_list):
        action_str = input("Choose action: ").lower()
        print()
        
        if action_str in valid_list:
            return action_str
            
        else:
            print("Invalid action!")
            return False

    def get_input_number(self, ob_list):
        """ Gets an number from user and checks if it is right """
        
        chosen_number = input("\nChoose a number: ")
        chosen_object = self.llapi.check_chosen_number(chosen_number, ob_list)
        
        if chosen_object:
            return chosen_object

        else:
            print("\nInvalid input!")
            self.get_input_number(ob_list)

    def show_employee_menu(self):
        """This prints the employee menu"""
    
        action_str = ""

        while True:
            print(self.LENGTH_STAR * "*")
            print("EMPLOYEES MENU\n")
            print("1 Print overview of all employees")
            print("2 Pilots")
            print("3 Cabin Crew")
            print("B Back\n")

            action_str = self.choose_action(["1", "2" ,"3" ,"b"])
            while action_str == False:
                action_str = self.choose_action(["1", "2", "3", "b"])

            if action_str == "1":
                self.show_overview_of_all_employees()

            elif action_str == "2":
                self.show_pilot_or_crew_menu(self.PILOT)

            elif action_str == "3":
                self.show_pilot_or_crew_menu(self.CREW)

            elif action_str == "b":
                return

    def show_pilot_or_crew_menu(self, staff_str):
        """ Prints either the menu and calls appropriate functions or prints Invalid action"""

        while True:
            print(self.LENGTH_STAR * "*")
            print(f"{staff_str.upper()} MENU\n")
            
            print(f"1 Print overview of {staff_str}s")
            print(f"2 Search for a {staff_str}")
            print(f"3 Create a new {staff_str}")
            print("B Back\n")

            action_str = self.choose_action(["1", "2", "3", "b"])
            while action_str == False:
                action_str = self.choose_action(["1", "2", "3", "b"])
        
            if action_str == "1":
                self.show_either_crew_or_pilots_overview(staff_str)

            elif action_str == "2": 
                self.show_enter_name_to_search(staff_str)

            elif action_str == "3" and staff_str == self.PILOT: 
                self.show_create_form(staff_str)
            
            elif action_str == "3" and staff_str == self.CREW:
                self.show_create_form(staff_str)

            elif action_str == "b":
                return

    def show_overview_of_all_employees(self):
        """This prints the overview of all employees"""

        print("OVERVIEW OF EMPLOYEES\n")

        employees_ob_list = self.llapi.get_employee_overview() #Hérna kallar hann í fall í llapanum sem heitir get_employee_overview sem returnar lista yfir alla starfsmenn
        
        for employee_ob in employees_ob_list:
            print(employee_ob.print_info_in_line("*"))
                
        print(f"\nNAN AIR has {len(employees_ob_list)} employees")

        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        while action_str == False:
            action_str = self.choose_action(["b"])

        if action_str == "b":
            return 

    def show_either_crew_or_pilots_overview(self, staff_str):
        """ Prints the overview of either """
        
        print(self.LENGTH_STAR * "*")
        print(f"OVERVIEW OF {staff_str.upper()}S\n")
        
        if staff_str == self.PILOT:
            staff_ob_list = self.llapi.get_pilot_overview() # Calls the class that makes a list of all pilots and prints it
        
        elif staff_str == self.CREW:
            staff_ob_list = self.llapi.get_cabin_crew_overview()

        for staff_ob in staff_ob_list:
            print(staff_ob.print_info_in_line("*"))
        
        print(f"\nNAN AIR has {len(staff_ob_list)} {staff_str}s")
        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        while action_str == False:
            action_str = self.choose_action(["b"])
        
        if action_str == "b":
            return

    def get_input_name_and_common_name_list(self, staff_str):
        
        input_name = input(f"Enter name of {staff_str}: ").lower() 
        print()   

        if staff_str == self.PILOT:
            common_named_staff_list = self.llapi.get_common_named_pilots(input_name)

        elif staff_str == self.CREW:
            common_named_staff_list = self.llapi.get_common_named_crew_members(input_name)

        else: 
            return False

        return common_named_staff_list, input_name


    def show_enter_name_to_search(self, staff_str):
        """ This prints the search for a pilot window """
         
        print(self.LENGTH_STAR * "*")
        print(f"SEARCH FOR A {staff_str.upper()}\n")
        
        print("B Back \nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
            action_str = self.choose_action(["b", "c"])
        
        if action_str == "b":
            return

        elif action_str == "c":
        
            common_named_staff_list, input_name = self.get_input_name_and_common_name_list(staff_str)
            
            while common_named_staff_list == False:
                print(f"{staff_str} does not exist!\n")
                common_named_staff_list, input_name = self.get_input_name_and_common_name_list(staff_str)
            
            if len(common_named_staff_list) == 1:
                staff_ob = common_named_staff_list[0]
    
            else: 
                counter = 1
                for staff_ob in common_named_staff_list:

                    print(staff_ob.print_info_in_line(counter))
                    counter += 1
                
                staff_ob = self.get_input_number(common_named_staff_list)

            print()
            print(self.LENGTH_STAR * "*")
            print(f"{staff_ob.name.upper()}'S INFO\n")
            print(staff_ob.print_info_new_line())
    
            print(f"\n1 {staff_ob.name}'s flight schedule")
            print(f"2 Edit {staff_ob.name}'s address")
            print(f"3 Edit {staff_ob.name}'s mobile number")
            print(f"4 Edit {staff_ob.name}'s email")
            print("B Back\n")

            action_str = self.choose_action(["1","2","3","4","b"])
            while action_str == False:
                action_str = self.choose_action(["1", "2", "3", "4" "b"])
            
            if action_str == "1":
                self.show_flight_schedule_of_employee(staff_ob)

            elif action_str == "2": 
                self.show_employee_edit_form(staff_ob, 1)
            
            elif action_str == "3": 
                self.show_employee_edit_form(staff_ob, 2)

            elif action_str == "4": 
                self.show_employee_edit_form(staff_ob, 3)

            elif action_str == "b":
                return

    def show_flight_schedule_of_employee(self, staff_ob):
        """Calls a class that makes a list of their voyages and prints it"""
        print("Continue to pick dates")
        print("\nB Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
            action_str = self.choose_action(["b", "c"])
        if action_str == "b":
            return

        elif action_str == "c":
           
            valid_interval = False
            while valid_interval != True:
                date_from = self.get_date_from()
                while date_from == False:
                    date_from = self.get_date_from()
                date_to = self.get_date_to()
                while date_to == False:
                    date_to = self.get_date_to()
                valid_interval = self.get_valid_interval(date_from, date_to)

            flights_on_asked_time = self.llapi.get_employee_schedule_by_date(staff_ob, date_from, date_to)
            
            counter = 1
            if len(flights_on_asked_time) < 1:
                print(f"\n{staff_ob.name} has no flights on selected period")

            else:
                print(self.LENGTH_STAR * "*")
                print(f"{staff_ob.name.upper()}'S FLIGHT SCHEDULE")
                
                for flight_ob in flights_on_asked_time:
                    
                    print(flight_ob.print_schedule(counter))
                    counter += 1

            print("\nB Back\n")

            action_str = self.choose_action(["b"])
            while action_str == False:
                action_str = self.choose_action(["b"])

            if action_str == "b":
                return

    def show_employee_edit_form(self, staff_ob, number):
        """This prints the edit form for an employee"""

        print(self.LENGTH_STAR * "*")
        print(f"EDIT {staff_ob.role.upper()}\n")

        print("B Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
            action_str = self.choose_action(["b", "c"])
        if action_str == "b":
            return
        elif action_str == "c":

            if number == 1:
                print(self.LENGTH_STAR * "*")
                print(f"You are changing {staff_ob.name}´s address\nThe current address is: {staff_ob.address}")
                new_address = self.get_address()
                while new_address == False:
                    new_address = self.get_address()
                success = self.check_action_edit_form(staff_ob, number, new_address)

            elif number == 2:
                print(self.LENGTH_STAR * "*")
                print(f"You are changing {staff_ob.name}´s mobile number\nThe current mobile number is: {staff_ob.mobile_number}")
                new_mobile_number = self.get_mobile_number()
                while new_mobile_number == False:
                    new_mobile_number = self.get_mobile_number
                success = self.check_action_edit_form(staff_ob, number, new_mobile_number)
            
            elif number == 3:
                print(self.LENGTH_STAR * "*")
                print(f"You are changing {staff_ob.name}´s email\nThe current the email is: {staff_ob.email}")
                new_email = self.get_email()
                while new_email == False:
                    new_email = self.get_email()
                success = self.check_action_edit_form(staff_ob, number, new_email)
        
        print(f"{staff_ob.name}'s information successfully changed")
        
        return

    def check_action_edit_form(self, staff_ob, number, new_info):
        
        print("\nS Save \nB Back\n")
        action_str = self.choose_action(["s","b"])
        while action_str == False:
            action_str = self.choose_action(["s", "b"])

        if action_str == "s" and number == 1:

            if staff_ob.role == self.PILOT.capitalize():
                updated_staff_ob = PilotsModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.license_type, new_info, staff_ob.mobile_number, staff_ob.email)
            else:
                updated_staff_ob = CabinCrewModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, new_info, staff_ob.mobile_number, staff_ob.email)
            
        elif action_str == "s" and number == 2:

            if staff_ob.role == self.PILOT.capitalize():
                updated_staff_ob = PilotsModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.license_type, staff_ob.address, new_info, staff_ob.email)
            else:
                updated_staff_ob = CabinCrewModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.address, new_info, staff_ob.email)
        
        elif action_str == "s" and number == 3:

            if staff_ob.role == self.PILOT.capitalize():
                updated_staff_ob = PilotsModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.license_type, staff_ob.address, staff_ob.mobile_number, new_info)
            else:
                updated_staff_ob = CabinCrewModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.address, staff_ob.mobile_number, new_info)
        
        elif action_str == "b":
            return


        if updated_staff_ob.role == self.PILOT.capitalize():

            return self.llapi.update_new_pilot_information(updated_staff_ob)

        else:
            return self.llapi.update_new_crew_member_information(updated_staff_ob)
        

    def show_create_form(self, staff_str):
        """ This prints the create a pilot form """

        print(self.LENGTH_STAR * "*")
        print(f"CREATE A NEW {staff_str.upper()}\n")
        
        print("B Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
            action_str = self.choose_action(["b", "c"])
        if action_str == "b":
            return
        elif action_str == "c":
            name = self.get_name()
            while name == False:
                name = self.get_name()
            ssn = self.get_ssn()
            while ssn == False:
                ssn = self.get_ssn()
            address = self.get_address()
            while address == False:
                address = self.get_address()
            mobile_number = self.get_mobile_number()
            while mobile_number == False:
                mobile_number = self.get_mobile_number()
            email = self.get_email()
            while email == False:
                email = self.get_email()
            
            if staff_str == self.PILOT:
                rank = self.get_pilot_rank()
                while rank == False:
                    rank = self.get_pilot_rank()
                license_type = self.get_license_type()
                while license_type == False:
                    license_type = self.get_license_type()

            else:
                rank = self.get_cabin_crew_rank()
                while rank == False:
                    rank = self.get_cabin_crew_rank()

            print("\nS Save \nB Back\n")

            action_str = self.choose_action(["s","b"])
            while action_str == False:
                action_str = self.choose_action(["s", "b"])

            if action_str == "s":
                if staff_str == self.PILOT:

                    new_staff_object = PilotsModel(ssn, name, "Pilot", rank, license_type, address, mobile_number, email)
                    self.llapi.create_new_pilot(new_staff_object)

                elif staff_str == self.CREW:
                    new_staff_object = CabinCrewModel(ssn, name, "Cabin crew", rank, address, mobile_number, email)
                    self.llapi.create_new_cabin_crew(new_staff_object)

                print(f"{staff_str.capitalize()} {new_staff_object.name} successfully created\n")
                return
            
            elif action_str == "b":
                return
        
        
    def get_date_from(self):
        print(self.LENGTH_STAR * "*")
        print("Enter date from\n")
        year_from = input("Enter year (yyyy): ")
        month_from = input("Enter month (mm): ")
        day_from = input("Enter day (dd): ")
        date = [year_from, month_from, day_from, "00", "00", "00"]

        date_check = self.llapi.check_dates(date)

        if date_check:
            return date_check
        else:
            print("\nInvalid date\n")
            return date_check

    def get_date_to(self):
        print(self.LENGTH_STAR * "*")
        print("Enter date to\n")
        year_to = input("Enter year (yyyy): ")
        month_to = input("Enter month (mm): ")
        day_to = input("Enter day (dd): ")
        date = [year_to, month_to, day_to, "23", "59", "00"]

        date_check = self.llapi.check_dates(date)

        if date_check:
            return date_check
        else:
            print("\nInvalid date\n")
            return date_check

    def get_valid_interval(self, date_from, date_to):
        valid_check = self.llapi.check_date_interval(date_from, date_to)
        if valid_check == True:
            return valid_check
        else:
            print("\nInvalid interval\n")
            return valid_check

    def get_name(self):
        name = input("Enter full name: ").lower()
        name_check = self.llapi.check_name(name)
        
        if name_check:
            return name_check
            
        else:
            print("\nInvalid name")
            return name_check


    def get_pilot_rank(self):
        rank = input("\nEnter number for either \n1 Captain \n2 Copilot\nEnter: ")
        rank_check = self.llapi.check_pilot_rank(rank)
        
        if rank_check:
            return rank_check
        
        else:
            print("\nInvalid rank\n")
            return rank_check

    def get_cabin_crew_rank(self):
        rank = input("\nEnter number for either \n1 Flight Service Manager \n2 Flight Attendant\nEnter: ")
        rank_check = self.llapi.check_crew_member_rank(rank)

        if rank_check:
            return rank_check
        
        else:
            print("\nInvalid rank")
            return rank_check

    def get_ssn(self):
        ssn = input("\nEnter social security number: ")
        ssn_check = self.llapi.check_ssn(ssn)

        if ssn_check:
            return ssn_check
        
        else:
            print("\nInvalid SSN")
            return ssn_check

    def get_address(self):
        address = input("\nEnter address in form \n(address name) (house number), (zip code)\n: ").replace(",", "").split()
        address_check = self.llapi.check_address(address)

        if address_check:
            return address_check
        
        else:
            print("\nInvalid address")
            return address_check


    def get_mobile_number(self):
        mobile_number = input("\nEnter mobile number: ")
        mobile_number_check = self.llapi.check_mobile_number(mobile_number)

        if mobile_number_check:
            return mobile_number_check
        
        else:
            print("\nInvalid mobile_number")
            return mobile_number_check
    

    def get_email(self):
        email = input("\nEnter email: ")
        email_check = self.llapi.check_email(email)

        if email_check:
            return email_check
        
        else:
            print("\nInvalid email")
            return email_check

    def get_license_type(self):
        print("\nOverview of license types:")
        airplane_list = self.llapi.get_airplanes_for_UI()
        
        counter = 1
        for airplane_type in airplane_list:
            print(f"\n{counter} {airplane_type}")
            counter += 1

        license_type_num = input("\nEnter a number to choose the license type: ")
        license_type_check = self.llapi.check_license_type(license_type_num, airplane_list)
    
        if license_type_check:
            return license_type_check
        
        else:
            print("\nInvalid license_type")
            return license_type_check