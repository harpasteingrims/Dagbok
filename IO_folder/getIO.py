from models.CabinCrewModel import CabinCrewModel
from models.AirplanesModel import AirplanesModel
from models.DestinationsModel import DestinationsModel
from models.PilotModel import PilotsModel

class GetIO():
    def __init__(self):
        self.all_employee_list = []
        self.pilot_list = []
        self.airplane_list = []
        self.destination_list = []

        
    def get_all_employees(self):

        self.pilot_list = self.get_all_pilots()
        self.crew_list = self.get_cabin_crew()

        self.all_employee_list.extend(self.crew_list)
        self.all_employee_list.extend(self.pilot_list)

        return sorted(self.all_employee_list)

    def get_all_pilots(self):
        pilot_file = open("Pilots.csv","r")
        
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
                #pilot = {}
                #pilot[SSN] = [name, role, plane_license, address, mobile_number, email]
                pilot = PilotsModel(SSN, name, role, rank, plane_license, address, mobile_number, email)
                self.pilot_list.append(pilot)

        return self.pilot_list
        
    def get_all_airplanes(self):
        '''Retrieves airplanes and sends to Get LL'''
        airplane_file = open("Aircraft.csv")

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
        return self.airplane_list

    def get_destinations(self):
        dest_file = open("destinations.csv")

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
                Destination = DestinationsModel(self,country,airport,flight_dur_from_Ice,dist_from_Ice,contact_name,contact_phone_number)
                self.destination_list.append(Destination)

        return self.destination_list
        

    def get_cabin_crew(self):
        crew_file = open("CabinCrew.csv","r")
        
        
        crew_list = []
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
                Address = line[4]
                Mobile_number = line[5]
                email = line[6]
                Crew_employee = CabinCrewModel.set_cabincrew(self,Name,Role,SSN,Address,Mobile_number,email)
                crew_list.append(Crew_employee)

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
                


