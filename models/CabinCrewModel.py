class CabinCrewModel():
    def __init__(self, name, role, ssn, address, mobile_number, email):
        self.name = name
        self.role = role
        self.ssn = ssn
        self.address = address
        self.mobile_number = mobile_number
        self.email = email

    def set_cabincrew(self):
        cabincrew = {}
        cabincrew[self.ssn] = [self.name, self.role, self.address, self.mobile_number, self.email]
        
        return cabincrew
