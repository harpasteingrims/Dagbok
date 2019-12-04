import sys
sys.path.insert(1, '~/VERKLEGT-1-verkefni/')

from LL_folder.LLAPI import LLAPI

class UIAPI():
    ''' EMPLOYEES '''

    def __init__(self):
        self.__voyage_repo = LLAPI()
        
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




    
