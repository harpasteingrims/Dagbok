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

    def calculate_outbound_arrival_time(self, new_voyage_object):
        
        arrival_time = ""
        departure_time = new_voyage_object.departure_time
        parsed_departure_time = dateutil.parser.parse(departure_time)

        destination_list = self.ioapi.get_destination_list()

        for destination_ob in destination_list:
            if new_voyage_object.destination == destination_ob.airport:
                distance = destination_ob.flight_dur_from_Ice
                hours = distance[:2]
                minutes = distance[3:]
                arrival_time = (parsed_departure_time + timedelta(hours=int(hours),minutes=int(minutes))).isoformat()
        new_voyage_object.arrival_time = arrival_time

        return new_voyage_object

    def calculate_flight_num(self, new_voyage_object): #Þetta þarf að reikna bæði outbound flight num og return flight num
        outbound_flight_num = "NA"
        return_flight_num = "NA"
        destination_list = self.ioapi.get_destination_list()

        for destination_ob in destination_list:
            if new_voyage_object.destination == destination_ob.airport:
                dest_ID = str(destination_ob.destiID)
        outbound_flight_num = outbound_flight_num + dest_ID
        return_flight_num = return_flight_num + dest_ID
        voyage_list = self.list_all_voyages()
        highest_number = 0
        for voyage_ob in voyage_list:
            if new_voyage_object.departure_time[0:9] == voyage_ob.departure_time[0:9] and new_voyage_object.destination == voyage_ob.destination:
                
                if int(voyage_ob.return_flight_num[-1]) > highest_number:
                    highest_number = int(voyage_ob.return_flight_num[-1])
        highest_number += 1
        outbound_flight_num = outbound_flight_num + str(highest_number)
        highest_number = int(highest_number)
        highest_number += 1
        return_flight_num = return_flight_num + str(highest_number)
        new_voyage_object.outbound_flight_num = outbound_flight_num
        new_voyage_object.return_flight_num = return_flight_num

        return new_voyage_object


    def calculate_return_departure_time(self, new_voyage_object): #Þetta þarf að reikna return departure time, sem er einni klst meira en arrival_time
        return_departure_time = ""
        arrival_time = new_voyage_object.arrival_time
        parsed_arrival_time = dateutil.parser.parse(arrival_time)

        return_departure_time = (parsed_arrival_time + timedelta(hours = 1, minutes = 0)).isoformat()
        new_voyage_object.return_departure_time = return_departure_time

        return new_voyage_object

    def calculate_return_arrival_time(self, new_voyage_object): #Þetta þarf að reikna return arrival time sem er svipað og hitt fallið
        return_arrival_time = ""
        return_departure_time = new_voyage_object.return_departure_time
        parsed_return_departure_time = dateutil.parser.parse(return_departure_time)

        destination_list = self.ioapi.get_destination_list()

        for destination_ob in destination_list:
            if new_voyage_object.destination == destination_ob.airport:
                distance = destination_ob.flight_dur_from_Ice
                hours = distance[:2]
                minutes = distance[3:]
                return_arrival_time = (parsed_return_departure_time + timedelta(hours=int(hours),minutes=int(minutes))).isoformat()
        new_voyage_object.return_arrival_time = return_arrival_time

        return new_voyage_object
    