from models.PilotModel import PilotsModel

class CreateLL():
    '''Subclass of LLAPI that is designed to create something and error checking the input'''
    
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def create_pilot(self, new_pilot_ob):
        """Method that creates a new pilot"""
        return self.ioapi.create_pilot(new_pilot_ob)
        
    def create_cabincrew(self, new_cabincrew_ob):
        '''Method that creates a new cabincrew member'''
        return self.ioapi.new_cabincrew_ob
    
    def create_voyage(self, new_voyage_ob):
        '''Method that creates a new voyage'''
        return self.ioapi.new_voyage_ob

    def create_destination(self, new_destination_ob):
        '''Method that creates a new destination'''
        return self.ioapi.new_destination_ob
    
    def create_airplane(self, new_airplane_ob):
        '''Method that creates a new airplane'''
        return self.ioapi.new_airplane_ob
    
    def create_common_voyage(self, common_voyages_ob):
        '''Method that creates common voyages'''
        return self.ioapi.common_voyages_ob

    """ CHECKING INPUT FOR EMPLOYEES"""

    def check_name(self,name):

        if len(name) < 40 and name.isalpha(): 
            return name
        
        else:
            return False


    def check_pilot_rank(self, rank):s

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
        
        if len(ssn) == 10:
            return ssn
        
        else:
            return False
    
    def check_address(self, address):
        zip_code, address_name, house_number = address.split()

        if len(zip_code) == 3 and zip_code.isdigit() and address_name.isalpha() and house_number.isdigit():
            return address
        
        else: 
            return False

    def check_mobile_number(self, mobile_number):
        
        mobile_number_int = int(mobile_number)
        try:

            if len(mobile_number) == 7 and mobile_number.isdigit():
                return mobile_number

        except ValueError:
            return False

    def check_email(self, email):
        if "@" in email and "." in email:
            return email
        
        else:
            return False
    
    def check_license_type(self, license_type):
        #ariplane_list = vantar fallið úr airplanes

        if license_type in ariplane_list:
            return license_type

        else:
            return False

        pass

    """ CHECKING INPUT FOR VOYAGES"""

    """ CHECKING INPUT FOR DESTINATIONS"""

    """ CHECKING INPUT FOR AIRPLANES"""

    def check_airplane_id(self, airplane_id):
        
        if len(airplane_id) == 6:
            return airplane_id
        else: return False