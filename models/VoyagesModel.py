import datetime
from datetime import timedelta
import dateutil.parser
class VoyagesModel():
    def __init__(self, departure_time, destination, aircraftID, arrival_time = "", crew_list = [], outbound_flight_num = "", return_flight_num = "", return_departure_time = "", return_arrival_time = "", departure_dest = "Keflavik"):
        self.departure_time = departure_time
        self.destination = destination
        self.aircraftID = aircraftID
        self.arrival_time = arrival_time
        self.crew_list = crew_list
        self.outbound_flight_num = outbound_flight_num
        self.return_flight_num = return_flight_num
        self.return_departure_time = return_departure_time
        self.return_arrival_time = return_arrival_time
        self.departure_dest = departure_dest
 
    def print_voy_out(self, counter):
        return f"\n{counter} {self.departure_time}, {self.destination}, {self.aircraftID}"
    
    def print_schedule(self, counter):
        departure_time = dateutil.parser.parse(self.departure_time)
        arrival_time = dateutil.parser.parse(self.arrival_time)

        if len(self.crew_list) == 5:

            return f"\n{counter} {self.destination}: {departure_time.day}/{departure_time.month}/{departure_time.year} - {arrival_time.day}/{arrival_time.month}/{arrival_time.year}, fully staffed"

        else:
            return f"\n{counter} {self.destination}: {departure_time.day}/{departure_time.month}/{departure_time.year} - {arrival_time.day}/{arrival_time.month}/ {arrival_time.year}, not fully staffed"