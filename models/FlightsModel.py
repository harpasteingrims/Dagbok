class FlightsModel():
    def __init__(self, flight_number, departing_from, arriving_at, departure_time, arrival_time, aircraftID, captain = "", copilot = "", fsm = "", fa1 = "", fa2 = ""):
        self.flight_number = flight_number
        self.departing_from = departing_from
        self.arriving_at = arriving_at
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.aircraftID = aircraftID
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2

    #Þurfum að bæta virkni hér við

    def to_csv_string(self):
        return f"\r\n{self.departure_time}, {self.arriving_at}, {self.aircraftID}"
    
    def assign_crew_to_voyage(self, captain, copilot, fsm, fa1, fa2):
        staff_list = [captain, copilot, fsm, fa1, fa2]
        self.crew_list.append(staff_list)
        return self.crew_list

    def to_csv_string_crew(self):
        return f"\r\n{self.departure_time}, {self.arriving_at}, {self.aircraftID}, {self.captain}, {self.copilot}, {self.fsm}, {self.fa1}, {self.fa2}"