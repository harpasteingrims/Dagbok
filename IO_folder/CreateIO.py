import csv
from models.CabinCrewModel import CabinCrewModel
from models.PilotsModel import PilotsModel
from models.AirplanesModel import AirplanesModel
from models.VoyagesModel import VoyagesModel
from models.DestinationsModel import DestinationsModel
import os

class CreateIO():
    def store_pilot(self, new_pilot):
        """ takes pilot object and writes it in pilots.csv"""

        with open('./csv_files/Pilots.csv', 'a', newline = "") as openfile:
            fieldnames = ["ssn", "name", "role", "rank", "plane license", "address", "mobile_number", "email"]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"ssn": new_pilot.ssn,"name": " " + new_pilot.name,"role": " " + new_pilot.role,"rank": " " + new_pilot.rank, "plane license": " " + new_pilot.license_type, "address": " " + new_pilot.address, "mobile_number": " " + new_pilot.mobile_number,"email": " " + new_pilot.email})

    def store_cabincrew(self, new_cabincrew):
        """ takes cabincrew object and writes it in CabinCrew.csv"""

        with open('./csv_files/CabinCrew.csv', 'a', newline = "") as openfile:
            fieldnames = ["ssn", "name", "role", "rank", "address", "mobile number", "email"]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"ssn": new_cabincrew.ssn, "name": " " + new_cabincrew.name, "role": " " + new_cabincrew.role, "rank": " " + new_cabincrew.rank, "address": " " + new_cabincrew.address, "mobile number": " " + new_cabincrew.mobile_number, "email": " " + new_cabincrew.email})
        
    def store_airplane(self, new_airplane):
        """ takes airplane object and writes it in Aircraft.csv"""

        with open('./csv_files/Aircraft.csv', 'a', newline = "") as openfile:
            fieldnames = ["planeID", "airplane_type", "manufacturer", "seat_amount"]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"planeID": new_airplane.planeID, "airplane_type": " " + new_airplane.airplane_type, "manufacturer": " " + new_airplane.manufacturer, "seat_amount": " " + new_airplane.seat_amount})

    def store_destination(self, new_destination):
        """ takes destination object and writes it in Destinations.csv"""

        with open('./csv_files/Destinations.csv', 'a', newline = "") as openfile:
            fieldnames = ["country", "airport", "flight_dur_from_Ice", "dist_from_Ice", "contact_name", "contact_phone_number", "destiID"]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"country": new_destination.country, "airport": " " + new_destination.airport, "flight_dur_from_Ice": " " + new_destination.flight_dur_from_Ice, "dist_from_Ice": " " + new_destination.dist_from_Ice,"contact_name": " " + new_destination.contact_name,"contact_phone_number": " " + new_destination.contact_phone_number, "destiID": " " + new_destination.destiID})

    def store_voyage(self, new_voyage):
        """ takes voyage object and writes it in Flights.csv with and without crew"""

        with open('./csv_files/Flights.csv', 'a', newline = "") as openfile:
            if new_voyage.crew_list == []:
                fieldnames = ["flight_num","departure_dest","destination","departure_time","arrival_time","aircraftID"]
                writer = csv.DictWriter(openfile, fieldnames = fieldnames)
                writer.writerow({"flight_num": new_voyage.outbound_flight_num, "departure_dest": " " + new_voyage.departure_dest, "destination": " " + new_voyage.destination,"departure_time" : " " + new_voyage.departure_time, "arrival_time": " " + new_voyage.arrival_time,"aircraftID": " " + new_voyage.aircraftID})
                writer.writerow({"flight_num": new_voyage.return_flight_num, "departure_dest": " " + new_voyage.destination, "destination": " " + new_voyage.departure_dest, "departure_time": " " + new_voyage.return_departure_time, "arrival_time": " " + new_voyage.return_arrival_time, "aircraftID" : " " + new_voyage.aircraftID})
            else:
                fieldnames = ["flight_num","departure_dest","destination","departure_time","arrival_time","aircraftID","captain","copilot","fsm","fa1","fa2"]
                writer = csv.DictWriter(openfile, fieldnames = fieldnames)
                writer.writerow({"flight_num": new_voyage.outbound_flight_num, "departure_dest": " " + new_voyage.departure_dest, "destination": " " + new_voyage.destination,"departure_time" : " " + new_voyage.departure_time, "arrival_time": " " + new_voyage.arrival_time, "aircraftID": " " + new_voyage.aircraftID, "captain": " " + (new_voyage.crew_list[0]), "copilot": " " + (new_voyage.crew_list[1]), "fsm": " " + (new_voyage.crew_list)[2], "fa1": " " + (new_voyage.crew_list)[3], "fa2": " " + (new_voyage.crew_list)[4]})
                writer.writerow({"flight_num": new_voyage.return_flight_num, "departure_dest": " " + new_voyage.destination, "destination": " " + new_voyage.departure_dest, "departure_time": " " + new_voyage.return_departure_time, "arrival_time": " " + new_voyage.return_arrival_time, "aircraftID" : " " + new_voyage.aircraftID, "captain": " " + (new_voyage.crew_list[0]), "copilot": " " + (new_voyage.crew_list[1]), "fsm": " " + (new_voyage.crew_list)[2], "fa1": " " + (new_voyage.crew_list)[3], "fa2": " " + (new_voyage.crew_list)[4]})

    def store_voyage_with_crew(self, new_voyage):
        """ takes voyage object and writes it in Flights.csv with crew"""

        with open('./csv_files/Flights.csv', 'a', newline = "") as openfile:
            fieldnames = ["flight_num","departure_dest","destination","departure_time","arrival_time","aircraftID","captain","copilot","fsm","fa1","fa2"]
            writer = csv.DictWriter(openfile, fieldnames = fieldnames)
            writer.writerow({"flight_num": new_voyage.outbound_flight_num, "departure_dest": " " + new_voyage.departure_dest, "destination": " " + new_voyage.destination,"departure_time" : " " + new_voyage.departure_time, "arrival_time": " " + new_voyage.arrival_time, "aircraftID": " " + new_voyage.aircraftID, "captain": " " + new_voyage.crew_list[0], "copilot": " " + new_voyage.crew_list[1], "fsm": " " + new_voyage.crew_list[2], "fa1": " " + new_voyage.crew_list[3], "fa2": " " + new_voyage.crew_list[4]})
            writer.writerow({"flight_num": new_voyage.return_flight_num, "departure_dest": " " + new_voyage.destination, "destination": " " + new_voyage.departure_dest, "departure_time": " " + new_voyage.return_departure_time, "arrival_time": " " + new_voyage.return_arrival_time, "aircraftID" : " " + new_voyage.aircraftID, "captain": " " + new_voyage.crew_list[0], "copilot": " " + new_voyage.crew_list[1], "fsm": " " + new_voyage.crew_list[2], "fa1": " " + new_voyage.crew_list[3], "fa2": " " + new_voyage.crew_list[4]})