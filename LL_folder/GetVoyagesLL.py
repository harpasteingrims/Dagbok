import datetime
import dateutil.parser
from models.VoyagesModel import VoyagesModel
class GetVoyagesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        self.voyages_list = []

    def list_all_voyages(self):
        flights_list = self.ioapi.get_all_voyages_list()
        return flights_list

    def list_not_staffed_voyages(self):
        voyages_list = self.ioapi.get_all_voyages_list()
        unmanned_list = []
        for voyage_ob in voyages_list:
            if voyage_ob.captain == "":
                unmanned_list.append(voyage_ob)
        
        return unmanned_list

    def list_all_common_voyages_dict(self):
        voyages_list = self.ioapi.get_all_voyages_list()
        counter = 0
        common_voyages_list = []
        for voyage_ob in voyages_list:
            destination = voyage_ob.arriving_at
            parsed_date = dateutil.parser.parse(voyage_ob.departure_time)
            for voyage_object in voyages_list:
                parsed_date_voyage = dateutil.parser.parse(voyage_object.departure_time)
                if [voyage_object.arriving_at, parsed_date_voyage.hour, parsed_date_voyage.minute] == [destination, parsed_date.hour, parsed_date.minute]:
                    counter += 1
            if counter > 2:
                departure_time = parsed_date.hour + ":" + parsed_date.minute + ":00"
                common_voyages_list.append([destination, departure_time])
            counter = 0

        return common_voyages_list

    def list_unavailable_voyage_time(self, voyage_year, voyage_month, voyage_day):
        voyages_list = self.ioapi.get_all_voyages_list()
        unavailable_voyage_time_list = []
        for voyage_ob in voyages_list:
            date = voyage_ob.date
            parsed_date = dateutil.parser.parse(date)
            if voyage_year == parsed_date.year and voyage_month == parsed_date.month and voyage_day == parsed_date.day:
                time_str = parsed_date.hour + ":" + parsed_date.minute + ":00"
                unavailable_voyage_time_list.append(time_str)
        
        return unavailable_voyage_time_list

        