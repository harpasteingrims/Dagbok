from models.PilotModel import PilotsModel

class InputCheckLL():
    '''Subclass of LLAPI that is designed to create something and error checking the input'''
    
    def __init__(self, ioapi):
        self.ioapi = ioapi

    """ CHECKING INPUT FOR EMPLOYEES"""

    def check_name(self, name):

        first_name, last_name = name.split()
            
        if len(name) < 40 and first_name.isalpha() and last_name.isalpha(): 
            return name.title()
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
        
        if len(ssn) == 10 and ssn.isdigit():
            return ssn
        else:
            return False
    
    def check_address(self, address):
        zip_code, address_name, house_number = address.split()

        if len(zip_code) == 3 and zip_code.isdigit() and address_name.isalpha() and house_number.isdigit():
            return address[0:4] + address[4].upper() + address[5:]
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
    
    def check_license_type(self, license_type):
        airplane_object_list = self.llapi.get_airplanes_overview()

        if license_type in airplane_object_list:
            return license_type
        else:
            return False

        pass

    """CHECKING INPUT FOR VOYAGES"""

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

    def check_flight_airport(self, flight_duration):

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