
class VoyagesModel():
    def __init__(self, time, destination, airplaneID, copilot =[]):
        self.time = time #hér erum við búin í LL-layer að nota datetime þar sem þetta formattast saman í year,month,day,hour,minute
        self.destination = destination
        self.airplaneID = airplaneID
        self.crew_list = []

    def csv_voyage_to_string(self):
        return f"{self.time},{self.destination},{self.airplaneID}"
    
    def assign_crew_to_voyage(self, captain, copilot, fsm, fa1, fa2):
        staff_list = [captain, copilot, fsm, fa1, fa2]
        self.crew.append(staff_list)

    def csv_voyage_with_crew_to_string(self):
        return f"{self.time},{self.destination},{self.airplaneID}, {self.captain}, {self.copilot}, {self.fsm}, {self.fa1}, {self.fa2}"
