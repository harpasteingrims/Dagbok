
class VoyagesModel():
    def __init__(self, time, destination, airplaneID, employees = []):
        self.time = time #hér erum við búin í LL-layer að nota datetime þar sem þetta formattast saman í year,month,day,hour,minute
        self.destination = destination
        self.airplaneID = airplaneID
        self.employees = employees

    #def set_voyages(self):
    #    voyage = {}
    #    if len(self.employees) > 0:
    #        voyage[self.time] = [self.destination, self.airplane, self.employees]
    #    else:
    #        voyage[self.time] = [self.destination, self.airplane]

    #    return voyage