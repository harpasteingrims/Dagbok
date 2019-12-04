class IOAPI():
    def __init__(self):
        self.get = GetIO()
        self.create = CreateIO()
        self.update = UpdateIO()

    """ AIRPLAINS """
    def get_airplane_list(self):
         
        return

    """ EMPLOYEES """
    def get_list_of_all_employees(self):
        all_employee_list = self.get.get_all_employees()
        return all_employee_list

    def get_list_of_all_pilots(self):
        pilot_list = self.get.get_all_pilots()
        return pilot_list

    def get_list_of_all_cabin_crew

    """ DESTINATIONS """
    def get_destination_list(self):
        return self.destination.get_all_destinations()