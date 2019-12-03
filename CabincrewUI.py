class CabincrewUI():

    @classmethod
    def show_cabin_crew_menu(cls):
        """ This prints out the cabin crew menu """
        print("CABIN CREW MENU \n\n 1 Search for a flight attendant \n2 Print overview of flight attendants \n3 Create a new flight attendant\n")
        print("B Back")

        action = input("Choose action: ")

        if action == "1":
            CabincrewUI.show_enter_name_to_search()

        elif action == "2": 
            CabincrewUI.show_flight_attendants_overview()

        elif action == "3": 
            CabincrewUI.show_flight_attendant_create_form()

        elif action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_employee_menu()
    
    @classmethod
    def show_enter_name_to_search(cls):
        print("Search for a flight attendant to get information")
        
        name = input("Enter name of flight attendant: ")
        
        # info_of_flight_attendant = # Calls the class that holds the information of flight attendant and prints it
        """ Name 
            Social security number
            Adress:
            Home number:
            Mobile number:
            Email: 
        """

        print("1 {}'s flight schedule").format(name)
        print("2 Edit information about flight attendant \nB Back")

        action = input("Choose action: ")

        if action == "1":
            CabincrewUI.show_flight_schedule_of_flight_attendant(name)

        elif action == "2": 
            CabincrewUI.show_flight_attendant_edit_form(name)

        elif action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_cabin_crew_menu()

    @classmethod
    def show_flight_schedule_of_flight_attendant(cls, name):
        """ Calls a class that makes a list of his voyages """
        date_from = input("Enter date from: ")
        date_to = input("Enter date to: ")

        # calls the class that makes a list of the lfight schedule and prints it

        print("B Back")

        action = input("Choose action: ")

        if action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_cabin_crew_menu()

    @classmethod
    def show_flight_attendant_edit_form(cls, name):
        """ This prints out the edit form for an employee """

        # name, ssn, .... = #calls the class to get the info of the flight attendant
        
        print("You are changing the information for flight attendant: {}, {}".format(name, ssn))
       
        new_address = input("Enter new address")
        new_home_number = input("Enter new home number: ")
        new_mobile_number = input("Enter new mobile number: ")
        new_email = input("Enter new email: ")
        
        print("S Save \nB Back\n")

        action = input("Choose action: ")
        print()

        if action == "S":
            """ Takes the new info, changes and adds it to the cabin crew list"""
            
            # calls the class that stores the info about the cabin crew to change it...
            print("flight attendant's information successfully changed")
            
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_cabin_crew_menu()

        elif action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_cabin_crew_menu()
     
    @classmethod
    def show_flight_attendants_overview(cls):
        """ This prints out the flight attendant list """

        print("OVERVIEW OF flight attendants\n")
        # Calls the class that makes a list of all flight attendants and prints it 

        pass 
    
    @classmethod
    def show_flight_attendant_create_form(cls):
        """ This prints out the flight attendant format to put in the flight attendant information """

        print("CREATE A NEW FLIGHT ATTENDANT")
        name = input("Enter full name: ")
        ssn = input("Enter social security number: ")
        address = input("Enter address: ")
        home_number = input("Enter home number: ")
        mobile_number = input("Enter mobile number: ")
        email = input("Enter email: ")
        licence_type = input("Enter license type: ")
        
        print("S Save \nB Back")

        action = input("Choose action: ")

        if action == "S":
            """ Takes the info and adds it to the flight attendant list"""
            #calls the method that adds the info to a list of flight attendant
            
            print("Flight attendant successfully created")
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_cabin_crew_menu()

        elif action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_cabin_crew_menu()
