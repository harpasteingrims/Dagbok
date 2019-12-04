class IOAPI():
    def __init__(self):
        self.airplanes = GetAirplanesLL()
        self.employees = GetEmployeesLL()
        self.destination = GetDestinationsLL()
        self.voyages = GetVoyagesLL()
        self.create_ll = CreateLL()
        self.update_LL = UpdateLL()

    """ AIRPLAINS """
    def get_airplane_list(self):
        return self.airplanes.make_list_of_airplanes()

    """ EMPLOYEES """
    def get_list_of_all_employees(self):
        return self.employees.get_all_employees()
    
    def get_list_of_all_pilots(self):
        get_all_pilots

    """ DESTINATIONS """
    def get_destination_list(self):
        return self.destination.get_all_destinations()