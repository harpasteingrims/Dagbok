#from CabincrewUI import CabincrewUI
#from PilotUI import PilotsUI

#from VoyageUI import Voyages_UI
#from DestinationUI import Destinations_UI
#form AirplaneUI import Airplane_UI
#from Information_about_a_date import IAAD_UI

class EmployeesUI():
    LENGTH_STAR = 20
    
    def __init__(self):
        # self.__employee_service = LLAPI()
        pass

    def show_employee_menu(self):
        print(self.LENGTH_STAR * "*")
        print("EMPLOYEES MENU \n\n1 Print overview of all employees \n2 Search for an employee \n3 Pilots \n4 Cabin Crew \nB Back \n")
        
        action = input("Choose action: ")
        print()

        if action == "1":
            self.show_overview_of_all_employees()

        elif action == "2":
            PilotsUI.show_pilot_menu()

        elif action == "3":
            CabincrewUI.show_cabin_crew_menu()

        elif action == "B":
            Main_menu.show_main_menu()

    def show_overview_of_all_employees(self):
        print("OVERVIEW OF EMPLOYEES")

        # calls the method that makes a list of all emps and prints it
        # employees = self.__employee_service.get_employess()
        # print(employees)
        print("B Back\n")

        action = input("Choose action: ")
        print()

        if action == "B":
            self.show_employee_menu()
