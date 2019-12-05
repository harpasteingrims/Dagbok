class GetDestinationsLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        
    def list_all_destinations(self):
        """ Calls the IOAPI to get a list of all destinations """
        return sorted(self.ioapi.get_destination_list())

        