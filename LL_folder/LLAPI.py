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
    
    def check_name(self,name):
        self.getemployees.check_name(name)
    
    def check_pilot_rank(self, rank):
        self.getemployees.check_pilot_rank(rank)

    def check_ssn(self, ssn):
        self.getemployees.check_ssn(ssn)

    def check_address(self, address):
        self.getemployees.check_address(address)

    def check_mobile_number(self, mobile_number):
        self.getemployees.check_mobile_number(mobile_number)
    
    def check_email(self,email):
        self.getemployees.check_email(email)
    
    def check_license_type(self, license_type):
        self.getemployees.check_license_type(liscense_type)
        #þarf að klára í getempll

    """ PILOTS """

    def get_pilot_overview(self):
        return self.getemployees.list_all_pilots()
        
    def get_common_named_pilots_by_name(self,name):
        return self.getemployees.find_common_named_pilots(name)
    
    def get_numbered_employee_dict(self, pilot_list):
        return self.getemployees.make_numbered_employee_dict(pilot_list)

    def get_employee_object_from_numbered_dict(self, numbered_pilot_dict, input_name):
        return self.getemployees.get_employee_object_from_numbered_dict(numbered_pilot_dict, input_name)

    def get_schedule_pilot_by_date(self, pilot_object, date_from, date_to):
        return self.getemployees.list_schedule_pilot_by_date(name, date_from, date_to)
        # eftir að klára

    def create_new_pilot(self):
        return self.createll.create_pilot()
    
    def update_new_pilot_information(self):
        return self.updatell.update_pilot_information()


    """ CABIN CREW """

    def get_cabin_crew_overview(self):
        return self.getemployees.list_all_cabin_crew()

    def get_common_named_cabincrew_by_name(self,name):
        return self.getemployees.find_common_named_cabincrew(name)

    def get_info_about_cabincrew_by_name(self, name):
        return self.getemployees.list_info_about_cabincrew_by_name(name)

    def get_schedule_cabincrew_by_date(self, name, date_from, date_to):
        return self.getemployees.list_schedule_cabincrew_by_date(name, date_from, date_to)

    def create_new_cabincrew(self):
        return self.createll.create_cabincrew()

    def update_new_cabincrew_information(self):
        return self.updatell.update_cabincrew_information()

    """DESTINATIONS"""
    def get_destination_overview(self): #Þessi listi þarf að vera númeraður
        return self.getdestinations.list_all_destinations()

    def get_airport_overview(self):
        return self.getdestinations.list_all_airports()

    def create_new_destination(self):
        return self.createll.create_destination()

    def update_new_emerg_contact(self):
        return self.updatell.update_emergency_contact()


    """VOYAGES"""
    def get_voyages_overview(self):
        return self.getvoyages.list_all_voyages()

    def get_not_staffed_voyages(self):
        return self.getvoyages.list_not_staffed_voyages()

    def get_common_voyages(self):
        return self.getvoyages.list_all_common_voyages()

    def get_unavailable_time_for_voyage(self, voyage_year, voyage_month, voyage_day):
        return self.getvoyages.list_unavailable_voyage_time(voyage_year, voyage_month, voyage_day)

    def create_new_voyage(self):
        return self.createll.create_voyage()

    def create_new_common_voyage(self):
        return self.createll.create_common_voyage()


    """AIRPLANES"""

    def get_airplanes_overview(self):
        return self.getairplanes.list_all_airplanes()

    def get_available_airplanes_by_date(self, voyage_date): #Þessi listi þarf að vera númeraður
        return self.getairplanes.list_available_airplanes_by_date(voyage_date)

    def create_new_airplane(self):
        return self.createll.create_airplane()


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
