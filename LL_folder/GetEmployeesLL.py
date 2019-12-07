class GetEmployeesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        self.avaliable_employees = []
        self.unavaliable_employees = []
    

    """ EMPLOYEES """

    def list_all_employees(self):
        """ Calls the IOAPI to get a list of all employees """
        
        return self.ioapi.get_list_of_all_employees()
    
    def list_available_employees(self,date_from, date_to):
        
        """ Calls the IOAPI to get a list of all employees """
        all_employee_list = self.get_all_employees()

        # flokka þá sem eru að vinna á ákv dagsetningu.......
        return avaliable_employees

    def list_unavailable_employees(self,date):
        
        
        #all_employee_list = self.ioapi.get_list_of_all_employees()
        
        # flokka þá sem ekki eru að vinna....

        return unavaliable_employees
    

    """ PILOTS """

    def list_all_pilots(self):
        """ Calls the IOAPI to get a list of all pilots """
        
        return self.ioapi.get_list_of_all_pilots()


    def list_all_cabin_crew(self):
        """ Calls the IOAPI to get a list of the whole cabin crew """

        return self.ioapi.get_list_of_all_cabin_crew()
    

    def find_common_named_pilots(self, name):
        common_pilot_names = []
        pilot_list = self.list_all_pilots()
        
        for pilot_object in pilot_list:
            first_name, last_name = pilot_object.name.split()
            if first_name.lower() == name.lower() or last_name.lower() == name.lower():
                
                common_pilot_names.append(pilot_object)
        
        if len(common_pilot_names) > 0:
            return common_pilot_names
        else:
            return False


    def make_numbered_pilot_dict(self, pilot_list):
        
        numbered_pilot_dict = {}
        counter = 1

        for pilot_object in pilot_list:
                
            numbered_pilot_dict[counter] = pilot_object

            counter += 1

        return numbered_pilot_dict


    def get_pilot_object_from_numbered_dict(self, numbered_pilot_dict, input_number):
        
        for number, pilot_object in numbered_pilot_dict.items():
            if number == input_number:
                return pilot_object
    
    
    def list_schedule_pilot_by_date(self, pilot_object, date_from, date_to):
        # unnið úr date og búið ti lista af voyages sem viðkamandi er á og á gefna tímabilinu
        # eftir að klára
        pass


    def list_unavaliable_pilots(self):
        pass


    def list_available_pilots(self):
        pass

    
    """ CABIN CREW """

    def find_common_named_cabincrew(self,name):
        common_crew_names = []
        cabin_crew_list = self.list_all_cabin_crew()
        
        for cabin_crew_object in cabin_crew_list:
            if cabin_crew_object.name == name:
                
                common_crew_names.append(cabin_crew_object)

        if len(common_crew_names) > 0:
            return common_crew_names

        else:
            return False


    def list_info_about_cabincrew_by_name(self, name):

        cabin_crew_list = self.list_all_cabin_crew()

        for cabin_crew_object in cabin_crew_list:
            if cabin_crew_object.name == name:
                return cabin_crew_object

        
    def list_schedule_cabincrew_by_date(self, name, date_from, date_to):
        # unnið úr date og búið ti lista af voyages sem viðkamandi er á og á gefna tímabilinu
        
        pass
    
    
    def list_available_cabin_crew(self):
        pass


    def list_unavailable_cabin_crew(self):
        pass
    
