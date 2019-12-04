class DestinationsModel():
    def __init__(self, country, airport, flight_duration, distance, contact, contact_phone):
        self.country = country
        self.airport = airport
        self.flight_duration = flight_duration
        self.distance = distance
        self.contact = contact
        self.contact_phone = contact_phone

    def set_destinations(self):
        destination = {}
        destination[self.country] = [self.airport, self.flight_duration, self.distance, self.contact, self.contact_phone]
        
        return destination

    
        
