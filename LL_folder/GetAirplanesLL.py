class GetAirplanesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def get_all_airplanes(self):
        self.ioapi.get_airplane_list()