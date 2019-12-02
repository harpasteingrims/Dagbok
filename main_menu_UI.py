from EmployeeUI import EmployeesUI
from VoyageUI import VoyagesUI
from DestinationUI import DestinationsUI
from AirplaneUI import AirplaneUI
from Information_about_a_date import IAADUI

class Main_menu():

    @classmethod
    def show_main_menu(cls):
        print("MAIN MENU\n\n1 Employees\n2 Voyages\n3 Destinations\n4 Airplanes\n5 Search a date\n")
        
        action = input("Choose action: ")
        print()

        if action == "1":
            EmployeesUI.show_employee_menu()
            pass

        elif action == "2":
            VoyagesUI.show_destination_menu()
            pass

        elif action == "3":
            DestinationsUI.show_destination_menu()
            pass

        elif action == "4":
            AirplaneUI.show_airplane_menu()
            pass

        elif action == "5":
            IAADUI.show_enter_date()
            pass
            
def main():
    Main_menu.show_main_menu()

main()
