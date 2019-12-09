
class VoyagesModel():
    def __init__(self, departure_time, arrival_time, destination, aircraftID, crew_list = []):
        self.departure_time = departure_time #hér erum við búin í LL-layer að nota datetime þar sem þetta formattast saman í year,month,day,hour,minute
        self.arrival_time = arrival_time
        self.destination = destination #tilvikið destination
        self.aircraftID = aircraftID
        self.crew_list = crew_list

    def csv_voyage_to_string(self):
        return f"{self.departure_time},{self.arrival_time},{self.destination},{self.aircraftID}"
    
    def assign_crew_to_voyage(self, captain, copilot, fsm, fa1, fa2):
        staff_list = [captain, copilot, fsm, fa1, fa2]
        self.crew_list.append(staff_list)
        return self.crew_list
    
    def calculate_arrival_date(self):
        pass
        


    def csv_voyage_with_crew_to_string(self):
        return f"{self.departure_time},{self.arrival_time}, {self.destination}, {self.aircraftID}, {self.crew_list[0]}, {self.crew_list[1]}, {self.crew_list[2]}, {self.crew_list[3]}, {self.crew_list[4]}, {self.crew_list[5]}"
