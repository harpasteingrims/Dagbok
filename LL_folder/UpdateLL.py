class UpdateLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def update_pilot_information(self,updated_pilot_list):
        ssn, name, new_role , new_rank, license_type, new_address, new_mobile_number, email = updated_pilot_list.split()
        
        pass

    def update_cabin_crew_information(self, updated_crew_member_list):
        ssn, name, new_role, new_rank, new_address, new_mobile_number, new_email = updated_crew_member_list.split()
        pass

    def update_emergency_contact(self):
        pass
