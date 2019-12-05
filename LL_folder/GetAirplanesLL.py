class GetAirplanesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_all_airplanes(self):
        """ Calls the IOAPI to get a list of all airplanes """
        return sorted(self.ioapi.get_airplane_list())

    def list_available_airplanes_by_date(self):
        pass