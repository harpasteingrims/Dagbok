from models.PilotModel import PilotsModel
class PilotsUI():
    LENGTH_STAR = 20

    def __init__(self, llapi):
        self.llapi = llapi

    def choose_action(self):
        action_str = input("Choose action: ").lower()
        print()
        return action_str

    def show_pilot_menu(self):
        '''This prints the pilot menu'''

        while True:
            print()
            print(self.LENGTH_STAR * "*")
            print("PILOT MENU")
            print()
            print("1 Print overview of pilots")
            print("2 Search for a pilot")
            print("3 Create a new pilot")
            print("B Back")
            print()

            action_str = self.choose_action()
        
            if action_str == "1":
                self.show_pilots_overview()

            elif action_str == "2": 
                self.show_enter_name_to_search()

            elif action_str == "3": 
                self.show_pilot_create_form()

            elif action_str == "b":
                return

            else:
                print("Invalid action!")  

    def show_enter_name_to_search(self):
        """This prints the search for a pilot window"""

        print(self.LENGTH_STAR * "*")
        print("SEARCH FOR A PILOT\n")
        
        name = input("Enter name of pilot: ").lower()
        print()
        
        same_named_pilots = self.llapi.get_common_named_pilots_by_name(name)

        counter = 1
        
        if len(same_named_pilots) == 1:
            pilot_object = same_named_pilots[0]
            print(pilot_object.print_pilot_info())
                
        else:
 
            numbered_pilot_dict = self.llapi.get_numbered_pilot_dict(same_named_pilots)
            for number, pilot_object in numbered_pilot_list.items():
                print(f"{key} {pilot_object.name}")

            input_number = input("\nPick the right one: ")
            
            pilot_object = self.llapi.get_pilot_object_from_numbered_dict(numbered_pilot_dict, input_name)

        print("1 {}'s flight schedule").format(pilot_object.name)
        print("2 Edit information about pilot \nB Back")

        action_str = self.choose_action()

        if action_str == "1":
            self.show_flight_schedule_of_pilot(name)

        elif action_str == "2": 
            self.show_pilot_edit_form(name)

        elif action_str == "b":
            self.show_pilot_menu()
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
    
    def show_flight_schedule_of_pilot(self, name):
        """Calls a class that makes a list of their voyages and prints it"""

        date_from = input("Enter date from: ")
        date_to = input("Enter date to: ")

        print(self.LENGTH_STAR * "*")
        #print("{}'S FLIGHT SCHEDULE").format(name.upper())
        flight_schedule = self.llapi.get_schedule_pilot_by_date()
        #Herna þarf name ad fara inn
        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            self.show_pilot_menu()
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_pilot_edit_form(self, name):
        """This prints the edit form for an employee"""
        
        print(self.LENGTH_STAR * "*")
        print("EDIT PILOT")
        # name, ssn, role.... = #calls the class to get the info of the pilot 
        #print("You are changing the information for pilot: {}, {}".format(name, ssn))
       
        new_address = input("Enter new address")
        new_mobile_number = input("Enter new mobile number: ")
        new_email = input("Enter new email: ")
        new_licence_type = input("Enter new license type: ")
        
        print("S Save \nB Back\n")

        action_str = self.choose_action()

        if action_str == "s":
            #Takes the new info, changes and adds it to the pilot list
            #Calls the class that stores the info about the pilot to change it...
            print("Pilot's information successfully changed")
            self.show_pilot_menu()

        elif action_str == "b":
            self.show_pilot_menu()
        else:
            print("Invalid action!")
            action_str = self.choose_action()
     
    def show_pilots_overview(self):
        """This prints the overview of all pilots"""

        print(self.LENGTH_STAR * "*")
        print("OVERVIEW OF PILOTS\n")
        # Calls the class that makes a list of all pilots and prints it 
        pilots_ob_list = self.llapi.get_pilot_overview()
        for pilot in pilots_ob_list:
            print(f"{pilot.name}, {pilot.role}, {pilot.SSN}, {pilot.mobile_number}, {pilot.email}")
        
        print("B Back\n")

        action_str = self.choose_action()
        
        if action_str == "b":
            self.show_pilot_menu()
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
    
    def show_pilot_create_form(self):
        """This prints the create a pilot form"""

        print(self.LENGTH_STAR * "*")
        print("CREATE A NEW PILOT \n")
        name = input("Enter full name: ")
        role = input("Enter role: ")
        ssn = input("Enter social security number: ")
        address = input("Enter address: ")
        mobile_number = input("Enter mobile number: ")
        email = input("Enter email: ")
        license_type = input("Enter license type: ")
        
        print("\nS Save \nB Back\n")

        action_str = self.choose_action()

        if action_str == "s":
            #Takes the info and adds it to the pilot list
            print("Pilot successfully created\n")
            #new_pilot = PilotModel(name, role, ssn, address, mobile_number, email, license_type)
            #self.pilot.create_pilot(new_pilot)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá        
            self.show_pilot_menu()

        elif action_str == "b":
            self.show_pilot_menu()
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()