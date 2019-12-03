from EmployeesUI import EmployeesUI
from VoyagesUI import VoyagesUI
from DestinationsUI import DestinationsUI
from AirplanesUI import AirplaneUI
from IAADUI import IAADUI

class MainmenuUI():
    lenght_star = 20

    @classmethod
    def show_main_menu(cls):

        print("*"*cls.lenght_star)
        print("MAIN MENU\n\n1 Employees\n2 Voyages\n3 Destinations\n4 Airplanes\n5 Search a date\n")
        
        action = input("Choose action: ")
        print()

        if action == "1":
            EmployeesUI.show_employee_menu()

        elif action == "2":
            VoyagesUI.show_voyage_menu()
            pass

        elif action == "3":
            DestinationsUI.show_destination_menu()
            pass

        elif action == "4":
            AirplanesUI.show_airplane_menu()
            pass

        elif action == "5":
            IAADUI.show_enter_date()
            pass
            
def main():
    Main_menu.show_main_menu()

main()
