#from models.CabinCrewModel import CabinCrewModel
#from models.AirplanesModel import AirplanesModel
#from models.DestinationsModel import DestinationsModel
#from models.PilotModel import PilotsModel

class GetIO():
    def __init__(self):
        pass

    def get_all_employees(self):
        all_employee_list = []
        
        pilot_list = self.get_all_pilots()
        crew_list = self.get_cabin_crew()

        all_employee_list.extend(crew_list)
        all_employee_list.extend(pilot_list)

        return sorted(all_employee_list)

    def get_all_pilots(self):
        pilot_file = open("Pilots.csv","r")
        
        pilot_list = []

        counter = 1
        for line in pilot_file:
            if counter == 1:
                counter += 1
            else:
                line = line.strip().split(",")
                SSN = line[0]
                Name = line[1]
                Role = line[2]
                Rank = line[3]
                licens = line[4]
            

        
        print(pilot_list)

        return pilot_list
        

    def get_all_airplanes(self):
        '''Retrieves airplanes and sends to Get LL'''
        airplane_file = open("Aircraft.csv")

        airplane_list = []
        counter = 1
        for line in airplane_file:
            if counter == 1:
                counter += 1
            else:
                line = line.strip().split(",")
                PlaneID = line[0]
                Type = line[1]
                Manufacturer = line[2]
                Seat_amount = line[3]
                
        
        print(airplane_list)
        
        return airplane_list

    def get_destinations(self):
        dest_file = open("destinations.csv")
        
        destination_list = []
        counter = 1
        for line in dest_file:
            if counter == 1:
                counter += 1
            else:
                line = line.strip.split(",")
                country = line[0]
                airport = line[1]
                flight_dur_from_Ice = line[2]
                dist_from_Ice = line[3]
                contact_name = line[4]
                contact_phone_number = line[5]
                destination_list.append(country)
        return destination_list
                
            
            
        destination_list = []
        

    def get_cabin_crew(self):
        crew_file = open("CabinCrew.csv","r")
        
        crew_file_list = []

        counter = 1

        for line in crew_file:
            if counter == 1:
                counter += 1
            else:
                line = line.strip().split(",")
                SSN = line[0]
                Name = line[1]
                Role = line[2]
                Rank = line[3]
            

        crew_list = []
        print(crew_list)

        return crew_list

    def get_voyages(self):
        voyages_file = open("Voyages.csv","r")

        voyages_list = []

        counter = 1
        for line in voyages_file:
            if counter == 1:
                counter +=1
            else:
                line = line.strip().split(",")
                Date = line[0]
                Time = line[1]
                Destination = line[2]
                AirplaneID = line[3]
                


def main():
    listi = GetIO.get_cabin_crew()
    pass
main()