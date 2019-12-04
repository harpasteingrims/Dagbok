from IO_folder.IOAPI import IOAPI
from LL_folder.GetDestinationsLL import GetDestinationsLL
from LL_folder.GetAirplanesLL import GetAirplanesLL
from LL_folder.GetEmployeesLL import GetEmployeesLL
from LL_folder.GetVoyagesLL import GetVoyagesLL
from LL_folder.UpdateLL import UpdateLL
from LL_folder.CreateLL import CreateLL

class LLAPI():
    def __init__(self):
        self.ioapi = IOAPI()
        
        #self.createll = getcreatell #Þetta á að vera klasi
        #self.updatell = getupdatell
        self.getvoyages = GetVoyagesLL()
        self.getairplanes = GetAirplanesLL()
        self.getdestinations = GetDestinationsLL()
        self.getemployees = GetEmployeesLL()
    

    """Setti þetta inn hér þetta var það sem ég var byrjuð á í UIAPI"""
    
    #EMPLOYEES   
    def get_employee_overview(self):
        return self.getemployees.get_all_employees() #Þetta kallar á klasann getemployees og fallið þar inni sem nær í alla employees

    def get_pilot_overview(self):
        pass

    def get_cabin_crew_overview(self):
        pass
    
    def get_info_about_pilot_by_name(self):
        pass

    #DESTINATIONS
    def get_destination_overview(self):
        # fall fyrir show_destination_overview, í því falli á að prenta út overview af destinations
        #kalla á LL-layer klasann sem er með lista af destinations
        #return
        return self.getdestinations.get_all_destinations()

    def new_destination(self):
        # fall fyrir show_create_des_form, þarf að senda nýja 
        pass


    #VOYAGES
    def get_voyages_overview(self):
        return self.getvoyages.get_all_voyages()

    #__init__(self):
        #self.llayer = LLAPI()
        #self.mainmenu = MainmenuUI()
        #...


    def add_employee(self):
        pass

    def get_employee(self):
        pass #Listar allar employees
