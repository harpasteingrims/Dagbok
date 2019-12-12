from IO_folder.CreateIO import CreateIO
from IO_folder.GetIO import GetIO
from IO_folder.UpdateIO import UpdateIO

class IOAPI():
    def __init__(self):
        self.getio = GetIO()
        self.createio = CreateIO()
        self.updateio = UpdateIO(self.createio, self.getio)

    """ EMPLOYEES """
    def get_list_of_all_employees(self):
        """ Calls the class get to get a list of all employees """
        return self.getio.load_all_employees()

    def get_list_of_all_pilots(self):
        """ Calls the class get to get a list of all pilots """
        return self.getio.load_all_pilots()

    def get_list_of_all_cabin_crew(self):
        """ Calls the class to get a list of the whole cabin crew """
        return self.getio.load_all_cabincrew()
    
    def create_pilot(self, new_pilot):
        
        return self.createio.store_pilot(new_pilot)
    
    def update_pilot(self, updated_pilot):
        
        return self.updateio.update_pilot(updated_pilot)

    def create_cabincrew(self, new_cabincrew):

        return self.createio.store_cabincrew(new_cabincrew)

    def update_cabincrew(self, updated_cabincrew_ob):

        return self.updateio.update_cabincrew(updated_cabincrew_ob)

    """ DESTINATIONS """

    def get_destination_list(self):
        """ Calls the get class to get a list of all destinations """
        return self.getio.load_all_destinations()
    
    def create_destination(self, new_destination):
        return self.createio.store_destination(new_destination)
    
    def update_emergency_contact(self, updated_contact):  
        return self.updateio.update_emergency_contact(updated_contact)


    """ AIRPLANES """

    def get_airplane_list(self):
        """ Calls the get class to get a list of all airplanes """
        return self.getio.load_all_airplanes()
         
    def create_airplane(self, new_airplane):
        return self.createio.store_airplane(new_airplane)


    """ VOYAGES """

    def get_all_voyages_list(self):
        """ Calls the Get class to get a list of all voyagess """
        return self.getio.load_all_voyages()

    def get_all_flights_list(self):
        return self.getio.load_all_flights()

    def update_voyage(self, voyage_ob):
        return self.updateio.update_voyage(voyage_ob)
        
    def create_voyage(self, new_voyage):
        return self.createio.store_voyage(new_voyage)
    
    