from UI_folder.CabincrewUI import CabincrewUI
from UI_folder.PilotsUI import PilotsUI
import datetime
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
            print("EMPLOYEES MENU\n")
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
        
        for employee in employees_ob_list:
            if employee.role == "Cabin crew":

                print(employee.to_csv_string())

            else:
                print(employee.to_csv_string())
        
        print("\nB Back\n")

        action_str = self.choose_action()

        if action_str == "b":
            return 
        else:
            print("Invalid action!")
            action_str = self.choose_action()

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


    def show_flight_schedule_of_employee(self, employee_ob):
        """Calls a class that makes a list of their voyages and prints it"""

        date_from = self.get_date_from()
        date_to = self.get_date_to()

        flights_on_asked_time = self.llapi.get_employee_schedule_by_date(employee_ob, date_from, date_to)
        
        counter = 1
        if len(flights_on_asked_time) < 1:
            print(f"{employee_ob.name} has no flights on selected period")

        else:
            print(self.LENGTH_STAR * "*")
            print(f"{employee_ob.name.upper()}'S FLIGHT SCHEDULE")
            
            for flight_ob in flights_on_asked_time:
                
                print(flight_ob.print_schedule(counter))
                counter += 1

        print("\nB Back\n")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("\nInvalid action!")
            action_str = self.choose_action()


    def get_name(self):
        print(self.LENGTH_STAR * "*")
        name = input("Enter full name: ").lower()
        print()
        name_check = self.llapi.check_name(name)
        
        if name_check:
            return name_check
            
        else:
            print("\nInvalid name\n")
            self.get_name()


    def get_pilot_rank(self):
        print(self.LENGTH_STAR * "*")
        rank = input("Enter number for either \n1 Captain \n2 Copilot\n: ")
        print()

        rank_check = self.llapi.check_pilot_rank(rank)
        
        if rank_check:
            return rank_check
        
        else:
            print("\nInvalid rank\n")
            self.get_pilot_rank()
    
    def get_cabin_crew_rank(self):
        print(self.LENGTH_STAR * "*")
        rank = input("Enter number for either \n1 Flight Service Manager \n2 Flight Attendant\n: ")
        print()

        rank_check = self.llapi.check_crew_member_rank(rank)

        if rank_check:
            return rank_check
        
        else:
            print("\nInvalid rank")
            self.get_cabin_crew_rank()
        

    def get_ssn(self):
        print(self.LENGTH_STAR * "*")
        ssn = input("Enter social security number: ")
        print()

        ssn_check = self.llapi.check_ssn(ssn)

        if ssn_check:
            return ssn_check
        
        else:
            print("\nInvalid SSN")
            self.get_ssn()
    

    def get_address(self):
        print(self.LENGTH_STAR * "*")
        address = input("Enter address in form \n{address name} {house number}, {zip code} \n: ").replace(",", "").split()
        print()

        address_check = self.llapi.check_address(address)

        if address_check:
            return address_check
        
        else:
            print("\nInvalid address")
            self.get_address()


    def get_mobile_number(self):
        print(self.LENGTH_STAR * "*")
        mobile_number = input("Enter mobile number: ")
        print()

        mobile_number_check = self.llapi.check_mobile_number(mobile_number)

        if mobile_number_check:
            return mobile_number_check
        
        else:
            print("\nInvalid mobile_number")
            self.get_mobile_number()
    

    def get_email(self):
        print(self.LENGTH_STAR * "*")
        email = input("Enter email: ")
        print()
        email_check = self.llapi.check_email(email).lower()

        if email_check:
            return email_check.capitalize()
        
        else:
            print("\nInvalid email")
            self.get_email()


    def get_license_type(self):
        print(self.LENGTH_STAR * "*")
        print("Overview of license types:")
        
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