import datetime
import dateutil.parser
from datetime import timedelta
from datetime import datetime
from models.VoyagesModel import VoyagesModel
class GetVoyagesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        self.voyages_list = []

    def list_all_voyages(self):
        return self.ioapi.get_all_voyages_list()

    def list_all_voyages_overview(self):
        voyages_list = self.list_all_voyages()
        flights_list = self.ioapi.get_all_flights_list()
        all_voyage_list = []
        now = datetime.now()
        date_time_now = now.strftime("%Y-%m-%dT%H:%M:%S")
        i = 0
        for voyage_ob in voyages_list:
            if voyage_ob.departure_time == flights_list[i].departure_time:
                if date_time_now < flights_list[i].departure_time:
                    flight_status = "Not started"
                elif flights_list[i].departure_time <= date_time_now <= flights_list[i].arrival_time:
                    flight_status = "In the air"
                elif flights_list[i+1].departure_time <= date_time_now <= flights_list[i+1].arrival_time:
                    flight_status = "In the air"
                elif flights_list[i].departure_time < date_time_now:
                    flight_status = "Finished"
                else:
                    flight_status = "Has landed at destination"

                departure_time = dateutil.parser.parse(voyage_ob.departure_time)
                arrival_time = dateutil.parser.parse(voyage_ob.arrival_time)

                departure_time_str = str(departure_time.year) + "/" + str(departure_time.month) + "/" + str(departure_time.day) + " " + str(departure_time.hour) + ":" + str(departure_time.minute) + ":00"
                arrival_time_str = str(arrival_time.year) + "/" + str(arrival_time.month) + "/" + str(arrival_time.day) + " " + str(arrival_time.hour) + ":" + str(arrival_time.minute) + ":00"

                all_voyage_list.append([departure_time_str, arrival_time_str, voyage_ob.destination, voyage_ob.aircraftID, flights_list[i].flight_number, flights_list[i+1].flight_number, flight_status])

            i += 2
        return all_voyage_list

    def list_not_staffed_voyages(self):

        voyages_list = self.list_all_voyages()
        unmanned_list = []
        for voyage_ob in voyages_list:
            if voyage_ob.crew_list == []:
                unmanned_list.append(voyage_ob)
        
        return unmanned_list

    def list_all_common_voyages(self):

        voyages_list = self.list_all_voyages()
        counter = 0
        common_voyages_list = []
        for voyage_ob in voyages_list:
            destination = voyage_ob.destination
            parsed_date = dateutil.parser.parse(voyage_ob.departure_time)
            for voyage_object in voyages_list:
                parsed_date_voyage = dateutil.parser.parse(voyage_object.departure_time)
                if [voyage_object.destination, parsed_date_voyage.hour, parsed_date_voyage.minute] == [destination, parsed_date.hour, parsed_date.minute]:
                    counter += 1
            if counter > 1:
                departure_time = str(parsed_date.hour) + ":" + str(parsed_date.minute) + ":00"
                if [destination, departure_time] not in common_voyages_list:
                    common_voyages_list.append([destination, departure_time])
            counter = 0

        return common_voyages_list

    def list_unavailable_voyage_time(self, voyage_year, voyage_month, voyage_day):

        voyages_list = self.list_all_voyages()
        unavailable_voyage_time_list = []
        for voyage_ob in voyages_list:
            parsed_date = dateutil.parser.parse(voyage_ob.departure_time)
            if int(voyage_year) == parsed_date.year and int(voyage_month) == parsed_date.month and int(voyage_day) == parsed_date.day:
                unavailable_voyage_time_list.append(voyage_ob)
        
        return unavailable_voyage_time_list

    def list_schedule_employee_by_date(self, employee_ob, date_from, date_to):
        voyages_list = self.list_all_voyages()
        
        all_flights_of_employee = []
        
        for voyage_ob in voyages_list:
            if employee_ob.ssn in voyage_ob.crew_list:
                all_flights_of_employee.append(voyage_ob)

        flights_on_asked_time = []
        for voyage_ob in all_flights_of_employee:
            if date_from <= voyage_ob.departure_time <= date_to:
                flights_on_asked_time.append(voyage_ob)

        
        return flights_on_asked_time

    def calculate_arrival_time(self, new_voyage_object):
        departure_time = new_voyage_object.departure_time
        if new_voyage_object.destination == "Longyearbyean":
            new_voyage_object.arrival_time = datetime.datetime.strptime(departure_time) + timedelta(hours=2,minutes=47)
        elif new_voyage_object.destination == "Nuuk":
            new_voyage_object.arrival_time = datetime.datetime.strptime(departure_time) + timedelta(hours=2,minutes=7)
        elif new_voyage_object.destination == "Kulusuk":
            new_voyage_object.arrival_time = datetime.datetime.strptime(departure_time) + timedelta(hours=1,minutes=29)
        elif new_voyage_object.destination == "Thorshavn":
           new_voyage_object.arrival_time = datetime.datetime.strptime(departure_time) + timedelta(hours=1,minutes=34)
        elif new_voyage_object.destination == "Tingwall":
            new_voyage_object.arrival_time = datetime.datetime.strptime(departure_time) + timedelta(hours=5,minutes=47)

        return new_voyage_object
        
    