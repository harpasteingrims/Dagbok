from models.PilotModel import PilotsModel

class CreateLL():
    '''Subclass of LLAPI that is only designed to create something'''
    
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def create_pilot(self, new_pilot_list):

        name = new_pilot_list[0]
        rank = new_pilot_list[1]
        ssn = new_pilot_list[2]
        address = new_pilot_list[3]
        mobile_number = new_pilot_list[4]
        email = new_pilot_list[5]
        license_type = new_pilot_list[6]

        new_pilot_object = PilotsModel(name, rank, ssn, address, mobile_number, email, license_type)
    
        return self.ioapi.create_pilot(new_pilot_object)
        

    def create_cabincrew(self, new_cabincrew):
        '''Method that creates a new cabincrew member'''
        new_cabincrew_list = []
        new_cabincrew_list.append(new_cabincrew)
        pass
    
    def create_voyage(self, new_voyage):
        '''Method that creates a new voyage'''
        new_voyage_list = []
        new_voyage_list.append(new_voyage)
        pass

    def create_destination(self, new_destination):
        '''Method that creates a new destination'''
        new_destination_list = []
        new_destination_list.append(new_destination)
        pass
    
    def create_airplane(self, new_airplane):
        '''Method that creates a new airplane'''
        new_airplane_list = []
        new_airplane_list.append(new_airplane)
        pass
    
    def create_common_voyage(self, common_voyages):
        '''Method that creates common voyages'''
        common_voyages_list = []
        pass


    """ CHECKING INPUT FOR EMPLOYEES"""


    def check_name(self,name):
            
        if len(name) < 40: 
            return name
        
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

        if license_type in airplane_list:
            return license_type

        else:
            return False

        pass