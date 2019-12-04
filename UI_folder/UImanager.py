import sys
sys.path.insert(1, '~/VERKLEGT-1-verkefni/')

from LL_folder.LLAPI import LLAPI
from UI_folder.DestinationsUI import DestinationsUI
from UI_folder.VoyagesUI import VoyagesUI
from UI_folder.EmployeesUI import EmployeesUI
from UI_folder.AirplanesUI import AirplanesUI
from UI_folder.IAADUI import IAADUI
from UI_folder.CabincrewUI import CabincrewUI
from UI_folder.PilotsUI import PilotsUI

class UImanager():
    LENGTH_STAR = 20
    def __init__(self):
        self.llapi = LLAPI()
        self.cabincrew = CabincrewUI()
        self.pilots = PilotsUI()
        self.iaad = IAADUI()
        self.employees = EmployeesUI(self.cabincrew, self.pilots)
        self.voyages = VoyagesUI()
        self.destinations = DestinationsUI()
        self.airplanes = AirplanesUI()
        

    def mainmenuUI(self):
        #Just to start things up
        run = True
        
        while run is True:
            print("*" * self.LENGTH_STAR)
            print("MAIN MENU\n\n1 Employees\n2 Voyages\n3 Destinations\n4 Airplanes\n5 Search a date\n")
        
            #Hérna vantar input check, break ef >5 og setja run í false
            action = input("Choose action: ").lower()
            print()
            if action == "1":
                self.employees.show_employee_menu()

            elif action == "2":
                self.voyages.show_voyage_menu()

            elif action == "3":
                self.destinations.show_destination_menu()

            elif action == "4":
                self.airplanes.show_airplane_menu()

            elif action == "5":
                self.iaad.show_enter_date()
            
            elif action == "q" or action > 5:
                run = False
                break
    

#def main():
#    menu = MainmenuUI()
#    menu.show_main_menu()

#main()
