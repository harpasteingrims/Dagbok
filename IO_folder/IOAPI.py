from IO_folder.CreateIO import CreateIO
from IO_folder.GetIO import GetIO
from UI_folder.updateIO import UpdateIO

class IOAPI():
    def __init__(self):
        self.get = GetIO()
        self.create = CreateIO()
        self.update = UpdateIO()

    """ EMPLOYEES """

    def get_list_of_all_employees(self):
       
        return self.get.get_all_employees()
        
    def get_list_of_all_pilots(self):


        return self.get.get_all_pilots()

    def get_list_of_all_cabin_crew(self):
         
        return self.get_cabincrew()
    
    def create_pilot(self):

        return self.create.add_pilot()

    def create_cabincrew(self):
        
        return self.create.add_cabincrew()


    """ DESTINATIONS """

    def get_destination_list(self):
        """ Calls the get class to get a list of all destinations """
        return self.create.get_all_destinations()
    
    def create_destination(self):
        return self.create.add_destiantions()


    """ AIRPLAINS """

    def get_airplane_list(self):
        """ Calls the Get class to get a list of all airplanes """
        return self.get.get_all_airplanes()
         
    def create_airlane(self):
        return self.create.add_airplane()


    """ VOYAGES """

    def get_voyages(self):
        #voyages_listget_voyages
        pass
    def create_voyage(self):
        return self.create.add_voyage()