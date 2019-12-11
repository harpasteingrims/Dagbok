from models.PilotsModel import PilotsModel
from UI_folder.EmployeesUI import EmployeesUI
from datetime import datetime , timedelta
import datetime

class InputCheckLL():
    '''Subclass of LLAPI that is designed to create something and error checking the input'''
    
    def __init__(self, ioapi, getvoyages):
        self.ioapi = ioapi
        self.getvoyages = getvoyages

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
        
        employee_list = self.ioapi.get_list_of_all_employees()
        for employee_ob in employee_list:
            if ssn != employee_ob.ssn:
                if int(ssn[4:6]) > 20:
                    if len(ssn) == 10 and ssn.isdigit() and self.check_date(["19" + ssn[4:6], ssn[2:4], ssn[0:2]]) != False:
                        return ssn
                    else:
                        return False
                elif ssn[4] == "0" and 0 < int(ssn[5]) < 4:
                    if len(ssn) == 10 and ssn.isdigit() and self.check_date(["20" + ssn[4:6], ssn[2:4], ssn[0:2]]) != False:
                        return ssn
                    else:
                        return False
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
    
    def check_time(self, date, voyage_year, voyage_month, voyage_day):
        unavailable_times_list = self.getvoyages.list_unavailable_voyage_time( voyage_year, voyage_month, voyage_day)
        for unavailable_time_ob in unavailable_times_list:
            if date[-8:] != unavailable_time_ob.date:
                try:
                    valid_time = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), 0).isoformat()
                    return valid_time
                except ValueError:
                    return False
            else:
                return False

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

        if flight_duration[0:1].isdigit() and flight_duration[3:5].isdigit() and flight_duration[2] == ":" and int(flight_duration[3:5]) < 60:
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

    def check_iaad_time(self, time):

        try:
            valid_time = datetime.datetime(2019, 1, 1, int(time[0]), int(time[1]), 0).isoformat()
            return valid_time[-8:]
        except ValueError:
            return False

    """CHECKING INPUT FOR OTHER"""
    
    def check_date(self, date):
        try:
            valid_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 00, 00, 0).isoformat()
            return valid_date[0:10]
        except ValueError:
            return False

    def check_input_number(self, chosen_number, ob_list):
        try:
            chosen_number = int(chosen_number)
            if chosen_number and 1 <= chosen_number <= len(ob_list):
                chosen_ob = ob_list[chosen_number-1]
                return chosen_ob

            else:
                return False
        except ValueError:
            return False

