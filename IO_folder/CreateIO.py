from IO_folder.GetIO import GetIO
from models.CabinCrewModel import CabinCrewModel
from models.PilotModel import PilotsModel
from models.AirplanesModel import AirplanesModel
import csv

class CreateIO():
    def __init__(self):
        pass
    
    def add_pilot(self, new_pilot):
        with open(r'Pilots.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_pilot.to_csv_string())

    def add_cabincrew(self):

        
    def add_airplane(self):


    def add_destiantions(self):
        pass

    def add_voyage(self):
        pass
