from IO_folder.IOAPI import IOAPI
from LL_folder.GetDestinationsLL import GetDestinationsLL
from LL_folder.GetAirplanesLL import GetAirplanesLL
from LL_folder.GetEmployeesLL import GetEmployeesLL
from LL_folder.GetVoyagesLL import GetVoyagesLL
from LL_folder.GetIAAD import GetIAAD
from LL_folder.UpdateLL import UpdateLL
from LL_folder.InputCheckLL import InputCheckLL

class LLAPI():
    def __init__(self):
        self.ioapi = IOAPI()
        self.inputcheckll = InputCheckLL(self.ioapi)
        self.updatell = UpdateLL(self.ioapi)
        self.getvoyages = GetVoyagesLL(self.ioapi)
        self.getairplanes = GetAirplanesLL(self.ioapi)
        self.getdestinations = GetDestinationsLL(self.ioapi)
        self.getemployees = GetEmployeesLL(self.ioapi)
        self.getiaad = GetIAAD(self.ioapi)

    """ EMPLOYEES """

    def get_employee_overview(self):
        return self.getemployees.list_all_employees() #Þetta kallar á klasann getemployees og fallið þar inni sem nær í alla employees
    
    def check_name(self, name):
        return self.inputcheckll.check_name(name)
    
    def check_pilot_rank(self, rank):
        return self.inputcheckll.check_pilot_rank(rank)

    def check_crew_member_rank(self, rank):
        return self.inputcheckll.check_crew_member_rank(rank)

    def check_ssn(self, ssn):
        return self.inputcheckll.check_ssn(ssn)

    def check_address(self, address):
        return self.inputcheckll.check_address(address)

    def check_mobile_number(self, mobile_number):
        return self.inputcheckll.check_mobile_number(mobile_number)
    
    def check_email(self, email):
        return self.inputcheckll.check_email(email)
    
    def check_license_type(self, license_type):
        return self.inputcheckll.check_license_type(license_type)
        #þarf að klára í getempll

    """ PILOTS """

    def get_pilot_overview(self):
        return self.getemployees.list_all_pilots()
        
    def get_common_named_pilots(self,name):
        return self.getemployees.find_common_named_pilots(name)
    
    def create_new_pilot(self, new_pilot_ob):
        return self.ioapi.create_pilot(new_pilot_ob)
    
    def update_new_pilot_information(self, updated_pilot_ob):
        return self.ioapi.update_pilot(updated_pilot_ob)

    """ CABIN CREW """

    def get_cabin_crew_overview(self):
        return self.getemployees.list_all_cabin_crew()

    def get_common_named_crew_members(self, name):
        return self.getemployees.find_common_named_crew_members(name)

    def get_schedule_cabincrew_by_date(self, name, date_from, date_to):
        return self.getemployees.list_schedule_cabincrew_by_date(name, date_from, date_to)

    def create_new_cabin_crew(self, new_cabincrew_ob):
        return self.ioapi.create_cabincrew(new_cabincrew_ob)

    def update_new_crew_member_information(self, updated_crew_member_ob):
        return self.ioapi.update_cabincrew(updated_crew_member_ob)

    """VOYAGES"""

    def get_voyages_overview(self):
        return self.getvoyages.list_all_voyages()

    def get_not_staffed_voyages(self):
        return self.getvoyages.list_not_staffed_voyages()

    def get_common_voyages(self):
        return self.getvoyages.list_all_common_voyages()

    def get_unavailable_time_for_voyage(self, voyage_year, voyage_month, voyage_day):
        return self.getvoyages.list_unavailable_voyage_time(voyage_year, voyage_month, voyage_day)

    def get_numbered_common_voyage_dict(self):
        pass    

    def create_new_voyage(self, new_voyage_object):
        return self.ioapi.create_voyage(new_voyage_object)

    def create_new_common_voyage(self, common_voyage_object):
        #HÉR Á EFTIR AÐ VINNA
        common_voyage_object = []
        voyage_list = self.ioapi.get_all_voyages_list()
        return common_voyage_list
    
    def update_voyage(self, updated_voyage_ob):
        return self.ioapi.update_voyage(updated_voyage_ob)

    #Vantar check föll

    """DESTINATIONS"""

    def get_destination_overview(self): #Þessi listi þarf að vera númeraður
        return self.getdestinations.list_all_destinations()

    def get_airport_overview(self):
        return self.getdestinations.list_all_airports()

    def create_new_destination(self, new_destination_ob):
        return self.ioapi.create_destination(new_destination_ob)

    def update_new_emerg_contact(self, updated_emergency_contact_ob):
        return self.ioapi.update_emergency_contact(updated_emergency_contact_ob)

    def check_country(self, country):
        return self.inputcheckll.check_country(country)

    def check_airport(self, airport):
        return self.inputcheckll.check_airport(airport)

    def check_flight_duration(self, flight_duration):
        return self.inputcheckll.check_flight_duration(flight_duration)

    def check_distance(self, distance):
        return self.inputcheckll.check_distance(distance)

    def check_contact(self, contact):
        return self.inputcheckll.check_contact(contact)

    def check_contact_number(self, contact_number):
        return self.inputcheckll.check_contact_number(contact_number)

    """AIRPLANES"""

    def get_airplanes_overview(self):
        return self.getairplanes.list_all_airplanes()
    
    def get_numbered_employee_dict(self):
        airplane_list = self.get_airplanes_overview()
        return self.getairplane.make_numbered_airplane_dict(airplane_list)

    def get_airplane_object_from_numbered_dict(self, numbered_airplane_dict, input_airplane_name):
        return self.getairplane.get_airplane_object_from_numbered_dict(numbered_airplane_dict, input_airplane_name)

    def get_available_airplanes_by_date(self, voyage_date): #Þessi listi þarf að vera númeraður
        return self.getairplanes.list_available_airplanes_by_date(voyage_date)

    def create_new_airplane(self, new_airplane_object):
        return self.ioapi.create_airplane(new_airplane_object)

    def check_airplane_id(self, airplane_id):
        return self.inputcheckll.check_airplane_id(airplane_id)

    def check_manufacturer(self, manufacturer):
        return self.inputcheckll.check_manufacturer(manufacturer)

    def check_seat_amount(self, seat_amount):
        return self.inputcheckll.check_seat_amount(seat_amount)

    """IAAD"""

    def get_available_emp_by_date(self, user_input_date):
        return self.getiaad.list_available_emp_by_date(user_input_date)

    def get_unavailable_emp_by_date(self, user_input_date):
        return self.getiaad.list_unavailable_emp_by_date(user_input_date)

    def get_airplane_status_by_date(self, user_input_date):
        return self.getiaad.list_airplane_status_by_date(user_input_date)

    def get_voyages_status_by_date(self, user_input_date):
        return self.getiaad.list_voyages_status_by_date(user_input_date)

    def check_iaad_year(self, iaad_year):
        return self.inputcheckll.check_iaad_year(iaad_year)

    def check_iaad_month(self, iaad_month, iaad_year):
        return self.inputcheckll.check_iaad_month(iaad_month, iaad_year)

    def check_iaad_day(self, iaad_day, iaad_month, iaad_year):
        return self.inputcheckll.check_iaad_day(iaad_day, iaad_month, iaad_year)

    #__init__(self):
        #self.llayer = LLAPI()
        #self.mainmenu = MainmenuUI()
        #...
