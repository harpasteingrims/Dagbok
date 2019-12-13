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