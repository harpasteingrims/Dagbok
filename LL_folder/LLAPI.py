from IO_folder.IOAPI import IOAPI
from LL_folder.GetDestinationsLL import GetDestinationsLL
from LL_folder.GetAirplanesLL import GetAirplanesLL
from LL_folder.GetEmployeesLL import GetEmployeesLL
from LL_folder.GetVoyagesLL import GetVoyagesLL
from LL_folder.GetIAAD import GetIAAD
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
        self.getiaad = GetIAAD(self.ioapi)
    

    """EMPLOYEES"""
    def get_employee_overview(self):
        return self.getemployees.list_all_employees() #Þetta kallar á klasann getemployees og fallið þar inni sem nær í alla employees

    def get_pilot_overview(self):
        return self.getemployees.list_all_pilots()

    def get_cabin_crew_overview(self):
        return self.getemployees.list_all_cabin_crew()

    def find_common_named_pilots_by_name(self,name):
        return self.getemployees.find_common_named_pilots(name)
    
    def get_info_about_pilot_by_name(self, name):
        return self.getemployees.list_info_about_pilot_by_name(name)
    
    def find_common_named_cabincrew_by_name(self,name):
        return self.getemployees.find_common_named_cabincrew(name)

    def get_info_about_cabincrew_by_name(self, name):
        self.getemployees.list_info_about_cabincrew_by_name(name)

    def get_schedule_cabincrew_by_date(self, name, date_from, date_to):
        pass

    def get_schedule_pilot_by_date(self, name, date_from, date_to):
        pass

    """DESTINATIONS"""
    def get_destination_overview(self): #Þessi listi þarf að vera númeraður
        return self.getdestinations.list_all_destinations()


    """VOYAGES"""
    def get_voyages_overview(self):
        return self.getvoyages.list_all_voyages()

    def get_not_staffed_voyages(self):
        return self.getvoyages.list_not_staffed_voyages()

    def get_common_voyages(self):
        return self.getvoyages.list_all_common_voyages()

    def get_unavailable_time_for_voyage(self):
        return self.getvoyages.list_unavailable_voyage_time()


    """AIRPLANES"""

    def get_airplanes_overview(self):
        return self.getairplanes.list_all_airplanes()

    def get_available_airplanes_by_date(self, voyage_date): #Þessi listi þarf að vera númeraður
        return self.getairplanes.list_available_airplanes_by_date(voyage_date)


    """IAAD"""

    def get_available_emp_by_date(self, user_input_date):
        return self.getiaad.list_available_emp_by_date(user_input_date)

    def get_unavailable_emp_by_date(self, user_input_date):
        return self.getiaad.list_unavailable_emp_by_date(user_input_date)

    def get_airplane_status_by_date(self, user_input_date):
        return self.getiaad.list_airplane_status_by_date(user_input_date)

    def get_voyages_status_by_date(self, user_input_date):
        return self.getiaad.list_voyages_status_by_date(user_input_date)


    #__init__(self):
        #self.llayer = LLAPI()
        #self.mainmenu = MainmenuUI()
        #...
