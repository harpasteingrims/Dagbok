import csv
import sys
sys.path.insert(0, 'VERKLEGT-1-verkefni/models') #Vorum að prufa þetta til að ná að importa models en þetta virkar ekki

from models.CabinCrewModel import CabinCrewModel
from models.AirplanesModel import AirplanesModel
from models.DestinationsModel import DestinationsModel
from models.PilotsModel import PilotsModel
from models.VoyagesModel import VoyagesModel
from models.FlightsModel import FlightsModel

class GetIO():

    def load_all_employees(self):
        """returns a list of both pilot and cabincrew objects from CabinCrew.csv and Pilots.csv"""

        all_employee_list = []

        if len(all_employee_list) == 0:

            pilot_list = self.load_all_pilots()
            cabincrew_list = self.load_all_cabincrew()

            all_employee_list = pilot_list + cabincrew_list

            return all_employee_list
     
    def load_all_pilots(self):
        """returns a list of pilot objects from Pilots.csv"""

        pilot_file = open("./csv_files/Pilots.csv","r", encoding= "utf8")

        pilot_list = []
        counter = 1
        for line in pilot_file:
            line = line.strip()
            if counter == 1:
                counter += 1
            else:
                ssn, name, role, rank, license_type, address, mobile_number, email = line.split(", ")
                pilot = PilotsModel(ssn, name, role, rank, license_type, address, mobile_number, email)
                pilot_list.append(pilot)
        
        pilot_file.close()
        
        return pilot_list

    def load_all_cabincrew(self):
        """returns a list of cabincrew object from CabinCrew.csv"""

        crew_file = open("./csv_files/CabinCrew.csv","r", encoding= "utf8")
        
        cabincrew_list = []
        counter = 1
        for line in crew_file:
            line = line.strip()
            if counter == 1:
                counter += 1
            else:
                ssn, name, role, rank, address, mobilenumber, email = line.split(", ")
                
                cabincrew_employee = CabinCrewModel(ssn, name, role, rank, address, mobilenumber, email)
                cabincrew_list.append(cabincrew_employee)
        crew_file.close()

        return cabincrew_list
        
    def load_all_airplanes(self):
        '''Retrieves airplanes and sends to Get LL'''

        airplane_file = open("./csv_files/Aircraft.csv", "r", encoding= "utf8")

        airplane_list = []
        counter = 1
        for line in airplane_file:
            line = line.strip()
            if counter == 1:
                counter += 1 #to skip the header
            else:
                planeID, airplane_type, manufacturer, seat_amount = line.split(", ")
                airplane = AirplanesModel(planeID, airplane_type, manufacturer, seat_amount)
                airplane_list.append(airplane)

        airplane_file.close()

        return airplane_list

    def load_all_destinations(self):
        """returns a list of destination objects from Destinations.csv"""

        dest_file = open("./csv_files/Destinations.csv", "r", encoding= "utf8")

        destination_list = []
        counter = 1
        for line in dest_file:
            line = line.strip()
            if counter == 1:
                counter += 1 #to skip the header
            else:
                country, airport, flight_dur_from_Ice, dist_from_Ice, contact_name, contact_phone_number, destiID = line.split(", ")
                destination = DestinationsModel(country, airport, flight_dur_from_Ice, dist_from_Ice, contact_name, contact_phone_number, destiID)
                destination_list.append(destination)
                
        dest_file.close()


        return destination_list  
    
    def load_all_voyages(self):
        """returns a list of voyage objects from Flights.csv"""

        flights_with_crew_file = open("./csv_files/Flights.csv","r", encoding= "utf8")
        flights_list = []
        voyages_list = []
        
        counter = 1
        for line in flights_with_crew_file:
            line = line.strip().split(", ")
            if counter == 1: # to skip the first line in file
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
                except IndexError: #so we can read the whole file, not just manned flights
                    captain = ""
                    copilot = ""                    
                    fsm = ""
                    fa1 = ""
                    fa2 = ""
                flight_with_crew = FlightsModel(flight_number,departing_from,arriving_at,departure_time,arrival_time,aircraft_ID,captain,copilot,fsm,fa1,fa2)
                flights_list.append(flight_with_crew)

        i = 0
        for j in range(len(flights_list)//2): #here we use the flights to create a voyage obj
            outbound_flight_num = flights_list[i].flight_number
            departure_time = flights_list[i].departure_time
            destination = flights_list[i].arriving_at
            aircraftID = flights_list[i].aircraftID
            return_flight_num = flights_list[i+1].flight_number
            arrival_time = flights_list[i].arrival_time
            departure_dest = flights_list[i+1].arriving_at #i+1 is used so we differentiate between the 1st flight and 2nd flight in a voyage
            return_departure_time = flights_list[i+1].departure_time
            return_arrival_time = flights_list[i+1].arrival_time
            if flights_list[i].captain == "":
                crew_list = []
            else:
                crew_list = [flights_list[i].captain, flights_list[i].copilot, flights_list[i].fsm, flights_list[i].fa1, flights_list[i].fa2]

            voyage = VoyagesModel(departure_time, destination, aircraftID, arrival_time, crew_list, outbound_flight_num, return_flight_num, return_departure_time, return_arrival_time, departure_dest)
            voyages_list.append(voyage)

            i += 2

        flights_with_crew_file.close()

        return voyages_list

    def load_all_flights(self):
        """returns a list of Flight objects from Flights.csv"""

        flights_with_crew_file = open("./csv_files/Flights.csv","r", encoding= "utf8")
        flights_list = []
        
        counter = 1
        for line in flights_with_crew_file:
            line = line.strip().split(", ")
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
                except IndexError: #if flight has no crew variables become empty strings
                    aircraft_ID = ""
                    captain = ""
                    copilot = ""                    
                    fsm = ""
                    fa1 = ""
                    fa2 = ""
                flight_with_crew = FlightsModel(flight_number,departing_from,arriving_at,departure_time,arrival_time,aircraft_ID,captain,copilot,fsm,fa1,fa2)
                flights_list.append(flight_with_crew)

        return flights_list