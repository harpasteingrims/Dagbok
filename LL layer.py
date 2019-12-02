class LLAPI():
    '''Main logic layer that sends objects between the layers'''
    def __init__(self):
        pass

    def call_create_LL():
        pass
    
    def call_update_LL():
        pass
    
    def call_get_LL():
        pass

class create_LL(LLAPI):
    '''Subclass of LLAPI that is only designed to create something'''
    def __init__(self):
        pass

    def create_pilot():
        '''Method that creates a new pilot'''
        new_pilot = {}
        pass

    def create_cabincrew():
        '''Method that creates a new cabincrew member'''
        new_cabincrew = {}
        pass
    
    def create_voyage():
        '''Method that creates a new voyage'''
        new_voyage = {}
        pass

    def create_destination():
        '''Method that creates a new destination'''
        new_destination = {}
        pass
    
    def create_airplanes():
        '''Method that creates a new airplane'''
        airplane_id = input("Enter airplane id: ")
        airplane_type = input("Enter airplane type: ")
        airplane_manufacturer = input("Enter airplane manufacturer: ")
        airplane_seat_amount = input("Enter airplane seat amount: ")
        airplane = [airplane_type, airplane_manufacturer, airplane_seat_amount]
        new_airplane = {}
        new_airplane[airplane_id] = airplane
    
    def create_common_voyages():
        '''Method that creates common voyages'''
        common_voyages = []
        pass

class update_LL():
    def __init__(self):
        pass

    def update_voyages():
        '''Method that updates information about voyages'''
        update_voyage = []
        pass
    
    def update_employee():
        '''Method that updates information about an employee'''
        update_employee = {}
        pass

    def update_destcontact():
        '''Method that updates information about the contact for a certain destination'''
        update_destcontact = {}
        pass
    

class get_LL():

    """ This class gets the command to go and get something """
    
    def __init__(self):
        pass

    def call_get_voyages(self):
        """ This method calls the get voyages class """
        pass

    def call_get_airplanes(self):
        """ This method calls the get airplanes class """
        pass

    def call_get_destinations(self):
        """ This method calls the get destinations class """
        pass

class get_voyages(get_LL):
    """ This class gets information about voyages """

    def __init__(self):
        pass

    def get_unavaliable_staff(self):
        """ This method gets a date and makes a list of the unavaliable staff on that date and returns it  """
        unavaliable_staff = []
        pass

    def get_avaliable_staff(self):
        """ This method gets a date and makes a list of the avaliable staff on that date and returns it """
        avaliable_staff = []
        pass

    def get_unavaliable_times_for_date(self):
        """ This method gets a date and makes a list of the avaliable times on that date and returns it """
        unavaliable_times_for_date = []
        pass

    def get_all_voyages(self):
        """ This method makes a list of all voyages """
        all_voyages = []
        pass

    def get_voyages_by_date(self):
        """ This method gets a date and makes a list of voyages on that date"""
        
class get_airplanes(get_LL):

    def __init__(self):
        pass

    def get_all_airplanes(slef):
        """ This method makes a list of all airplanes and returnes it """
        all_airplanes = []
        pass

class get_destinations(get_LL):

    def __init__(self):
        pass

    def get_all_destinations(self):
        """ This method makes a list of all destinations and returnes it"""
        all_destinations = []
        pass

    def get_contact_of_country(self):
        """ This method gets a name of a country and returnes information about the emergency contact of that country"""
        contact_of_country = []
        pass


class get_employees():
    def __init__(self):
        pass

    def get_searched_employees(self):
        """ This method gets a name to search for and returnes a list of the information about those who have the name"""
        searched_employee = []
        pass

    def get_all_pilots(self):
        """ This method makes a list of all pilots and returns it """
        all_pilots = []
        pass

    def get_all_cabin_crew(self):
        """ This method makes a list of all pilots and returns it"""
        all_cabin_crew = []
        pass

    def get_flight_schedule_of_employee(self):
        """ This method gets a name of an employee and returns a list of his flights"""
        flight_schedule_of_employee = []
        pass
