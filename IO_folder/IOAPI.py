class IOAPI():
    def __init__(self):
        self.airplanes = GetAirplanes()
        self.employees = GetEmployees()
        self.destination = GetDestinations()
        self.voyages = GetVoyages()
        self.create_ll = CreateLL()
        self.update_LL = UpdateLL()

    """ AIRPLAINS """
    def get_airplane_list(self):
        self.airplanes.make_list_of_airplanes()

    def get_destination_list(self):
        #self.destination.
        pass