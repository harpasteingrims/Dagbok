
class VoyagesModel():
    def __init__(self, time, destination, airplaneID, copilot =[]):
        self.time = time #hér erum við búin í LL-layer að nota datetime þar sem þetta formattast saman í year,month,day,hour,minute
        self.destination = destination
        self.airplaneID = airplaneID
        self.crew_list = []

    def csv_voyage_to_string(self):
        return f"{self.date},{self.destination},{self.airplaneID}"
    
    def assign_crew_to_voyage(self, captain, copilot, fsm, fa1, fa2):
        staff_list = [captain, copilot, fsm, fa1, fa2]
        self.crew.append(staff_list)
        return self.crew_list

    def csv_voyage_with_crew_to_string(self):
        return f"{self.date}, {self.destination}, {self.airplaneID}, {self.crew_list[0]}, {self.crew_list[1]}, {self.crew_list[2]}, {self.crew_list[3]}, {self.crew_list[4]}, {self.crew_list[5]}"
