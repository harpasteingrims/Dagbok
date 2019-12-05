
class IAADUI():
    
    def __init__(self, llapi):
        self.llapi = llapi

    def show_enter_date(self):
        print("\n")
        user_input_date = input("Enter a date: ")
        print("\n")
        self.show_IAAD_menu(user_input_date)
        """ This prints out, input date """
        return user_input_date

    def show_available_employees(self, user_input_date):
        """ This prints the available employees from a certain date """
        print("this is a list of available employees")
        available_employess = self.llapi.get_available_emp_by_date()
        print(available_employess)

        print("\n")
        print("B Back")
        user_input = self.choose_action()
        if user_input == "b":
            self.show_IAAD_menu(user_input_date)
        pass

    def show_unavailable_employees(self, user_input_date):
        """ This prints the unavailable employees from a certain date """
        print("this is a list of unavailable employees")
        unavailable_employess = self.llapi.get_unavailable_emp_by_date()
        print(unavailable_employess)
        print("\n")
        print("B Back")
        user_input = self.choose_action()
        if user_input == "b":
            self.show_IAAD_menu(user_input_date)
        pass

    def show_airplane_status(self, user_input_date):
        """ This prints the status of a airplane from a certain date """
        print("this is a list of airplanes and their status")
        airplane_status = self.llapi.get_airplane_status_by_date()
        print(airplane_status)
        print("\n")
        print("B Back")
        user_input = self.choose_action()
        if user_input == "b":
            self.show_IAAD_menu(user_input_date)
        pass
   
    def show_voyages_status(self, user_input_date):
        """ This prints the status of a voyage from a certain date """
        print("this is a list of voyages and their status")
        voyage_status = self.llapi.get_voyages_status_by_date()
        print(voyage_status)
        print("\n")
        print("B Back")
        user_input = self.choose_action()
        if user_input == "b":
            self.show_IAAD_menu(user_input_date)
        pass


    def show_IAAD_menu(self, user_input_date):
        """ This prints the information about a date menu """
        print("IAAD")
        print("1 Available Employees","\n2 Unavailable Employees","\n3 Status of voyages","\n4 Status of Airplanes","\nB Back")

        user_input = self.choose_action()

        if user_input == "1":
            self.show_available_employees(user_input_date)
        elif user_input == "2":
            self.show_unavailable_employees(user_input_date)
        elif user_input == "3":
            self.show_voyages_status(user_input_date)
        elif user_input == "4":
            self.show_airplane_status(user_input_date)
        elif user_input == "b":
            return
            
  
    def choose_action(self):
        print("\n")
        user_action = input("Choose action: ").lower()
        return user_action