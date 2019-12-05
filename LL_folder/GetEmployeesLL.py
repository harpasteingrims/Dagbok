class GetEmployeesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        self.avaliable_employees = []
        self.unavaliable_employees = []
        
    def get_all_employees(self):
        """ Calls the IOAPI to get a list of all employees """
        return sorted(self.ioapi.get_list_of_all_employees())

    def get_all_pilots(self):
        """ Calls the IOAPI to get a list of all pilots """
        return sorted(self.ioapi.get_list_of_all_pilots())
    
    def get_all_cabin_crew(self):
        """ Calls the IOAPI to get a list of the whole cabin crew """
        return sorted(self.ioapi.get_list_of_all_cabin_crew())
    
    def get_available_employees(self,date):
        
        """ Calls the IOAPI to get a list of all employees """
        all_employee_list = self.get_all_employees()

        # flokka þá sem eru að vinna á ákv dagsetningu.......
        return avaliable_employees

    def get_unavailable_employees(self,date):
        
        
        #all_employee_list = self.ioapi.get_list_of_all_employees()
        
        # flokka þá sem ekki eru að vinna....

        return unavaliable_employees

    