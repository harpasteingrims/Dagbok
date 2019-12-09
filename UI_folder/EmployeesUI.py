from UI_folder.CabincrewUI import CabincrewUI
from UI_folder.PilotsUI import PilotsUI
class EmployeesUI():
    LENGTH_STAR = 20
    
    def __init__(self , llapi, employees = None):
        self.llapi = llapi
        self.employees = employees
        self.cabincrew = CabincrewUI(llapi, employees)
        self.pilots = PilotsUI(llapi, employees)
        
    def choose_action(self):
        action_str = input("Choose action: ").lower()
        print()
        return action_str

    def show_employee_menu(self):
        """This prints the employee menu"""
    
        action_str = ""

        while True:
    
            print(self.LENGTH_STAR * "*")
            print("\nEMPLOYEES MENU\n")
            print("1 Print overview of all employees")
            print("2 Pilots")
            print("3 Cabin Crew")
            print("B Back\n")

            action_str = self.choose_action()

            if action_str == "1":
                self.show_overview_of_all_employees()

            elif action_str == "2":
                self.pilots.show_pilot_menu()

            elif action_str == "3":
                self.cabincrew .show_cabincrew_menu()

            elif action_str == "b":
                return

            else:
                print("Invalid action!\n")

    def show_overview_of_all_employees(self):
        """This prints the overview of all employees"""

        print("OVERVIEW OF EMPLOYEES\n")

        employees_ob_list = self.llapi.get_employee_overview() #Hérna kallar hann í fall í llapanum sem heitir get_employee_overview sem returnar lista yfir alla starfsmenn
        
        counter = 1
        for employee in employees_ob_list:
            if employee.role == "Cabin crew":

                print(employee.print_crew_member_info_in_line(counter))

            else:
                print(employee.print_pilot_info_in_line(counter))
            counter += 1
        
        print("\nB Back\n")

        action_str = self.choose_action()

        if action_str == "b":
            return 
        else:
            print("Invalid action!")
            action_str = self.choose_action()


    def get_name(self):
        name = input("\nEnter full name: ").lower()
        name_check = self.llapi.check_name(name)
        
        if name_check:
            return name_check
            
        else:
            print("\nInvalid name\n")
            self.get_name()


    def get_pilot_rank(self):

        rank = input("\nEnter number for either \n1 Captain \n2 Copilot\n: ")
        
        rank_check = self.llapi.check_pilot_rank(rank)
        
        if rank_check:
            return rank_check
        
        else:
            print("\nInvalid rank\n")
            self.get_pilot_rank()
    
    def get_cabin_crew_rank(self):
        rank = input("\nEnter number for either \n1 Flight Service Manager \n2 Flight Attendant\n: ")
        
        rank_check = self.llapi.check_crew_member_rank(rank)

        if rank_check:
            return rank_check
        
        else:
            print("\nInvalid rank")
            self.get_cabin_crew_rank()
        

    def get_ssn(self):
        ssn = input("\nEnter social security number: ")
        ssn_check = self.llapi.check_ssn(ssn)

        if ssn_check:
            return ssn_check
        
        else:
            print("\nInvalid SSN")
            self.get_ssn()
    

    def get_address(self):
        address = input("\nEnter address in form \nzip code address name house number\n: ")
            
        address_check = self.llapi.check_address(address).lower()

        if address_check:
            return address_check
        
        else:
            print("\nInvalid address")
            self.get_address()


    def get_mobile_number(self):
        mobile_number = input("\nEnter mobile number: ")
        mobile_number_check = self.llapi.check_mobile_number(mobile_number)

        if mobile_number_check:
            return mobile_number_check
        
        else:
            print("\nInvalid mobile_number")
            self.get_mobile_number()
    

    def get_email(self):
        email = input("\nEnter email: ")
        email_check = self.llapi.check_email(email).lower()

        if email_check:
            return email_check.capitalize()
        
        else:
            print("\nInvalid email")
            self.get_email()


    def get_license_type(self):


        license_type = input("\nEnter license type: ").lower()
        
        airplane_object_list = self.llapi.get_airplanes_overview()


        license_type_check = self.llapi.check_license_type(license_type)



        if license_type_check:
            return license_type_check.capitalize()
        
        else:
            print("\nInvalid license_type")
            self.get_license_type()