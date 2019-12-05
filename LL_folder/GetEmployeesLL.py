class GetEmployeesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        
    def get_all_employees(self):
        all_employee_list = self.ioapi.get_list_of_all_employees()
        return all_employee_list

    def get_all_pilots(self):
        pilot_list = self.ioapi.get_list_of_all_pilots()
        return pilot_list

    def get_available_employees(self,date):
        avaliable_employees = []

        #all_employee_list = self.ioapi.get_list_of_all_employees()
        # flokka þá sem eru að vinna á ákv dagsetningu.......
        return avaliable_employees

    def get_unavailable_employees(self,date):
        unavaliable_employees = []
        
        #all_employee_list = self.ioapi.get_list_of_all_employees()
        
        # flokka þá sem ekki eru að vinna....

        return unavaliable_employees

    def get_all_cabin_crew(self):
        pass