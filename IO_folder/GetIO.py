import csv
import sys
sys.path.insert(0, 'Documents\VERKLEGT-1-verkefni\models') #Vorum að prufa þetta til að ná að importa models en þetta virkar ekki

from models.CabinCrewModel import CabinCrewModel
from models.AirplanesModel import AirplanesModel
from models.DestinationsModel import DestinationsModel
from models.PilotModel import PilotsModel
from models.VoyagesModel import VoyagesModel
from models.Voyage_crewModel import Voyage_crewModel


class GetIO():
    def __init__(self):
        self.all_employee_list = []
        self.pilot_list = []
        self.cabincrew_list = []
        self.airplane_list = []
        self.destination_list = []
        self.voyages_list = []

    def load_all_employees(self):

        self.pilot_list = self.load_all_pilots()
        self.cabincrew_list = self.load_all_cabincrew()

        self.all_employee_list.extend(self.cabincrew_list)
        self.all_employee_list.extend(self.pilot_list)
        

        return sorted(self.all_employee_list)

    def load_all_pilots(self):
        pilot_file = open("csv_files\Pilots.csv","r")
        line = pilot_file.readlines()
        
        counter = 1
        for line in pilot_file:
            if counter == 1:
                counter += 1
            else:
                SSN = line[0]
                name = line[1]
                role = line[2]
                rank = line[3]
                plane_license = line[4]
                address = line[5]
                mobile_number = line[6]
                email = line[7]
                SSN, name, role, rank, plane_license, address, mobile_number, email = line.split(",")
                pilot = PilotsModel(SSN, name, role, rank, plane_license, address, mobile_number, email)
                self.pilot_list.append(pilot)
        print(self.pilot_list)

        pilot_file.close()
        
        
        return self.pilot_list

    def load_all_cabincrew(self):
        crew_file = open("csv_files\CabinCrew.csv","r")
        
        counter = 1
        for line in crew_file:
            if counter == 1:
                counter += 1
            else:
                SSN = line[0]
                name = line[1]
                role = line[2]
                rank = line[3]
                address = line[4]
                mobile_number = line[5]
                email = line[6]
                SSN, name, role, rank, address, mobile_number, email = line.split(",")
                
                cabincrew_employee = CabinCrewModel(SSN, name, role, rank, address, mobile_number, email)
                self.cabincrew_list.append(cabincrew_employee)
        crew_file.close()

        return self.cabincrew_list
        
    def load_all_airplanes(self):
        '''Retrieves airplanes and sends to Get LL'''
        airplane_file = open("csv_files\Aircraft.csv", "r")

        counter = 1
        for line in airplane_file:
            if counter == 1:
                counter += 1
            else:
                planeID = line[0]
                airplane_type = line[1]
                manufacturer = line[2]
                seat_amount = line[3]
                planeID, airplane_type, manufacturer, seat_amount = line.split(",")
                airplane = AirplanesModel(planeID, airplane_type, manufacturer, seat_amount)
                self.airplane_list.append(airplane)

        airplane_file.close()

        return self.airplane_list

    def load_all_destinations(self):
        dest_file = open("csv_files\Destinations.csv", "r")

        counter = 1
        for line in dest_file:
            if counter == 1:
                counter += 1
            else:
                country = line[0]
                airport = line[1]
                flight_dur_from_Ice = line[2]
                dist_from_Ice = line[3]
                contact_name = line[4]
                contact_phone_number = line[5]
                country, airport, flight_dur_from_Ice, dist_from_Ice, contact_name, contact_phone_number = line.split(",")
                destination = DestinationsModel(country ,airport ,flight_dur_from_Ice ,dist_from_Ice ,contact_name ,contact_phone_number)
                self.destination_list.append(destination)
                
        dest_file.close()

        dest_file.close()

        return self.destination_list  
    
    def load_all_voyages(self):
        voyages_file = open("csv_files\Voyages.csv","r")

        counter = 1
        for line in voyages_file:
            if counter == 1:
                counter +=1
            else:
                date = line[0]
                time = line[1]
                destination = line[2]
                airplaneID = line[3]
                date, time, destination, airplaneID = line.split(",")
        
                voyages = VoyagesModel(date, time, destination, airplaneID)
                self.voyages_list.append(voyages)

        voyages_file.close()

        return self.voyages_list


    def load_all_voyages_with_crew(self):
        voyages_file = open("csv_files\Voyages.csv","r")

        counter = 1
        for line in voyages_file:
            if counter == 1:
                counter +=1
            else:
                date = line[0]
                time = line[1]
                destination = line[2]
                airplaneID = line[3]
                captain = line[4]
                copilot = line[5]
                fsm = line[6]
                fa1 = line[7]
                fa2 = line[8]
                date, time, destination, airplaneID = line.split(",")
                voyage = VoyagesModel(date, time, destination, airplaneID)
                voyage_with_crew = Voyage_crewModel(voyage,captain,copilot,fsm,fa1,fa2)
                
                self.voyages_list.append()

        voyages_file.close()

        return self.voyages_list
