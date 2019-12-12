import sys
sys.path.insert(1, '~/')
import csv
from models.CabinCrewModel import CabinCrewModel
from models.PilotsModel import PilotsModel
from models.AirplanesModel import AirplanesModel
from models.VoyagesModel import VoyagesModel
from models.DestinationsModel import DestinationsModel
import os

class CreateIO():
    def store_pilot(self, new_pilot):
        with open('./csv_files/Pilots.csv', 'a', newline = " ") as openfile:
            fieldnames = ["ssn", "name", "role", "rank", "plane license", "address", "mobile_number", "email"]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"ssn": new_pilot.ssn,"name": new_pilot.name,"role": new_pilot.role,"rank": new_pilot.rank,"plane license": new_pilot.license_type,"address": new_pilot.address,"mobile_number": new_pilot.mobile_number,"email": new_pilot.email})

    def store_cabincrew(self, new_cabincrew):
        with open('./csv_files/CabinCrew.csv', 'a', newline = " ") as openfile:
            fieldnames = ["ssn", "name", "role", "rank", "address", "mobile number", "email"]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"ssn": new_cabincrew.ssn, "name": new_cabincrew.name, "role": new_cabincrew.role, "rank": new_cabincrew.rank, "address": new_cabincrew.address, "mobile number": new_cabincrew.mobile_number, "email": new_cabincrew.email})

        
    def store_airplane(self, new_airplane):
        with open('./csv_files/Aircraft.csv', 'a', newline = " ") as openfile:
            fieldnames = ["planeID", "airplane_type", "manufacturer", "seat_amount"]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"planeID": new_airplane.planeID, "airplane_type": new_airplane.airplane_type, "manufacturer": new_airplane.manufacturer, "seat_amount": new_airplane.seat_amount})

    def store_destination(self, new_destination):
        with open('./csv_files/Destinations.csv', 'a', newline = " ") as openfile:
            fieldnames = ["country" ,"airport" ,"manufacturer" ,"flight_dur_from_Ice" ,"dist_from_Ice" ,"contact_name, contact_phone_number" ,"destiID" ]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"country": new_destination.country, "airport": new_destination.airport, "flight_dur_from_Ice": new_destination.flight_dur_from_Ice, "dist_from_Ice": new_destination.dist_from_Ice,"contact_name": new_destination.contact_name,"contact_phone_number": new_destination.contact_phone_number, "destiID": new_destination.destiID})

    def store_voyage(self, outbound_flight, return_flight):
        with open('./csv_files/Flights.csv', 'a', newline = " ") as openfile:
            fieldnames = ["outbound_flight_num" ,"departure_dest" ,"destination" ,"departure_time" ,"arrival_time" ,"aircraftID" ,"\nreturn_flight_num" ,"destination","departure_dest", "return_departure_time","return_arrival_time","aircraftID" ]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"outbound_flight_num": outbound_flight.outbound_flight_num, "departure_dest": outbound_flight.departure_dest, "destination": outbound_flight.destination,"departure_time" : outbound_flight.departure_time, "arrival_time": outbound_flight.arrival_time,"aircraftID": outbound_flight.aircraftID,"\nreturn_flight_num": return_flight.return_flight_num, "destination": return_flight.destination, "departure_dest": return_flight.departure_dest, "return_departure_time": return_flight.return_departure_time, "return_arrival_time": return_flight.return_arrival_time, "aircraftID" : return_flight.aircraftID})

            #{self.outbound_flight_num}, {self.departure_dest}, {self.destination}, {self.departure_time}, {self.arrival_time}, {self.aircraftID}"
            #{self.return_flight_num}, {self.destination}, {self.departure_dest}, {self.return_departure_time}, {self.return_arrival_time}, {self.aircraftID}"
 