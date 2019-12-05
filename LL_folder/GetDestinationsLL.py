class GetDestinationsLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        
    def get_all_destinations(self):
        """ Calls the IOAPI to get a list of all airplanes """
        return sorted(self.ioapi.get_destination_list()) 