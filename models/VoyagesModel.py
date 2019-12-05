
class VoyagesModel():
    def __init__(self, time, destination, airplaneID, employees = []):
        self.time = time #hér erum við búin í LL-layer að nota datetime þar sem þetta formattast saman í year,month,day,hour,minute
        self.destination = destination
        self.airplaneID = airplaneID
        self.employees = employees

    def csv_to_string(self):
        return f"{self.time},{self.destination},{self.airplaneID},{self.employees}"