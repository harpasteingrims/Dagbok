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
        with open('./csv_files/Pilots.csv', 'a', newline = "") as fileToOpen:
            fieldnames = ["ssn", "name", "role", "rank", "plane license", "address", "mobile number", "email"]
            writer = csv.DictWriter(fileToOpen, fieldnames = fieldnames)
            writer.writerow({"ssn": new_pilot.ssn, "name": new_pilot.name, "role": new_pilot.role, "rank": new_pilot.rank, "plane license": new_pilot.license_type, "address": new_pilot.address, "mobile number": new_pilot.mobile_number, "email": new_pilot.email})

    def store_cabincrew(self, new_cabincrew):
        with open('./csv_files/CabinCrew.csv', 'a', newline = None) as f:
            f.write(new_cabincrew.to_csv_string())
        
    def store_airplane(self, new_airplane):
        with open('./csv_files/Aircraft.csv', 'a', newline = None) as f:
            f.write(new_airplane.to_csv_string())

    def store_destination(self, new_destination):
        with open('./csv_files/Destinations.csv', 'a', newline = None) as f:
            f.write(new_destination.to_csv_string())

    def store_voyage(self, new_voyage):
        with open('./csv_files/Flights.csv', 'a', newline = None) as f:
            f.write(new_voyage.to_csv_string())


