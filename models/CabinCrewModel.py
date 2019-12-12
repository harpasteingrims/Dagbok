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
        return f"\n{self.ssn}, {self.name}, {self.role}, {self.rank}, {self.address}, {self.mobile_number}, {self.email}"

    def print_info_new_line(self):
        return f"Name: {self.name} \nRank: {self.rank} \nSSN: {self.ssn} \nAdress: {self.address} \nMobile number: {self.mobile_number} \nEmail:{self.email}"

    def print_info_in_line(self, front_of_str = ""):
        return f"\n{front_of_str} {self.name}, {self.ssn}, {self.role}, {self.rank}, {self.address}, {self.mobile_number}, {self.email}"

    def print_available(self, counter):
        return f"\n{counter} {self.name}, {self.rank}"
