class GetDestinationsLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        
    def list_all_destinations(self):
        """ Calls the IOAPI to get a list of all destinations """
        return self.ioapi.get_destination_list()

    def list_all_airports(self):
        destination_list = self.ioapi.get_destination_list()
        airport_list = []
        for destination_ob in destination_list:
            if destination_ob.airport != "Keflavik":
                airport_list.append(destination_ob.airport)
        return airport_list

        