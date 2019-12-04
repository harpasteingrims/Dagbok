import sys
sys.path.insert(1, '~/VERKLEGT-1-verkefni/')

from LL_folder.LLAPI import LLAPI
from UI_folder.EmployeesUI import EmployeesUI
from UI_folder.VoyagesUI import VoyagesUI
from UI_folder.DestinationsUI import DestinationsUI
from UI_folder.AirplanesUI import AirplanesUI
from UI_folder.IAADUI import IAADUI
class UImanager():
    
    def __init__(self):
        self.llapi = LLAPI()
        self.employee = EmployeesUI()
        self.voyages = VoyagesUI()
        self.destination = DestinationsUI()
        self.airplanes = AirplanesUI()

    def MainmenuUI(self):















    ''' EMPLOYEES '''    
    def get_employee_overwiew(self):
        pass
        # employees = self.__employee_service.get_employee_overwiew()

    def get_pilot_overview(self):
        pass

    def get_cabin_crew_overwiew(self):
        pass
    
    def get_info_about_pilot_by_name(self):
        pass

    ''' DESTINATIONS '''
    def get_destination_overview(self):
        # fall fyrir show_destination_overview, í því falli á að prenta út overview af destinations
        #kalla á LL-layer klasann sem er með lista af destinations
        #return
        pass
    def new_destination(self):
        # fall fyrir show_create_des_form, þarf að senda nýja 
        pass

    def get_voyages_overview(self):
        return self.__voyage_repo.get_voyages()

    #__init__(self):
        #self.llayer = LLAPI()
        #self.mainmenu = MainmenuUI()
        #...


#Þetta er rotarskrain

# Arnar: látið þessa skrá bara heita __main__.py og hafið hana ekki
# í sér möppu heldur í möppunni sem ER raunverulega rótin á verkefninu
# (þeas í möppunni  VERKLEGT-1-verkefni)


from UI_folder.MainmenuUI import MainmenuUI

def main():
    ui = MainmenuUI()
    ui.show_main_menu()

if __name__ == '__main__':
    main()

    
