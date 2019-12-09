
class UpdateLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def update_pilot_information(self,updated_pilot_ob):
        #ssn, name, new_role , new_rank, license_type, new_address, new_mobile_number, email = updated_pilot_list.split()
        #ef ég fæ updated pilot list sentann inn í þetta fall er ég þá ekki bara að senda hann beint í ioapi...?
        return self.ioapi.update_pilot(updated_pilot_ob)
        

    def update_cabin_crew_information(self, updated_crew_member_ob):
        #ssn, name, new_role, new_rank, new_address, new_mobile_number, new_email = updated_crew_member_list.split()
        return self.ioapi.update_cabincrew(updated_crew_member_ob)

    def update_emergency_contact(self, updated_emergency_contact_ob):
        return self.ioapi.update_emergency_contact(updated_emergency_contact_ob)
    
    def update_voyages(self, updated_voyage_ob):
        return self.ioapi.update_voyage(updated_voyage_ob)
        
