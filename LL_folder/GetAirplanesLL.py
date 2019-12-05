class GetAirplanesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_all_airplanes(self):
        """ Calls the IOAPI to get a list of all airplanes """
        return sorted(self.ioapi.get_airplane_list())

    def list_available_airplanes_by_date(self, voyage_date):
        airplane_list = self.ioapi.get_airplane_list()
        voyage_list = self.ioapi.get_all_voyages_list()
        for time_object in voyage_list:
            airplane_list = []
            if time_object.time == voyage_date:
                pass #OMG þetta er alltof erfitt... Þarf ég að taka inn tímann hingað líka? Þarf ég að vita hvenær flugvélarnar eru almennt að lenda? Þarf ég að vita hvaða destination hann er að fara til upp á að flugvélin verði lent áður en hún þarf að fara aftur út? Hvernig geri ég þetta allt??
        pass

    #searched_pilot_info = []

        #pilot_list = self.get_all_pilots()

        #for pilot in self.pilot_list:
            #if pilot.name == name:
                # TODO handle if found
            #    pass
        # TODO handle if none is found
