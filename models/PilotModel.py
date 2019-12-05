class PilotsModel():
    def __init__(self,SSN, name, role, rank, plane_license, address, mobile_number, email):
        self.SSN = SSN 
        self.name = name
        self.role = role
        self.rank = rank
        self.plane_licence = plane_license
        self.address = address
        self.mobile_number = mobile_number
        self.email = email
        
    def to_csv_string(self):
        return f"{self.SSN},{self.name},..."
    #def set_pilot(self):
    #    pilot = {}
    #    pilot[self.ssn] = [self.name, self.role, self.address, self.mobile_number, self.email] 
        
    #    return pilot

