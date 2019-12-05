class GetAirplanesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_all_airplanes(self):
        """ Calls the IOAPI to get a list of all airplanes """
        return sorted(self.ioapi.get_airplane_list())

    def list_available_airplanes_by_date(self, voyage_date):
        pass

    #searched_pilot_info = []

        #pilot_list = self.get_all_pilots()

        #for pilot in self.pilot_list:
            #if pilot.name == name:
                # TODO handle if found
            #    pass
        # TODO handle if none is found
