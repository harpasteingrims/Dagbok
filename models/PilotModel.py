class PilotsModel():
    def __init__(self,name, role, ssn, address, mobile_number, email, license_type):
        self.name = name
        self.role = role
        self.ssn = ssn 
        self.address = address
        self.mobile_number = mobile_number
        self.email = email
        self.license_type = license_type
    
    def add_pilot_to_file(self):
        pass

    def __get__(self):
        pass
