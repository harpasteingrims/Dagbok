from UI_folder.UImanager import UImanager
from models.CabinCrewModel import CabinCrewModel

class CabincrewUI():
    LENGTH_STAR = 20
    def __init__(self, llapi):
        self.llapi = llapi

    def show_cabincrew_menu(self):
        """ This prints the cabin crew member menu """

        action_str = ""
        while(action_str != "q"):
            print(self.LENGTH_STAR * "*")
            print("CABIN CREW MENU")
            print("1 Search for a cabin crew member")
            print("2 Print overview of cabin crew")
            print("3 Create a new cabin crew member")
            print("B Back")
            print("Q Quit")
            action_str = input("Choose action: ").lower()
            print()

            if action_str == "1":
                self.show_enter_name_to_search()
            elif action_str == "2":
                self.show_cabincrew_member_overview()
            elif action_str == "3":
                self.show_cabincrew_member_create_form()
            elif action_str == "b":
                return

    def show_enter_name_to_search(self):
        """This prints the search for a cabin crew member window"""

        print(self.LENGTH_STAR * "*")
        print("SEARCH FOR A CABIN CREW MEMBER")

        name = input("Enter name of cabin crew member: ")
        print()

        cabincrew_info = self.llapi.get_info_about_cabincrew_by_name()
        print(cabincrew_info)
            #Name:
            #Role:
            #Social security number:
            #Adress:
            #Mobile number:
            #Email:

        print("1 {}'s flight schedule".format(name))
        print("2 Edit information about cabin crew member \nB Back")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "1":
            self.show_flight_schedule_of_cabincrew_member()

        elif action_str == "2":
            self.show_cabincrew_member_edit_form()

        elif action_str == "b":
            self.show_cabincrew_menu

    def show_flight_schedule_of_cabincrew_member(self):
        """Calls a class that makes a list of their voyages and prints it"""

        print(self.LENGTH_STAR * "*")
        data_from = input("Enter date from: ")
        date_to = input("Enter date to: ")

        #print("{}'S FLIGHT SCHEDULE").format(name.upper)
        cabincrew_schedule = self.llapi.get_schedule_pilot_by_date()
        print(cabincrew_schedule)

        print("B Back")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "b":
            self.show_cabincrew_menu
    
    def show_cabincrew_member_edit_form(self):
        """This prints the edit form for a cabin crew member"""
        
        print(self.LENGTH_STAR * "*")
        print("EDIT CABIN CREW MEMBER")
        # name, ssn, role.... = #calls the class to get the info of the cabin crew member 
        #print("You are changing the information for cabin crew member: {}, {}".format(name, ssn))
        
        new_address = input("Enter new address")
        new_mobile_number = input("Enter new mobile number: ")
        new_email = input("Enter new email: ")

        print("S Save \nB Back\n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "s":
            #Takes the new info, changes and adds it to the cabin crew member list
            #Calls the class that stores the info about the cabin crew member to change it...
            print("Cabin crew member's information successfully changed")
            self.show_cabincrew_menu

        elif action_str == "b":
            self.show_cabincrew_menu

    def show_cabincrew_member_overview(self):
        """This prints the overview of all pilots"""

        print(self.LENGTH_STAR * "*")
        print("OVERVIEW OF CABIN CREW\n")
        # Calls the class that makes a list of all cabin crew members and prints it 
        cabin_crew = self.llapi.get_cabin_crew_overview()
        print(cabin_crew)
        
        print("B Back\n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "b":
            self.show_cabincrew_menu
    
    def show_cabincrew_member_create_form(self):
        """This prints the create a cabin crew member form"""

        print(self.LENGTH_STAR * "*")
        print("CREATE A NEW CABIN CREW MEMBER\n")
        name = input("Enter full name: ")
        role = input("Enter role: ")
        ssn = input("Enter social security number: ")
        address = input("Enter address: ")
        mobile_number = input("Enter mobile number: ")
        email = input("Enter email: ")

        print("\nS Save \nB Back \n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "s":
            #Takes the info and adds it to the cabin crew member list
            print("Cabin crew member successfully created\n")
            #new_cabincrew_member = CabinCrewModel(name, role, ssn, address, mobile_number, email)
            #self.cabincrew_member.create_cabincrew_member(new_cabincrew_member)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá        
            self.show_cabincrew_menu

        elif action_str == "b":
            self.show_cabincrew_menu