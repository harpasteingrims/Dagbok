from models.PilotModel import PilotsModel
from UI_folder.EmployeesUI import EmployeesUI
from datetime import datetime , timedelta
import datetime

class InputCheckLL():
    '''Subclass of LLAPI that is designed to create something and error checking the input'''
    
    def __init__(self, ioapi):
        self.ioapi = ioapi

    """CHECKING INPUT FOR EMPLOYEES"""

    def check_name(self, name):
        if len(name.split()) > 1:
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
        
        if int(ssn[4:6]) > 20:
            if len(ssn) == 10 and ssn.isdigit() and self.check_iaad_month(ssn[2:4], "19" + ssn[4:6]) != False and self.check_iaad_day(ssn[0:2], ssn[2:4], "19" + ssn[4:6]) != False:
                return ssn
            else:
                return False
        elif ssn[4] == "0" and 0 < int(ssn[5]) < 4:
            if len(ssn) == 10 and ssn.isdigit() and self.check_iaad_month(ssn[2:4], "20" + ssn[4:6]) != False and self.check_iaad_day(ssn[0:2], ssn[2:4], "20" + ssn[4:6]) != False:
                return ssn
            else:
                return False
        else:
            return False
    
    def check_address(self, address):

        if len(address) == 3:
            address_name = address[0]
            house_number = address[1]
            zip_code = address[2]

            if len(zip_code) == 3 and address_name.isalpha() and house_number.isdigit() and zip_code.isdigit():
                return address[0].capitalize() + " " + str(address[1]) + " " + str(address[2])
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
            license_type_int = int(license_type_num)
            
            if license_type_int and 1 <= license_type_int <= len(plane_list):
                chosen_license_ob = plane_list[license_type_int-1]
                return chosen_license_ob

        except ValueError:
            return False

    """CHECKING INPUT FOR VOYAGES"""
    
    

    """CHECKING INPUT FOR DESTINATIONS"""

    def check_country(self, country):

        if " " in country:
            country_list = country.split()
            for element in country_list:
                element.isalpha()
            
            return country.title()

        elif country.isalpha():
            return country.title()

        else:
            return False

    def check_airport(self, airport):

        if " " in airport:
            airport_list = airport.split()
            for element in airport_list:
                element.isalpha()
            
            return airport.title()
        
        elif airport.isalpha():
            return airport.title()
            
        else:
            return False

    def check_flight_duration(self, flight_duration):

        if flight_duration[0:1].isdigit() and flight_duration[3:5].isdigit() and flight_duration[2] == ":":
            return flight_duration
        else:
            return False

    def check_distance(self, distance):

        if distance[-3:] == " km" and distance[:-3].isdigit():
            return distance 
        elif distance[-2:] == "km" and distance[:-2].isdigit():
            return distance[:-2] + " " + distance[-2:]
        else:
            return False

    def check_contact_number(self, contact_number): 

        if contact_number.replace("+", "").replace(" ", "").isdigit() and len(contact_number) < 14:
            return contact_number
        else:
            return False

    """ CHECKING INPUT FOR AIRPLANES"""

    def check_airplane_id(self, airplane_id):
        
        if len(airplane_id) == 6 and airplane_id[2] == "-":
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

    def check_date(self, date):
        try:
            valid_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 00, 00, 0).isoformat()
            return valid_date
        except ValueError:
            return False

    def time_check(self, time):
        pass

    def check_iaad_year(self, iaad_year):

        if len(iaad_year) == 4 and iaad_year.isdigit() and int(iaad_year) >= 2019:
            return iaad_year
        else:
            return False

    def check_iaad_month(self, iaad_month, iaad_year):

        if len(iaad_month) == 2 and iaad_month.isdigit() and 0 < int(iaad_month) < 13:
            return iaad_month
        else:
            return False

    def check_iaad_day(self, iaad_day, iaad_month, iaad_year):

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
