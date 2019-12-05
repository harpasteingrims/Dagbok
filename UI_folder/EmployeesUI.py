#from UI_folder.CabincrewUI import CabincrewUI
#from UI_folder.PilotsUI import PilotsUI

class EmployeesUI():
    LENGTH_STAR = 20
    
    def __init__(self, cabincrew, pilots, llapi):
        # self.__employee_service = LLAPI()
        self.cabincrew = cabincrew
        self.pilots = pilots
        self.llapi = llapi

    def show_employee_menu(self):

        run = True
        while run is True:

            print(self.LENGTH_STAR * "*")
            print("EMPLOYEES MENU \n\n1 Print overview of all employees \n2 Pilots \n3 Cabin Crew \nB Back \n")
            
            action = input("Choose action: ").lower()
            print()

            if action == "1":
                self.show_overview_of_all_employees()

            elif action == "2":
                self.pilots.show_pilot_menu()

            elif action == "3":
                self.cabincrew .show_cabincrew_menu()

            elif action == "b":
                return

    def show_overview_of_all_employees(self):
        print("OVERVIEW OF EMPLOYEES")

        employees = self.llapi.get_employee_overwiew() #Hérna kallar hann í fall í llapanum sem heitir get_employee_overview sem returnar lista yfir alla starfsmenn
        print(employees)
        
        print()
        print("B Back\n")

        action = input("Choose action: ").lower()
        print()

        if action == "b":
            self.show_employee_menu()
