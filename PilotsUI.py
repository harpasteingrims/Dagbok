class PilotsUI():

    @classmethod
    def show_pilot_menu(cls):
        """ This prints out the cabin crew menu """
        print("PILOT MENU \n\n1 Search for a pilot \n2 Print overview of pilots \n3 Create a new pilot\nB Back\n")

        action = input("Choose action: ")
        print()

        if action == "1":
            PilotsUI.show_enter_name_to_search()

        elif action == "2": 
            PilotsUI.show_pilots_overview()

        elif action == "3": 
            PilotsUI.show_pilot_create_form()

        elif action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_employee_menu()

    @classmethod
    def show_enter_name_to_search(cls):
        print("Search for a pilot to get information")
        
        name = input("Enter name of pilot: ")
        print()
        
        # info_of_pilot = # Calls the class that holds the information of pilots and prints it
        """ Name 
            Social security number
            Adress:
            Home number:
            Mobile number:
            Email:
            License type: 
        """

        print("1 {}'s flight schedule").format(name)
        print("2 Edit information about pilot \nB Back")

        action = input("Choose action: ")
        print()

        if action == "1":
            PilotsUI.show_flight_schedule_of_pilot(name)

        elif action == "2": 
            PilotsUI.show_pilot_edit_form(name)

        elif action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_pilot_menu()

    @classmethod
    def show_flight_schedule_of_pilot(cls, name):
        """ Calls a class that makes a list of his voyages """
        date_from = input("Enter date from: ")
        date_to = input("Enter date to: ")

        # calls the class that makes a list of the lfight schedule and prints it

        print("B Back")

        action = input("Choose action: ")
        print()

        if action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_pilot_menu()

    @classmethod
    def show_pilot_edit_form(cls, name):
        """ This prints out the edit form for an employee """

        # name, ssn, .... = #calls the class to get the info of the pilot 
        
        print("You are changing the information for pilot: {}, {}".format(name, ssn))
       
        new_address = input("Enter new address")
        new_home_number = input("Enter new home number: ")
        new_mobile_number = input("Enter new mobile number: ")
        new_email = input("Enter new email: ")
        new_licence_type = input("Enter new license type: ")
        
        print("S Save \nB Back\n")

        action = input("Choose action: ")
        print()

        if action == "S":
            """ Takes the new info, changes and adds it to the pilot list"""
            
            # calls the class that stores the info about the pilot to change it...
            print("Pilot's information successfully changed")
            
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_pilot_menu()

        elif action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_pilot_menu()
     
    @classmethod
    def show_pilots_overview(cls):
        """ This prints out the pilot list """
        print("OVERVIEW OF PILOTS\n")
        # Calls the class that makes a list of all pilots and prints it 
        print("B Back\n")

        action = input("Choose action: ")
        print()
        
        if action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_pilot_menu()
    
    @classmethod
    def show_pilot_create_form(cls):
        """ This prints out the pilot format to put in the pilot information """

        print("CREATE A NEW PILOT \n")
        name = input("Enter full name: ")
        ssn = input("Enter social security number: ")
        address = input("Enter address: ")
        home_number = input("Enter home number: ")
        mobile_number = input("Enter mobile number: ")
        email = input("Enter email: ")
        licence_type = input("Enter license type: ")
        
        print("\nS Save \nB Back\n")

        action = input("Choose action: ")
        print()

        if action == "S":
            """ Takes the info and adds it to the pilot list"""
            #calls the method that adds the info to a list of pilots
            
            print("Pilot successfully created\n")
            PilotsUI.show_pilot_menu()

        elif action == "B":
            PilotsUI.show_pilot_menu()
