


class IAADUI():
    
    def __init__(self):
        pass

    def show_enter_date(self):
        print("\n")
        user_input_date = input("Enter a date: ")
        print("\n")
        self.show_IAAD_menu()
        """ This prints out, input date """
        pass

    def show_available_employees(self):
        """ This prints out the available employees from a certain date """
        print("this is a list of available employees")
        print("\n")
        print("B Back")
        user_input = self.choose_action()
        if user_input == "b":
            self.show_IAAD_menu()
        pass

    def show_unavailable_employees(self):
        """ This prints out the unavailable employees from a certain date """
        print("this is a list of unavailable employees")
        print("\n")
        print("B Back")
        user_input = self.choose_action()
        if user_input == "b":
            self.show_IAAD_menu()
        pass

    def show_airplane_status(self):
        """ This prints out the status of a airplane from a certain date """
        print("this is a list of airplanes and their status")
        print("\n")
        print("B Back")
        user_input = self.choose_action()
        if user_input == "b":
            self.show_IAAD_menu()
        pass
   
    def show_voyages_status(self):
        """ This prints out the status of a voyage from a certain date """
        print("this is a list of voyages and their status")
        print("\n")
        print("B Back")
        user_input = self.choose_action()
        if user_input == "b":
            self.show_IAAD_menu()
        pass


    def show_IAAD_menu(self):
        """ This prints out the information about a date menu """
        print("IAAD")
        print("1 Available Employees","\n2 Unavailable Employees","\n3 Status of voyages","\n4 Status of Airplanes","\nB Back")

        user_input = self.choose_action()

        if user_input == "1":
            self.show_available_employees()
        elif user_input == "2":
            self.show_unavailable_employees()
        elif user_input == "3":
            self.show_voyages_status()
        elif user_input == "4":
            self.show_airplane_status()
        elif user_input == "b":
            return
            
  
    def choose_action(self):
        print("\n")
        user_action = input("Choose action: ").lower()
        return user_action


