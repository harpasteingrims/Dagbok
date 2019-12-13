class IOAPI:
    def __init__(self, filename):
        self.filename = filename
        
class GetIO:
    def __init__(self, filename):
        IOAPI.__init__(self, filename)

    def get_employee():                     '''Retrieves employees and sends to Get LL'''
        pass

    def get_airplane():                     '''Retrieves airplanes and sends to Get LL'''
        pass
        
    def get_destinations():                 '''Retrieves destinations and sends to Get LL'''
        pass

    def get_voyage():                       '''Retrieves voyages and sends to Get LL'''
        pass

class CreateIO:
    def __init__(self, filename):          
        IOAPI.__init__(self, filename)

    def add_employee():                     '''Retrieves employees and sends to Create LL'''
        pass

    def add_airplane():                     '''Retrieves airplanes and sends to Create LL'''
        pass
        
    def add_destination():                  '''Retrieves destinations and sends to Create LL'''
        pass

    def add_voyage():                       '''Retrieves voyages and sends to Create LL'''
        pass
    

"""def load_all_voyages_with_crew(self):
        flights_with_crew_file = open("./csv_files/Flights.csv","r", encoding= "utf8")
        flights_list = []
        voyages_list = []

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
                except IndexError:
                    aircraft_ID = ""
                    captain = ""
                    copilot = ""                    
                    fsm = ""
                    fa1 = ""
                    fa2 = ""
                #flight_number,departing_from,arriving_at,departure_time,arrival_time,aircraft_ID,captain,copilot,fsm,fa1,fa2 = line.split(", ")
                flight_with_crew = FlightsModel(flight_number, departing_from, arriving_at, departure_time, arrival_time, aircraft_ID, captain, copilot, fsm, fa1, fa2)
                flights_list.append(flight_with_crew)

        counter = 1

        for flights in flights_list:
            if counter % 2 != 0:
                departure_time = flights.departure_time
                destination = flights.arriving_at
                aircraftID = flights.aircraftID
                crew_list = [flights.captain, flights.copilot, flights.fsm, flights.fa1, flights.fa2]


                counter += 1
            elif counter % 2 == 0:
                arrival_time = flights.arrival_time
                voyage = VoyagesModel(departure_time, arrival_time, destination, aircraftID, crew_list)
                voyages_list.append(voyage)

                counter += 1


        flights_with_crew_file.close()

        return voyages_list"""