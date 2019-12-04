class GetIO():
    def __init__(self):
        pass

    def get_pilots():
        pilot_file = open("Pilots.csv","r")
        
        pilot_file_list = []
        for line in pilot_file:
            line = line.strip().split(",")
            SSN = line[0]
            Name = line[1]
            Role = line[2]
            Rank = line[3]
            licens = line[4]
            

        pilot_list = []
        print(pilot_list)

        return pilot_list
        

    def get_airplane():
        '''Retrieves airplanes and sends to Get LL'''
        airplane_file = open("Aircraft.csv")

        airplane_file_list = []

        for line in airplane_file:
            line = line.strip().split(",")
            PlaneID = line[0]
            Type = line[1]
            Manufacturer = line[2]
            Seat_amount = line[3]
            
            airplane = {}
            airplane[PlaneID] = [Type,Manufacturer,Seat_amount]
            airplane_file_list.append(airplane)
            airplane.clear
        airplane_list = []
        for obj in airplane_file_list[1:]:
            airplane_list.append(obj)

        return airplane_list
    def get_destinations():
        dest_file = open("destinations.csv")
        
        dest_file_list = []
        counter = 1
        for line in dest_file:
            if counter = 1:
                counter += 1
            else:
                line = line.strip.split(",")
                country = line[0]
                airport = line[1]
                flight_dur_from_Ice = line[2]
                dist_from_Ice = line[3]
                contact_name = line[4]
                contact_phone_number = line[5]
            
            

            DestinationsModel.set_destinations(country,airport,flight_dur_from_Ice,dist_from_Ice,contact_name,contact_phone_number)
            dest_file_list.append(destination)
        destination_list = []
        for obj in dest_file_list[1:]:
            destination_list.append(obj)

    def get_cabin_crew():
        crew_file = open("CabinCrew.csv","r")
        
        crew_file_list = []
        for line in crew_file:
            line = line.strip().split(",")
            SSN = line[0]
            Name = line[1]
            Role = line[2]
            Rank = line[3]
            

        crew_list = []
        print(crew_list)

        return crew_list

    def get_voyages():
        voyages_file = open("Voyages.csv","r")

        voyage_list = []



def main():
    listi = GetIO.get_destinations()
    pass
main()