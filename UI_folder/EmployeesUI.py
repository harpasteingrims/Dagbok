#from UI_folder.CabincrewUI import CabincrewUI
#from UI_folder.PilotsUI import PilotsUI

class EmployeesUI():
    LENGTH_STAR = 20
    
    def __init__(self, cabincrew, pilots, llapi):
        self.cabincrew = cabincrew
        self.pilots = pilots
        self.llapi = llapi

    def show_employee_menu(self):
        """This prints the employee menu"""

        run = True
        while run is True:

            action = ""
            while(action != "q"):
                print(self.LENGTH_STAR * "*")
                print("EMPLOYEES MENU")
                print("1 Print overview of all employees")
                print("2 Pilots")
                print("3 Cabin Crew")
                print("B Back")
                print("Q Quit")
                action_str = input("Choose action: ").lower()
                print()

                if action_str == "1":
                    self.show_overview_of_all_employees()

                elif action_str == "2":
                    self.pilots.show_pilot_menu()

                elif action_str == "3":
                    self.cabincrew .show_cabincrew_menu()

                elif action_str == "b":
                    return

    def show_overview_of_all_employees(self):
        """This prints the overview of all employees"""

        print("OVERVIEW OF EMPLOYEES")

        employees = self.llapi.get_employee_overwiew() #Hérna kallar hann í fall í llapanum sem heitir get_employee_overview sem returnar lista yfir alla starfsmenn
        print(employees)
        
        print()
        print("B Back\n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "b":
            self.show_employee_menu()
