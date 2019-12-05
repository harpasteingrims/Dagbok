class PilotsModel():
    def __init__(self,SSN, name, role, rank, license_type, address, mobile_number, email):
        self.SSN = SSN 
        self.name = name
        self.role = role
        self.rank = 
        self.license_type = license_type
        self.address = address
        self.mobile_number = mobile_number
        self.email = email
        
    
    def to_csv_string(self):
        return f"{self.ssn},{self.name},{self.role},{self.rank},{self.license_type},{self.address},{self.mobile_number},{self.email}"

