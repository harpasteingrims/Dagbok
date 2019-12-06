from IO_folder.CreateIO import CreateIO
from IO_folder.GetIO import GetIO
from IO_folder.UpdateIO import UpdateIO

class IOAPI():
    def __init__(self):
        self.get = GetIO()
        self.create = CreateIO(self.get)
        self.update = UpdateIO(self.get)

    """ EMPLOYEES """
    def get_list_of_all_employees():
        """ Calls the class get to get a list of all employees """
        employees = GetIO.load_all_employees()
        print(employees)
        return employees

    def get_list_of_all_pilots(self):
        """ Calls the class get to get a list of all pilots """
        return self.get.load_all_pilots()

    def get_list_of_all_cabin_crew(self):
        """ Calls the class to get a list of the whole cabin crew """
        return self.get.load_all_cabincrew()
    
    def create_pilot(self):
        
        return self.create.add_pilot()

    def create_cabincrew(self):

        return self.create.add_cabincrew()


    """ DESTINATIONS """

    def get_destination_list(self):
        """ Calls the get class to get a list of all destinations """
        return self.get.load_all_destinations()
    
    def create_destination(self):
        return self.create.add_destiantions()


    """ AIRPLAINS """

    def get_airplane_list(self):
        """ Calls the Get class to get a list of all airplanes """
        return self.get.load_all_airplanes()
         
    def create_airlane(self):
        return self.create.add_airplane()


    """ VOYAGES """

    def get_all_voyages_list(self):
        """ Calls the Get class to get a list of all voyagess """
        return self.get.load_all_voyages()
        
        
    def create_voyage(self):
        return self.create.add_voyage()