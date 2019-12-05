class GetEmployeesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        self.avaliable_employees = []
        self.unavaliable_employees = []
        
    def list_all_employees(self):
        """ Calls the IOAPI to get a list of all employees """
        return sorted(self.ioapi.get_list_of_all_employees())

    def list_all_pilots(self):
        """ Calls the IOAPI to get a list of all pilots """
        return sorted(self.ioapi.get_list_of_all_pilots())
    
    def list_all_cabin_crew(self):
        """ Calls the IOAPI to get a list of the whole cabin crew """
        return sorted(self.ioapi.get_list_of_all_cabin_crew())
    
    def find_common_named_pilots(self, name):
        common_names = []
        pilot_list = self.get_all_pilots()
        
        for pilot_object in pilot_list:
            if pilot_object.name == name:
                
                common_names.append(pilot_object)
        
        return common_names

    def list_info_about_pilot_by_name(self, name):
        """  """
        searched_pilot_info = []

        pilot_list = self.get_all_pilots()

        for pilot in self.pilot_list:
            if pilot.name == name:
                # TODO handle if found
                pass
        # TODO handle if none is found

    def find_common_named_cabincrew(self,name):
        return self.getemployees.find_common_named_pilots(name)


    def list_info_about_cabincrew_by_name(self):
        pass
        

    def list_info_about_cabincrew_by_name(self):
        pass


    def list_schedule_cabincrew_by_date(self):
        pass

    def list_schedule_pilot_by_date(self):
        pass

    def list_available_employees(self,date):
        
        """ Calls the IOAPI to get a list of all employees """
        all_employee_list = self.get_all_employees()

        # flokka þá sem eru að vinna á ákv dagsetningu.......
        return avaliable_employees

    def list_unavailable_employees(self,date):
        
        
        #all_employee_list = self.ioapi.get_list_of_all_employees()
        
        # flokka þá sem ekki eru að vinna....

        return unavaliable_employees

    def list_unavaliable_pilots(self):
        pass

    def list_available_cabin_crew(self):
        pass
    
    def list_available_cabin_crew(self):
        pass

    def list_unavailable_cabin_crew(self):
        pass
