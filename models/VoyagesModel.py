import datetime
import dateutil.parser
class VoyagesModel():
    def __init__(self, departure_time, destination, aircraftID, arrival_time = "", crew_list = []):
        self.departure_time = departure_time #hér erum við búin í LL-layer að nota datetime þar sem þetta formattast saman í year,month,day,hour,minute
        self.destination = destination #tilvikið destination, pæling hvort þetta ætti ekki að heita airport?
        self.aircraftID = aircraftID
        self.arrival_time = arrival_time #leiðréttið ef þetta er vitlaust gert - Hallmar
        self.crew_list = crew_list

    def to_csv_string(self):
        return f"\n{self.departure_time}, {self.arrival_time}, {self.destination}, {self.aircraftID}"
 
    def print_voy_out(self, counter):
        return f"\n{counter} {self.departure_time}, {self.destination}, {self.aircraftID}"
    
    def assign_crew_to_voyage(self, captain, copilot, fsm, fa1, fa2): #Held að crewið myndi verða hér listi af listum, en þurfum að hafa það bara sem lista
        staff_list = [captain, copilot, fsm, fa1, fa2]
        self.crew_list.append(staff_list)
        return self.crew_list
    
    def calculate_arrival_date(self):
        pass

    def csv_voyage_with_crew_to_string(self):
        return f"\n{self.departure_time}, {self.arrival_time}, {self.destination}, {self.aircraftID}, {self.crew_list[0]}, {self.crew_list[1]}, {self.crew_list[2]}, {self.crew_list[3]}, {self.crew_list[4]}, {self.crew_list[5]}"

    def print_schedule(self, counter):
        departure_time = dateutil.parser.parse(self.departure_time)
        arrival_time = dateutil.parser.parse(self.arrival_time)

        if len(self.crew_list) == 5:

            return f"\n{counter} {self.destination}: {departure_time.day}/{departure_time.month}/{departure_time.year} - {arrival_time.day}/{arrival_time.month}/{arrival_time.year}, fully staffed"

        else:
            return f"\n{counter} {self.destination}: {departure_time.day}/{departure_time.month}/{departure_time.year} - {arrival_time.day}/{arrival_time.month}/ {arrival_time.year}, not fully staffed"