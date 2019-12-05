class DestinationsModel():
    def __init__(self, country ,airport ,flight_dur_from_Ice ,dist_from_Ice ,contact_name ,contact_phone_number):
        self.country = country
        self.airport = airport
        self.flight_dur_from_Ice = flight_dur_from_Ice
        self.dist_from_Ice = dist_from_Ice
        self.contact_name = contact_name
        self.contact_phone_number = contact_phone_number

    def to_csv_string(self):
        return f"{self.country},{self.airport},{self.flight_dur_from_Ice},{self.dist_from_Ice},{self.contact_name},{self.contact_phone_number}"
    
        
