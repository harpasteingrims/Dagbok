from UI_folder.CabincrewUI import CabincrewUI
from UI_folder.PilotsUI import PilotsUI
from UI_folder.UIAPI import UIAPI
class EmployeesUI():
    LENGTH_STAR = 20
    
    def __init__(self):
        # self.__employee_service = LLAPI()
        pass

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
                PilotsUI.show_pilot_menu(self)

            elif action == "3":
                CabincrewUI.show_cabin_crew_menu(self)

            elif action == "b":
                return

    def show_overview_of_all_employees(self):
        print("OVERVIEW OF EMPLOYEES")

        # calls the method that makes a list of all emps and prints it
        # employees = self.__employee_service.get_employee_overwiew()
        # print(employees)
        
        print()
        print("B Back\n")

        action = input("Choose action: ").lower()
        print()

        if action == "b":
            self.show_employee_menu()
