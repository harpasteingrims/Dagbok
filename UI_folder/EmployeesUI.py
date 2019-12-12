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
            self.choose_action(valid_list)

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

            action_str = self.choose_action(["1","2","3","b"])

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
            
            print(f"1 Print overview of {staff_str}")
            print(f"2 Search for a {staff_str}")
            print(f"3 Create a new {staff_str}")
            print("B Back\n")

            action_str = self.choose_action(["1","2","3","b"])
        
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
        
        print("\nB Back\n")

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
            print(staff_ob.print_info_in_line())
        
        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        
        if action_str == "b":
            return


    def get_input_name_and_common_name_list(self, staff_str):
        
        input_name = input(f"Enter name of {staff_str}: ").lower()

        if staff_str == self.PILOT:
            common_named_staff_list = self.llapi.get_common_named_pilots(input_name)

        elif staff_str == self.CREW:
            common_named_staff_list = self.llapi.get_common_named_crew_members(input_name)

        return common_named_staff_list, input_name


    def show_enter_name_to_search(self, staff_str):
        """ This prints the search for a pilot window """
         
        print(self.LENGTH_STAR * "*")
        print(f"SEARCH FOR A {staff_str.upper()}\n")
        
        while True:
        
            common_named_staff_list, input_name = self.get_input_name_and_common_name_list(staff_str)
            
            while common_named_staff_list == False:
                print(f"{staff_str} does not exist!\n")
                common_named_staff_list, input_name = self.get_input_name_and_common_name_list(staff_str)
            
            if len(common_named_staff_list) == 1:
                staff_ob = common_named_staff_list[0]
                print()

            else: 
                counter = 1
                for staff_ob in common_named_staff_list:

                    print(staff_ob.print_info_in_line())
                    counter += 1
                staff_ob = self.get_input_number(common_named_staff_list)

        
            print()
            print(self.LENGTH_STAR * "*")
            print(f"{staff_ob.name.upper()}'S INFO\n")
            print(staff_ob.print_info_in_line())
    
            print(f"\n1 {staff_ob.name}'s flight schedule")
            print(f"2 Edit {staff_ob.name} address")
            print(f"3 Edit {staff_ob.name} mobile number")
            print(f"4 Edit {staff_ob.name} email")
            print("B Back\n")

            action_str = self.choose_action(["1","2","3","4","b"])
            
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
        print("Pick continue to pick dates")
        print("\nB Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        if action_str == "b":
            return

        date_from = self.get_date_from()
        date_to = self.get_date_to()

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

        if action_str == "b":
            return
        

    def show_employee_edit_form(self, staff_ob, number):
        """This prints the edit form for an employee"""

        print(self.LENGTH_STAR * "*")
        print(f"EDIT {staff_ob.role.upper()}\n")

        print("\nB Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        if action_str == "b":
            return
        
        if number == 1:
            print(self.LENGTH_STAR * "*")
            print(f"You are changing {staff_ob.name}´s address\nNow the address is: {staff_ob.address}")
            new_address = self.get_address()
            success = self.check_action_edit_form(staff_ob, number, new_address)

        elif number == 2:
            print(self.LENGTH_STAR * "*")
            print(f"You are changing {staff_ob.name}´s mobile number\nNow the mobile number is: {staff_ob.mobile_number}")
            new_mobile_number = self.get_mobile_number()
            success = self.check_action_edit_form(staff_ob, number, new_mobile_number)
        
        elif number == 3:
            print(self.LENGTH_STAR * "*")
            print(f"You are changing {staff_ob.name}´s email\nNow the email is: {staff_ob.email}")
            new_email = self.get_email()
            success = self.check_action_edit_form(staff_ob, number, new_email)
    
        if succsess:
            print(f"{staff_ob.name}'s information successfully changed")
            return


    def check_action_edit_form(self,staff_ob, number, new_address= "", new_mobile_number= "", new_email = ""):
        
        print("\nS Save \nB Back\n")
        action_str = self.choose_action(["s","b"])

        if action_str == "s" and number == 1:

            if staff_ob.role == self.PILOT:
                updated_staff_ob = PilotsModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.license_type, new_address, staff_ob.mobile_number, staff_ob.email)
            else:
                updated_staff_ob = CabinCrewModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, new_address, staff_ob.mobile_number, staff_ob.email)
            
        elif action_str == "s" and number == 2:

            if staff_ob.role == self.PILOT:
                updated_staff_ob = PilotsModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.license_type, staff_ob.address, new_mobile_number, staff_ob.email)
            else:
                updated_staff_ob = CabinCrewModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.address, new_mobile_number, staff_ob.email)
        
        elif action_str == "s" and number == 3:

            if staff_ob.role == self.PILOT:
                updated_staff_ob = PilotsModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.license_type, staff_ob.address, staff_ob.mobile_number, new_email)
            else:
                updated_staff_ob = CabinCrewModel(staff_ob.ssn, staff_ob.name, staff_ob.role, staff_ob.rank, staff_ob.address, staff_ob.mobile_number, new_email)
        
        elif action_str == "b":
            return


        if updated_staff_ob.role == self.PILOT:

            return self.llapi.update_new_pilot_information(updated_staff_ob)

        else:
            return self.llapi.update_new_crew_member_information(updated_staff_ob)
        

    def show_create_form(self, staff_str):
        """ This prints the create a pilot form """

        print(self.LENGTH_STAR * "*")
        print(f"CREATE A NEW {staff_str}\n")
        
        print("\nB Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        if action_str == "b":
            return

        name = self.get_name()
        ssn = self.get_ssn()
        address = self.get_address()
        mobile_number = self.get_mobile_number()
        email = self.get_email()
        
        if staff_str == self.PILOT:
            rank = self.get_pilot_rank()
            license_type = self.get_license_type()

        else:
            rank = self.get_cabin_crew_rank()

        print("\nS Save \nB Back\n")

        action_str = self.choose_action(["s","b"])

        if action_str == "s":
            if staff_str == self.PILOT:

                new_staff_object = PilotsModel(ssn, name, "Pilot", rank, license_type, address, mobile_number, email)
                self.llapi.create_new_pilot(new_staff_object)

            elif staff_str == self.CREW:
                new_staff_object = CabinCrewModel(ssn, name, "Cabin crew", rank, address, mobile_number, email)
                self.llapi.create_new_cabin_crew(new_staff_object)

            print(f"{staff_str} {new_staff_object.name} successfully created\n")
            return
         
        elif action_str == "b":
            return
        
    def get_date_from(self):
        print(self.LENGTH_STAR * "*")
        print("Enter date from\n")

        
        try:
            day_from = int(input("Enter day from: "))
            month_from = int(input("Enter month from: "))
            year_from = int(input("Enter year from: "))
        
            date_from = datetime.datetime(year_from, month_from, day_from, 0, 0, 0).isoformat()
            return date_from

        except ValueError:
            print("Invalid input, try again\n")
            self.get_date_from()

    def get_date_to(self):
        print(self.LENGTH_STAR * "*")
        print("Enter date to\n")
        try:
            day_to = int(input("Enter day to: "))
            month_to = int(input("Enter month to: "))
            year_to = int(input("Enter year to: "))

            date_to = datetime.datetime(year_to, month_to, day_to, 23, 59, 0).isoformat()
            return date_to

        except ValueError:
            print("Invalid input, try again\n")
            self.get_date_to()


    def get_name(self):
        
        name = input("\nEnter full name: ").lower()
        print()
        name_check = self.llapi.check_name(name)
        
        if name_check:
            return name_check
            
        else:
            print("\nInvalid name\n")
            self.get_name()


    def get_pilot_rank(self):
        
        rank = input("\nEnter number for either \n1 Captain \n2 Copilot\n: ")
        print()

        rank_check = self.llapi.check_pilot_rank(rank)
        
        if rank_check:
            return rank_check
        
        else:
            print("\nInvalid rank\n")
            self.get_pilot_rank()
    
    def get_cabin_crew_rank(self):

        rank = input("\nEnter number for either \n1 Flight Service Manager \n2 Flight Attendant\n: ")
        print()

        rank_check = self.llapi.check_crew_member_rank(rank)

        if rank_check:
            return rank_check
        
        else:
            print("\nInvalid rank")
            self.get_cabin_crew_rank()
        

    def get_ssn(self):
        
        ssn = input("\nEnter social security number: ")
        print()

        ssn_check = self.llapi.check_ssn(ssn)

        if ssn_check:
            return ssn_check
        
        else:
            print("\nInvalid SSN")
            self.get_ssn()
    

    def get_address(self):
        
        address = input("\nEnter address in form \n{address name} {house number}, {zip code} \n: ").replace(",", "").split()
        print()

        address_check = self.llapi.check_address(address)

        if address_check:
            return address_check
        
        else:
            print("\nInvalid address")
            self.get_address()


    def get_mobile_number(self):
        
        mobile_number = input("\nEnter mobile number: ")
        print()

        mobile_number_check = self.llapi.check_mobile_number(mobile_number)

        if mobile_number_check:
            return mobile_number_check
        
        else:
            print("\nInvalid mobile_number")
            self.get_mobile_number()
    

    def get_email(self):
        email = input("Enter email: ")
        print()
        email_check = self.llapi.check_email(email).lower()

        if email_check:
            return email_check.capitalize()
        
        else:
            print("\nInvalid email")
            self.get_email()


    def get_license_type(self):
        
        print("nOverview of license types:")
        
        airplane_list = self.llapi.get_airplanes_for_UI()
        
        counter = 1
        for airplane_type in airplane_list:
            print(f"{counter} {airplane_type}")
            
            counter += 1

        license_type_num = input("\nEnter a number to choose the license type: ")
        print()
        license_type_check = self.llapi.check_license_type(license_type_num, airplane_list)
    
        if license_type_check:
            return license_type_check.capitalize()
        
        else:
            print("\nInvalid license_type")
            self.get_license_type()