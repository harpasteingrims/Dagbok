class IOAPI():
    def __init__(self):
        self.getemployees = GetIO()
        self.getpilots = GetIO()
        self.getcabincrew = GetIO()
        self.getpilots = GetIO()
        self.create = CreateIO()
        self.update = UpdateIO()

    """ AIRPLAINS """
    def get_airplane_list(self):
        return self.get.get_pilots()

    """ EMPLOYEES """
    def get_list_of_all_employees(self):
        all_employee_list = self.getemployees.get_all_employees()
        return all_employee_list

    def get_list_of_all_pilots(self):
        return self.getpilots.get_all_pilots()

    """ DESTINATIONS """
    def get_destination_list(self):
        return self.destination.get_all_destinations()