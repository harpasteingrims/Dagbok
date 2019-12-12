
class AirplanesModel():
    def __init__(self, planeID, airplane_type, manufacturer, seat_amount):
        self.planeID = planeID
        self.airplane_type = airplane_type
        self.manufacturer = manufacturer
        self.seat_amount = seat_amount
    
    def to_csv_string(self):
        return f"\r\n{self.planeID}, {self.airplane_type}, {self.manufacturer}, {self.seat_amount}"

    def print_out_line(self, in_front_str):
        return f"\r\n{in_front_str} {self.planeID}, {self.airplane_type}, {self.manufacturer}, {self.seat_amount}"