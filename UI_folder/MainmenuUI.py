import sys
sys.path.insert(1, '~/VERKLEGT-1-verkefni/')

from EmployeesUI import EmployeesUI
from VoyagesUI import VoyagesUI
from DestinationsUI import DestinationUI
from AirplanesUI import AirplanesUI
from IAADUI import IAADUI
#from LogicLayer_folder.LLAPI import LLAPI

class MainmenuUI():
    LENGTH_STAR = 20

    #def __init__(self):
        #self.__employess_service = LLAPI()

    def show_main_menu(self):

        #Just to start things up
        run = True
        
        while run is True:
            print("*" * self.LENGTH_STAR)
            print("MAIN MENU\n\n1 Employees\n2 Voyages\n3 Destinations\n4 Airplanes\n5 Search a date\n")
        
            #Hérna vantar input check, break ef >5 og setja run í false
            action = input("Choose action: ")
            print()
            if action == "1":
                EmployeesUI.show_employee_menu(self)

            elif action == "2":
                Voyages_UI.show_voyage_menu()
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
    menu = MainmenuUI()
    menu.show_main_menu()

main()
