from EmployeeUI import Employees_UI
#from VoyageUI import Voyages_UI
#from DestinationUI import Destinations_UI
#form AirplaneUI import Airplane_UI
#from Information_about_a_date import IAAD_UI

class Main_menu():

    @classmethod
    def show_main_menu(cls):
        print("MAIN MENU\n\n1 Employees\n2 Voyages\n3 Destinations\n4 Airplanes\n5 Search a date\n")
        
        action = input("Choose action: ")
        print()

        if action == "1":
            Employees_UI.show_employee_menu()
            pass

        elif action == "2":
            Voyages_UI.show_destination_menu()
            pass

        elif action == "3":
            Destinations_UI.show_destination_menu()
            pass

        elif action == "4":
            Airplane_UI.show_airplane_menu()
            pass

        elif action == "5":
            IAAD_UI.show_enter_date()
            pass
            
def main():
    Main_menu.show_main_menu()

main()
