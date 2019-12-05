class Voyage_crewModel(PilotModel):

    def assign_crew_to_voyage(self, voyage, captain, copilot, fsm, fa1, fa2):
        self.voyage = voyage
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2

    def csv_to_string(self):
        return f"{self.time},{self.destination},{self.airplaneID}, {self.captain}, {self.copilot}, {self.fsm}, {self.fa1}, {self.fa2}"