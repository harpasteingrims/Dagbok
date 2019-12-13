from IO_folder.GetIO import GetIO
from IO_folder.CreateIO import CreateIO
import csv
class UpdateIO:
    def __init__(self, createio, getio):
        self.createio = createio
        self.getio = getio

        # ef við viljum að update noti get til að updatea
        
    def update_emergency_contact(self, update_contact):               
        ''' Updates an emergency contact for a certain country'''
        destionations_list = GetIO().load_all_destinations()
        with open("filename.csv", "w", encoding= "utf8", newline="") as csvfile:
            fieldnames = ["country", "airport", "flightDurFromIce", "DistFromIce", "ContactName", "ContactPhoneNR", "ID"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        for elem in destionations_list:
            if elem.destiID == update_contact.destiID:
                self.createio.store_destination(update_contact)
            else:    
                self.createio.store_destination(elem)

    def update_voyage(self, voyage_object):                    
        '''Updates a voyage'''
        voyages_list = GetIO.load_all_voyages(self)
        with open("./csv_files/Flights.csv","w", encoding= "utf8", newline="") as csvfile:
            fieldnames = ["flightNumber", "departingFrom", "arrivingAt", "departure", "arrival", "aircraftID", "captain", "copilot", " fsm", "fa1", "fa2"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        
        for elem in voyages_list:
            if elem.departure_time == voyage_object.departure_time and elem.destination == voyage_object.destination:
                self.createio.store_voyage(voyage_object)
            else:
                self.createio.store_voyage(elem)

    def update_pilot(self, update_pilot):
        ''' Updates a pilot '''
        pilot_list = GetIO.load_all_pilots(self)
        with open("./csv_files/Pilots.csv","w", encoding= "utf8", newline="") as csvfile:
            fieldnames = ["ssn", " name", " role" ,"rank" , "plane license" ,"address" , "mobile number" , "email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        for elem in pilot_list:
            if elem.ssn == update_pilot.ssn:
                self.createio.store_pilot(update_pilot)
                
            else:
                self.createio.store_pilot(elem)
        
    def update_cabincrew(self, update_cabincrew):
        cabincrew_list = GetIO.load_all_cabincrew(self)
        with open("./csv_files/CabinCrew.csv","w", encoding= "utf8", newline="") as csvfile:
            fieldnames = ["ssn", " name", " role", " rank", " address", " mobile number", "email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        for elem in cabincrew_list:
            if elem.ssn == update_cabincrew.ssn:
                self.createio.store_cabincrew(update_cabincrew)
            else:
                self.createio.store_cabincrew(elem)