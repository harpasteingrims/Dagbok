class CabinCrewModel():
    def __init__(self, ssn, name, role, rank, address, mobile_number, email):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.address = address
        self.mobile_number = mobile_number
        self.email = email
    
    def to_csv_string(self):
        return f"{self.ssn}, {self.name}, {self.role}, {self.rank}, {self.address}, {self.mobile_number} ,{self.email}"
