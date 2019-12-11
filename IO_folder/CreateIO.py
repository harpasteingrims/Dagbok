import sys
sys.path.insert(1, '~/')
import csv
from models.CabinCrewModel import CabinCrewModel
from models.PilotsModel import PilotsModel
from models.AirplanesModel import AirplanesModel
from models.VoyagesModel import VoyagesModel
from models.DestinationsModel import DestinationsModel

class CreateIO():
    def store_pilot(self, new_pilot):
        with open('./csv_files/Pilots.csv', 'a') as f:
            f.write(new_pilot.to_csv_string())

    def store_cabincrew(self, new_cabincrew):
        with open('./csv_files/CabinCrew.csv', 'a') as f:
            f.write(new_cabincrew.to_csv_string())
        
    def store_airplane(self, new_airplane):
        with open('./csv_files/Aircraft.csv', 'a') as f:
            f.write(new_airplane.to_csv_string())

    def store_destination(self, new_destination):
        with open('./csv_files/Destinations.csv', 'a') as f:
            f.write(new_destination.to_csv_string())

    def store_voyage(self, new_voyage):
        with open('./csv_files/Flights.csv', 'a') as f:
            f.write(new_voyage.to_csv_string())


