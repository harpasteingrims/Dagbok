from ioapi.create_pilot import create_pilot
from GetEmployeesLL.check_name import check_name
from GetEmployeesLL.check_SSN import check_SSN
from GetEmployeesLL.check_pilot_role import pilot_role
from GetEmployeesLL.check_address import check_address
from GetEmployeesLL.check_mobile_number import check_mobile_number
from GetEmployeesLL.check_email_address import check_email_address
class CreateLL():
    '''Subclass of LLAPI that is only designed to create something'''
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def create_pilot(self, new_pilot):
        '''Method that creates a new pilot'''
        #NÍNAAAAAA ER AÐ COMMENTA TIL ÞÍN - VIKKA

        #ÞARF ÉG EKKI AÐ SENDA ÞETTA ALLT INN Í GETEMPLOYEESLL TIL AÐ INPUT CHECKA EINS OG ÉG ER AÐ GERA FYRIR NEÐAN?
        #SÍÐAN RETURNA ÞESSI FÖLL Í GETEMPLOYEELL MÉR TIL BAKA HVORT INPUTTIÐ SÉ RÉTT SKILURU
        name = check_name(new_pilot.name)
        SSN = check_SSN(new_pilot.ssn)
        pilot_role = check_pilot_role(new_pilot.role)
        address = check_address(new_pilot.address)
        mobile_number = check_mobile_number(new_pilot.mobile_number)
        email_address = check_email_address.(new_pilot.email)

        new_pilot_list = [name, SSN, pilot_role, address, mobile_number, email_address] #vantar check_email_address í GetEmployeesLL sýndist mér
        #nú er ég komin með lista af öllu sem LLAPI sendi mér EN er búin að input checka allt saman og þá get ég sent það í IO
        self.ioapi.create_pilot(new_pilot_list)
        

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