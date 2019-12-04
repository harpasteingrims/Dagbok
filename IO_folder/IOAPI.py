from IO_folder.CreateIO import CreateIO
from IO_folder.getIO import GetIO
class IOAPI():
    def __init__(self):
        self.get = GetIO()
        self.create = CreateIO()
        self.update = UpdateIO()


    """ EMPLOYEES """

    def get_list_of_all_employees(self):
        all_employee_list = self.get.load_all_employees()
        return all_employee_list

    def get_list_of_all_pilots(self):
        pilot_list = self.get.load_all_pilots()
        return pilot_list

    def get_list_of_all_cabin_crew(self):
        airplane_list = self.get.load_all_airplanes()
        return airplane_list
    
    def create_pilot(self):
        return self.create.add_pilot()

    def create_cabincrew(self):
        return self.create.add_cabincrew()


    """ DESTINATIONS """

    def get_destination_list(self):
        return self.create.get_all_destinations()
    
    def create_destination(self):
        return self.create.add_destiantions()


    """ AIRPLAINS """

    def get_airplane_list(self):
         
        return
        
    def create_airlane(self):
        return self.create.add_airplane()


    """ VOYAGES """
    def create_voyage(self):
        return self.create.add_voyage()