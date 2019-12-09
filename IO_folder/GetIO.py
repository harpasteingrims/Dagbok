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
        self.flights_list = []
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
                license_type = line[4]
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


        return self.destination_list  
    
    def load_all_voyages(self):
        flights_file = open("./csv_files/Flights.csv","r")
        """flight_number_list = []
        departing_from_list = []
        arriving_at_list = []
        departure_time_list = []
        arrival_time_list = []
        aircraft_ID_list = []"""
        

        counter = 1
        for line in flights_file:
            line = line.strip().split(",")
            if counter == 1:
                counter += 1
            else:
                try:
                    flight_number = line[0]
                    departing_from = line[1]
                    arriving_at = line[2]
                    departure_time = line[3]
                    arrival_time = line[4]
                    aircraft_ID = line[5]
                    #flight_number, departing_from, arriving_at, departure_time, arrival_time, aircraft_ID = line.split(",")
                except IndexError:
                    aircraft_ID = ""
                Flight = FlightsModel(flight_number,departing_from,arriving_at,departure_time,arrival_time,aircraft_ID)
                self.flights_list.append(Flight)
                  


        counter = 1

        for flights in flights_list:
            if counter % 2 != 0:
                departure_time = flights.departure_time
                destination = flights.arriving_at
                aircraft_ID = flights.aircraft_ID


                counter += 1
            elif counter % 2 == 0:
                arrival_time = flights.arrival_time
                voyage = VoyagesModel(departure_time, arrival_time, destination, aircraftID)
                self.voyages_list.append(voyage)

                counter += 1

        flights_file.close()
    
        return self.voyages_list


    def load_all_voyages_with_crew(self):
        flights_with_crew_file = open("./csv_files/Flights.csv","r")

        counter = 1
        for line in flights_with_crew_file:
            line = line.strip().split(",")
            if counter == 1:
                counter += 1
            else:   
                try:
                    flight_number = line[0]  
                    departing_from = line[1]
                    arriving_at = line[2]
                    departure_time = line[3]
                    arrival_time = line[4]
                    aircraft_ID = line[5]    
                    captain = line[6]
                    copilot = line[7]
                    fsm = line[8]
                    fa1 = line[9]
                    fa2 = line[10]
                except IndexError:
                    aircraft_ID = ""
                    captain = ""
                    copilot = ""                    
                    fsm = ""
                    fa1 = ""
                    fa2 = ""
                #flight_number,departing_from,arriving_at,departure_time,arrival_time,aircraft_ID,captain,copilot,fsm,fa1,fa2 = line.split(",")
                flight_with_crew = FlightsModel(flight_number,departing_from,arriving_at,departure_time,arrival_time,aircraft_ID,captain,copilot,fsm,fa1,fa2)
                self.flights_list.append(flight_with_crew)

        counter = 1

        for flights in flights_list:
            if counter % 2 != 0:
                departure_time = flights.departure_time
                destination = flights.arriving_at
                aircraft_ID = flights.aircraft_ID
                crew_list = [flights.captain, flights.copilot, flights.fsm, flights.fa1, flights.fa2]


                counter += 1
            elif counter % 2 == 0:
                arrival_time = flights.arrival_time
                voyage = VoyagesModel(departure_time, arrival_time, destination, aircraftID, crew_list)
                self.voyages_list.append(voyage)

                counter += 1


        flights_with_crew_file.close()

        return self.voyages_list
