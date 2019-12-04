class CabincrewUI():
    LENGTH_STAR = 20
    def show_cabin_crew_menu(self):
         
        """ This prints out the cabin crew menu """

        print("*" * self.LENGTH_STAR)
        print("CABIN CREW MENU \n\n1 Search for a cabin crew member \n2 Print overview of cabin crew \n3 Create a new cabin crew member\nB Back\n")

        action = input("Choose action: ").lower()
        print()

        if action == "1":
            self.show_enter_name_to_search()

        elif action == "2": 
            self.show_cabincrew_overview()

        elif action == "3": 
            self.show_cabincrew_create_form()

        elif action == "b":
            return
    
    def show_enter_name_to_search(self):
        print("Search for a cabin crew member to get information")
        
        name = input("Enter name of cabincrew member: ")
        print()
        
        # info_of_cabincrew_member = # Calls the class that holds the information of cabin crew member and prints it
        """ Name:
            Role:
            Social security number:
            Adress:
            Mobile number:
            Email: 
        """

        print("1 {}'s flight schedule").format(name)
        print("2 Edit information about cabin crew member \nB Back")

        action = input("Choose action: ").lower()
        print()

        if action == "1":
            self.show_flight_schedule_of_cabincrew_member(name)

        elif action == "2": 
            self.show_cabincrew_member_edit_form(name)

        elif action == "b":
            self.show_cabin_crew_menu()
            
    def show_flight_schedule_of_cabincrew_member(self, name):
        """ Calls a class that makes a list of his voyages """
        date_from = input("Enter date from: ")
        date_to = input("Enter date to: ")

        # calls the class that makes a list of the lfight schedule and prints it

        print("B Back")

        action = input("Choose action: ").lower()
        print()

        if action == "b":
            self.show_cabin_crew_menu()

    def show_cabincrew_member_edit_form(self, name):
        """ This prints out the edit form for an employee """

        # name, ssn, role.... = #calls the class to get the info of the flight attendant
        
        print("You are changing the information for cabin crew member: {}, {}".format(name, ssn))
       
        new_address = input("Enter new address")
        new_mobile_number = input("Enter new mobile number: ")
        new_email = input("Enter new email: ")
        
        print("S Save \nB Back\n")

        action = input("Choose action: ").lower()
        print()

        if action == "s":
            """ Takes the new info, changes and adds it to the cabin crew list"""
            
            # calls the class that stores the info about the cabin crew to change it...
            print("cabin crew member's information successfully changed")
            
            

        elif action == "b":

            self.show_cabin_crew_menu()
     
    def show_cabincrew_member_overview(self):
        """ This prints out the cabin crew list """

        print("OVERVIEW OF CABIN VREW\n")
        # Calls the class that makes a list of all cabin crew and prints it 

        print("B Back\n")

        action = input("Choose action: ").lower()
        print()

        if action == "b":
            self.show_cabin_crew_menu()
    
    def show_cabincrew_member_create_form(self):
        """ This prints out the cabin crew member format to put in the information """

        print("CREATE A NEW CABIN CREW MEMBER\n")
        name = input("Enter full name: ")
        role = input("Enter role: ")
        ssn = input("Enter social security number: ")
        address = input("Enter address: ")
        mobile_number = input("Enter mobile number: ")
        email = input("Enter email: ")
        new_cabincrew_member = CabincrewModel(name, role, ssn, address, mobile_number, email)
        #self.??
        
        print("\nS Save \nB Back \n")

        action = input("Choose action: ").lower()
        print()

        if action == "s":
            """ Takes the info and adds it to the cabin crew list"""
            #calls the method that adds the info to a list of flight attendant
            
            print("Cabin crew member successfully created\n")
            self.show_cabincrew_menu()

        elif action == "b":
            self.show_cabincrew_menu()