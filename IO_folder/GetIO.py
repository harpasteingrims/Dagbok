import csv
import sys
sys.path.insert(0, 'VERKLEGT-1-verkefni/models') #Vorum að prufa þetta til að ná að importa models en þetta virkar ekki

from models.CabinCrewModel import CabinCrewModel
from models.AirplanesModel import AirplanesModel
from models.DestinationsModel import DestinationsModel
from models.PilotModel import PilotsModel
from models.VoyagesModel import VoyagesModel
from models.FlightsModel import FlightsModel

class GetIO():
    def __init__(self):
        self.all_employee_list = []
        self.pilot_list = []
        self.cabincrew_list = []
        self.airplane_list = []
        self.destination_list = []
        self.voyages_list = []

    def load_all_employees(self):

        pilot_list = self.load_all_pilots()
        cabincrew_list = self.load_all_cabincrew()

        self.all_employee_list.extend(cabincrew_list)
        self.all_employee_list.extend(pilot_list)

        return self.all_employee_list

    def load_all_pilots(self):
        pilot_file = open("./csv_files/Pilots.csv","r")
        
        counter = 1
        for line in pilot_file:
            if counter == 1:
                counter += 1
            else:
                ssn = line[0]
                name = line[1]
                role = line[2]
                rank = line[3]
                plane_license = line[4]
                address = line[5]
                mobile_number = line[6]
                email = line[7]
                ssn, name, role , rank, license_type, address, mobile_number, email = line.split(",")
                pilot = PilotsModel(ssn, name, role , rank, license_type, address, mobile_number, email)
                self.pilot_list.append(pilot)
        

        pilot_file.close()
        
        return self.pilot_list

    def load_all_cabincrew(self):
        crew_file = open("./csv_files/CabinCrew.csv","r")
        
        counter = 1
        for line in crew_file:
            if counter == 1:
                counter += 1
            else:
                ssn = line[0]
                name = line[1]
                role = line[2]
                rank = line[3]
                address = line[4]
                mobile_number = line[5]
                email = line[6]
                ssn, name, role, rank, address, mobile_number, email = line.split(",")
                
                cabincrew_employee = CabinCrewModel(ssn, name, role, rank, address, mobile_number, email)
                self.cabincrew_list.append(cabincrew_employee)
        crew_file.close()

        return self.cabincrew_list
        
    def load_all_airplanes(self):
        '''Retrieves airplanes and sends to Get LL'''
        airplane_file = open("./csv_files/Aircraft.csv", "r")

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
        dest_file = open("./csv_files/Destinations.csv", "r")

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
        voyages_file = open("./csv_files/Flights.csv","r")
        flight_nr_from_ice_list = []
        flight_nr_to_ice_list = []
        departure_from_ice_list = []
        arrival_to_ice_list = []
        Aircraft_ID_list = []

        counter = 1
        for line in voyages_file:
            if counter == 1:
                counter +=1
            elif counter % 2 == 0:
                flight_nr_from_ice_list.append(line[0])
                departure_from_ice_list.append(line[3])
                Aircraft_ID_list.append(line[5])
                counter += 1
                
            elif counter % 2 != 0 and counter != 1:
                flight_nr_to_ice_list.append(line[0])
                arrival_to_ice_list.append(line[4])
                counter += 1

        voyages_file.close()
        counter = 1

        for x in range(0,len(flight_nr_from_ice_list)):
            flight_nr_from_ice = flight_nr_from_ice_list[counter]
            departure_from_ice = departure_from_ice_list[counter]
            Aircraft_ID = Aircraft_ID_list[counter]
            flight_nr_to_ice = flight_nr_to_ice_list[counter]
            arrival_to_ice = arrival_to_ice_list[counter]
            flight_nr_from_ice,departure_from_ice,Aircraft_ID,flight_nr_to_ice,arrival_to_ice = line.split(",")
            Voyage = VoyagesModel() #þarf að spyrja hvað þýðir hvað hér
            self.voyages_list.append(Voyage)
            counter += 1


        return self.voyages_list


    def load_all_voyages_with_crew():
        voyages_file = open("./csv_files/Flights.csv","r")
        flight_nr_from_ice_list = []
        flight_nr_to_ice_list = []
        departure_from_ice_list = []
        arrival_to_ice_list = []
        Aircraft_ID_list = []
        captain_list = []
        copilot_list = []
        fsm_list = []
        fa1_list = []
        fa2_list = []
        voyages_list = []

        counter = 1
        for line in voyages_file:
            line = line.strip().split(",")
            print(line)
            if counter == 1:
                counter +=1
            elif counter % 2 == 0:
                flight_nr_from_ice_list.append(line[0])
                departure_from_ice_list.append(line[3])
                #Aircraft_ID_list.append(line[5])
                #captain_list.append(line[6])
                #copilot_list.append(line[7])
                #fsm_list.append(line[8])
                #fa1_list.append(line[9])
                #fa2_list.append(line[10])
                counter += 1
                
            elif counter % 2 != 0 and counter != 1:
                flight_nr_to_ice_list.append(line[0])
                arrival_to_ice_list.append(line[4])
                counter += 1

            voyages_file.close()

            counter = 1
            for x in range(len(arrival_to_ice_list)):
                flight_nr_from_ice = flight_nr_from_ice_list[counter]
                departure_from_ice = departure_from_ice_list[counter]
                Aircraft_ID = Aircraft_ID_list[counter]
                flight_nr_to_ice = flight_nr_to_ice_list[counter]
                arrival_to_ice = arrival_to_ice_list[counter]
                captain = captain_list[counter]
                copilot = copilot_list[counter]
                fsm = fsm_list[counter]
                fa1 = fa1_list[counter]
                fa2 = fa2_list[counter]
                flight_nr_from_ice,departure_from_ice,Aircraft_ID,flight_nr_to_ice,arrival_to_ice,captain,copilot,fsm,fa1,fa2 = line.split(",")
                Voyage = VoyagesModel() #þarf að spyrja hvað þýðir hvað hér
                self.voyages_list.append(Voyage)
                counter += 1

        


                
                
                

        voyages_file.close()

        return voyages_list
