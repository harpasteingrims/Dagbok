from models.PilotModel import PilotsModel
from UI_folder.EmployeesUI import EmployeesUI

class InputCheckLL():
    '''Subclass of LLAPI that is designed to create something and error checking the input'''
    
    def __init__(self, ioapi):
        self.ioapi = ioapi

    """ CHECKING INPUT FOR EMPLOYEES"""

    def check_name(self, name):
        if " " in name:
            first_name, last_name = name.split()
            
            if len(name) < 40 and first_name.isalpha() and last_name.isalpha():
            
                return name.title()

            else:
                return False
        else: 
            return False

    def check_pilot_rank(self, rank):

        if rank == "1":
            rank = "Captain"
            return rank
        elif rank == "2":
            rank = "Copilot"
            return rank
        else:
            return False
        
    def check_crew_member_rank(self, rank):

        if rank == "1":
            rank = "Flight Service Manager"
            return rank
        elif rank == "2":
            rank = "Flight Attendant"
            return rank
        else:
            return False

    def check_ssn(self, ssn):
        
        if len(ssn) == 10 and ssn.isdigit() and self.check_iaad_month(ssn[2:4], ) != False and self.check_iaad_day(ssn[0:2], ssn[2:4]) != False:
            return ssn
        else:
            return False
    
    def check_address(self, address_list):

        if len(address_list) == 3:
            
            address_name = address_list[0]
            house_number = address_list[1]
            zip_code = address_list[2]

            if len(zip_code) == 3 and int(zip_code) and address_name.isalpha() and int(house_number):
                return address_list[0].capitalize() + str(address_list[1]) + str(address_list[2])
            else: 
                return False
        else: 
            return False

    def check_mobile_number(self, mobile_number):
        
        if len(mobile_number) == 7 and mobile_number.isdigit():
            return mobile_number
        else:
            return False

    def check_email(self, email):

        if "@" in email and "." in email:
            return email.lower()
        else:
            return False
    
    def check_license_type(self, license_type_num, plane_list):
        try:
            if int(license_type_num) and 1 <= license_type_num <= len(plane_list):
                chosen_license_ob = airplane_ob_list[license_type_num-1]
                return chosen_license_ob

        except ValueError:
            return False


    """CHECKING INPUT FOR VOYAGES"""
    
    
    def calculate_arrival_time(self,new_voyage_object):
        #kann ekki nóg á datetime til að forrita þetta einmitt núna
        return new_voyage_object

    """CHECKING INPUT FOR DESTINATIONS"""

    def check_country(self, country):

        if country.isalpha():
            return country.title()
        else:
            return False

    def check_airport(self, airport):

        if airport.isalpha():
            return airport.title()
        else:
            return False

    def check_flight_duration(self, flight_duration):

        if flight_duration[0:1].isdigit() and flight_duration[3:5].isdigit() and flight_duration[2] == ":":
            return flight_duration
        else:
            return False

    def check_distance(self, distance):

        if distance[-3:] == " km":
            return distance
        else:
            return False

    def check_contact(self, contact):

        if contact.isalpha():
            return contact.title
        else:
            return False

    def check_contact_number(self, contact_number): 

        if contact_number.replace("+", "").replace(" ", "").isdigit():
            return contact_number
        else:
            return False

    """ CHECKING INPUT FOR AIRPLANES"""

    def check_airplane_id(self, airplane_id):
        
        if len(airplane_id) == 6:
            return airplane_id.upper()
        else: 
            return False

    def check_manufacturer(self, manufacturer):

        if manufacturer.isalpha():
            return manufacturer.capitalize()
        else:
            return False

    def check_seat_amount(self, seat_amount):

        if seat_amount.isdigit() and 2 <= int(seat_amount) <= 800:
            return seat_amount
        else:
            return False


    """CHECKING INPUT FOR IAAD"""

    def check_iaad_year(self, iaad_year):

        if len(iaad_year) == 4 and iaad_year.isdigit() and int(iaad_year) >= 2019:
            return iaad_year
        else:
            return False

    def check_iaad_month(self, iaad_month, iaad_year = 0):

        if len(iaad_month) == 2 and iaad_month.isdigit() and 0 < int(iaad_month) < 13:
            return iaad_month
        else:
            return False

    def check_iaad_day(self, iaad_day, iaad_month, iaad_year = 0):

        if iaad_month == "01" or iaad_month == "03" or iaad_month == "05" or iaad_month == "07" or iaad_month == "08" or iaad_month == "10" or iaad_month == "12":
            if len(iaad_day) == 2 and iaad_day.isdigit() and 0 < int(iaad_day) < 32:
                return iaad_day
            else:
                return False
        elif iaad_month == "04" or iaad_month == "06" or iaad_month == "09" or iaad_month == "11":
            if len(iaad_day) == 2 and iaad_day.isdigit() and 0 < int(iaad_day) < 31:
                return iaad_day
            else:
                return False
        elif iaad_month == "02" and int(iaad_year) % 4 == 0 and int(iaad_year) % 100 != 0 and int(iaad_year) % 400 != 0:
            if len(iaad_day) == 2 and iaad_day.isdigit() and 0 < int(iaad_day) < 30:
                return iaad_day
            else:
                return False
        elif iaad_month == "02":
            if len(iaad_day) == 2 and iaad_day.isdigit() and 0 < int(iaad_day) < 29:
                return iaad_day
            else:
                return False
        else:
            return False
