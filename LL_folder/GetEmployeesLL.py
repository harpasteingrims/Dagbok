class GetEmployeesLL():
    
    def __init__(self, ioapi):
        self.ioapi = ioapi
        self.avaliable_employees = []
        self.unavaliable_employees = []
    
    """ EMPLOYEES """

    def list_all_employees(self):
        """ Calls the IOAPI to get a list of all employees """
    
        return self.ioapi.get_list_of_all_employees()
    
    
    def list_schedule_employee_by_date(self, employee_ob, date_from, date_to):
        flights_ob_list = self.llapi.get_voyages_overview()

        employees_flights = []

        for flight_ob in flights_ob_list:
            if employee_ob.ssn in flight_ob.crew_list:
                employees_flights.append(flight_ob)
        
        pass

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
            first_name , last_name = pilot_object.name.split()
            
            if first_name.lower() == name.lower() or last_name.lower() == name.lower():

                common_pilot_names.append(pilot_object)
    
        if len(common_pilot_names) > 0:
            return common_pilot_names
        else:
            return False


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

        
   