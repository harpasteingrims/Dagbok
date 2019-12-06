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
                CreateIO(self.get).add_destiantions(update_contact)
            else:    
                CreateIO(self.get).add_destiantions(elem)

    def update_voyage(self, voyage_object):                    
        '''Updates a voyage'''
        voyages_list = GetIO.load_all_voyages()
        with open("csv_files\Voyages.csv","w")
        for line in voyages_file:
            if voyage_object.flightID == line[0]:
                pass


    def update_pilot(self, update_pilot):
        ''' Updates a pilot '''
        pilot_file = open("csv_files\Pi")
    
    def update_cabincrew(self, update_cabincrew):
        pass
