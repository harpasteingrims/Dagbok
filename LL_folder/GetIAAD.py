class GetIAAD():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_available_emp_by_date(self, user_input_date):
        employee_list = self.ioapi.get_list_of_all_employees()
        voyage_list = self.ioapi.get_all_voyages_list()
        for time_object in voyage_list:
            employees_workin_list = []
            if time_object.time == user_input_date:
                pass  #Hvernig er best að tengja saman employees og ferðirnar þeirra

    def list_unavailable_emp_by_date(self, user_input_date):
        pass

    def list_airplane_status_by_date(self, user_input_date):
        pass

    def list_voyages_status_by_date(self, user_input_date):
        pass