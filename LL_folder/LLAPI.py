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
        self.createll = CreateLL(self.ioapi)
        self.updatell = UpdateLL(self.ioapi)
        self.getvoyages = GetVoyagesLL(self.ioapi)
        self.getairplanes = GetAirplanesLL(self.ioapi)
        self.getdestinations = GetDestinationsLL(self.ioapi)
        self.getemployees = GetEmployeesLL(self.ioapi)
    

    """EMPLOYEES"""
    def get_employee_overview(self):
        return self.getemployees.get_all_employees() #Þetta kallar á klasann getemployees og fallið þar inni sem nær í alla employees

    def get_pilot_overview(self):
        return self.getemployees.get_all_pilots()

    def get_cabin_crew_overview(self):
        return self.getemployees.get_all_cabin_crew()
    
    def get_info_about_pilot_by_name(self):
        pass

    def get_info_about_cabincrew_by_name(self):
        pass

    def get_schedule_cabincrew_by_date(self):
        pass

    def get_schedule_pilot_by_date(self):
        pass

    """DESTINATIONS"""
    def get_destination_overview(self): #Þessi listi þarf að vera númeraður
        return self.getdestinations.get_all_destinations()

    def new_destination(self):
        # fall fyrir show_create_des_form, þarf að senda nýja 
        pass


    """VOYAGES"""
    def get_voyages_overview(self):
        return self.getvoyages.get_all_voyages()

    def get_not_staffed_voyages(self):
        return self.getvoyages.get_not_staffed()

    def get_common_voyages(self):
        pass

    def get_unavailable_time_for_voyage(self):
        pass


    """AIRPLANES"""

    def get_airplanes_overview(self):
        return self.getairplanes.get_all_airplanes()

    def add_employee(self):
        pass

    def get_employee(self):
        pass #Listar allar employees

    def get_available_airplanes_by_date(self): #Þessi listi þarf að vera númeraður
        pass


    """IAAD"""

    def get_available_employess_by_date(self):
        pass

    def get_unavailable_employees_by_date(self):
        pass

    def get_airplane_status_by_date(self):
        pass

    def get_voyages_status_by_date(self):
        pass


    #__init__(self):
        #self.llayer = LLAPI()
        #self.mainmenu = MainmenuUI()
        #...
