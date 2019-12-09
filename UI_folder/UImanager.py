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
        self.iaad = IAADUI(self.llapi)
        self.employees = EmployeesUI(self.llapi)
        self.employeesUI = EmployeesUI(self.llapi, self.employees)
        self.voyages = VoyagesUI(self.llapi)
        self.destinations = DestinationsUI(self.llapi)
        self.airplanes = AirplanesUI(self.llapi)
        self.cabincrew = CabincrewUI(self.llapi, self.employeesUI)
        self.pilots = PilotsUI(self.llapi, self.employeesUI)
        
    def mainmenuUI(self):    
        action_str = ""

        while action_str != "q":
            print(self.LENGTH_STAR * "*")
            print("MAIN MENU")
            print()
            print("1 Employees")
            print("2 Voyages")
            print("3 Destinations")
            print("4 Airplanes")
            print("5 Search a date")
            print("Q Quit")
            print()
    
            action_str = input("Choose action: ").lower()
        
            if action_str == "1":
                self.employeesUI.show_employee_menu()

            elif action_str == "2":
                self.voyages.show_voyage_menu()

            elif action_str == "3":
                self.destinations.show_destination_menu()

            elif action_str == "4":
                self.airplanes.show_airplane_menu()

            elif action_str == "5":
                self.iaad.show_enter_date_menu()

    def choose_a_number(self):
        chosen_number = input("Choose a number: ")
        return chosen_number