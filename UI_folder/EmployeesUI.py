from UI_folder.CabincrewUI import CabincrewUI
from UI_folder.PilotsUI import PilotsUI
class EmployeesUI():
    LENGTH_STAR = 20
    
    def __init__(self , llapi):
        self.llapi = llapi
        self.cabincrew = CabincrewUI(llapi)
        self.pilots = PilotsUI(llapi)
        
    def choose_action(self):
        action_str = input("Choose action: ").lower()
        print()
        return action_str

    def show_employee_menu(self):
        """This prints the employee menu"""
    
        action_str = ""

        while True:
            print()
            print(self.LENGTH_STAR * "*")
            print("EMPLOYEES MENU")
            print()
            print("1 Print overview of all employees")
            print("2 Pilots")
            print("3 Cabin Crew")
            print("B Back")
            print()

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
                print("Invalid action!")
                print()

    def show_overview_of_all_employees(self):
        """This prints the overview of all employees"""

        print("OVERVIEW OF EMPLOYEES")

        employees_ob_list = self.llapi.get_employee_overview() #Hérna kallar hann í fall í llapanum sem heitir get_employee_overview sem returnar lista yfir alla starfsmenn
        for employee in employees_ob_list:
            print(f"{employee.name}, {employee.role}, {employee.ssn}, {employee.mobile_number}, {employee.email}")
        
        print()
        print("B Back\n")

        action_str = self.choose_action()

        if action_str == "b":
            self.show_employee_menu()
        else:
            print("Invalid action!")
            action_str = self.choose_action()
