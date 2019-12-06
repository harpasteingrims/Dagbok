from IO_folder.GetIO import GetIO
from IO_folder.CreateIO import CreateIO
import csv
class UpdateIO:
    def __init__(self, get):
        self.get = get
        # ef við viljum að update noti get til að updatea
        
    def update_emergency_contact(self, update_contact):               
        ''' Updates an emergency contact for a certain country'''
        destionations_list = GetIO().load_all_destinations()
        with open("filename.csv", "w", newline="") as csvfile:
            fieldnames = ["country","airport","flightDurFromIce","DistFromIce","ContactName","ContactPhoneNR"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        for elem in lis:
            if elem.airport == update_contact.airport:
                CreateIO(self.get).store_destiantions(update_contact)
            else:    
                CreateIO(self.get).store_destiantions(elem)

    def update_voyage(self, voyage_object):                    
        '''Updates a voyage'''
        flights_list = GetIO.load_all_voyages()
        with open("csv_files\Flights.csv","w", newline="") as csvfile:
            fieldnames = ["flightNumber","departingFrom","arrivingAt","departure","arrival","aircraftID","captain","copilot","fsm","fa1","fa2"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        
        for elem in flights_list:
            if elem.flightNumber == voyage_object.flight_number:
                CreateIO(self.get).store_voyage(voyage_object)
            else:
                CreateIO(self.get).store_voyage(elem)

    def update_pilot(self, update_pilot):
        ''' Updates a pilot '''
        pilot_list = GetIO.load_all_pilots()
        with open("csv_files\Pilots.csv","w",newline="") as csvfile:
            fieldnames = ["ssn","name","role","rank", "plane license","address", "mobile number", "email"]
            write = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        for elem in pilot_list:
            if elem.ssn == update_pilot.SSN:
                CreateIO(self.get).store_pilot(update_pilot)
            else:
                CreateIO(self.get).store_pilot(elem)
        
    def update_cabincrew(self, update_cabincrew):
        cabincrew_list = GetIO.load_all_cabincrew()
        with open("csv_files\CabinCrew.csv","w", newline="") as csvfile:
            fieldnames = ["ssn","name","role","rank", "address", "mobile number", "email"]
            write = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
        for elem in cabincrew_list:
            if elem