import dateutil.parser

class GetVoyagesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_all_voyages(self):
        return self.ioapi.get_all_voyages_list()

    def list_not_staffed_voyages(self):
        voyages_list = self.ioapi.get_all_voyages_list()
        unmanned_list = []
        for voyage in voyages_list:
            #if len(voyage) < 6:
            if voyage.captain not in voyage:
                unmanned_list.append(voyage)
        
        return unmanned_list

    def list_all_common_voyages(self):
        pass

    def list_unavailable_voyage_time(self, voyage_year, voyage_month, voyage_day):
        voyages_list = self.ioapi.get_all_voyages_list
        unavailable_voyage_time_list = []
        for voyage_ob in voyages_list:
            date = voyage_ob.date
            parsed_date = dateutil.parser.parse(date)
            if voyage_year == parsed_date.year and voyage_month == parsed_date.month and voyage_day == parsed_date.day:
                time_str = parsed_date.hour + ":" + parsed_date.minute + ":00"
                unavailable_voyage_time_list.append(time_str)
        
        return unavailable_voyage_time_list

        