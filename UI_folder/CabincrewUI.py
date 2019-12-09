from models.CabinCrewModel import CabinCrewModel
import datetime

class CabincrewUI():
    LENGTH_STAR = 20

    def __init__(self, llapi, employeesUI):
        self.llapi = llapi
        self.employeesUI = employeesUI

    def choose_action(self):
        """ Asks the user for an action and returns it """

        action_str = input("Choose action: ").lower()
        print()

        return action_str


    def show_cabincrew_menu(self):
        """ This prints the cabin crew member menu """

        while True:
            print()
            print(self.LENGTH_STAR * "*")
            print("CABIN CREW MENU")
            print()
            print("1 Print overview of cabin crew")
            print("2 Search for a cabin crew member")
            print("3 Create a new cabin crew member")
            print("B Back")
            print()

            action_str = self.choose_action()

            if action_str == "1":
                self.show_cabincrew_member_overview()

            elif action_str == "2":
                self.show_enter_name_to_search()

            elif action_str == "3":
                self.show_cabincrew_member_create_form()

            elif action_str == "b":
                return

            else:
                print("Invalid action!")


    def show_cabincrew_member_overview(self):
        """This prints the overview of all pilots"""

        print(self.LENGTH_STAR * "*")
        print("OVERVIEW OF CABIN CREW\n")
        # Calls the class that makes a list of all cabin crew members and prints it 
        cabin_crew_ob_list = self.llapi.get_cabin_crew_overview()
        for member in cabin_crew_ob_list:
            print(f"{member.name}, {member.role}, {member.ssn}, {member.mobile_number}, {member.email}")
        
        print("B Back\n")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def get_crew_member_name_and_common_list(self):

        input_name = input("Enter name of cabin crew member: ").lower()
        print()
        same_named_crew_members = self.llapi.get_common_named_crew_members(input_name)
        
        return same_named_crew_members, input_name


    def get_number_from_user(self, numbered_crew_member_dict):
        """ Gets an number from user and checks if it is right """

        input_number = input("\nChoose the number you want: ")
        print()

        try:
            if int(input_number) in numbered_crew_member_dict:
                return int(input_number)
        
        except ValueError or False: 
            print("Not a valid number!")
            self.get_number_from_user(numbered_crew_member_dict)


    def show_enter_name_to_search(self):
        """This prints the search for a cabin crew member window"""

        print(self.LENGTH_STAR * "*")
        print("SEARCH FOR A CABIN CREW MEMBER\n")

        same_named_crew_members, input_name = self.get_crew_member_name_and_common_list()

        if same_named_crew_members == False:
            print("Crew member does not exist")
            same_named_crew_members, input_name = self.get_crew_member_name_and_common_list()
        
        counter = 1
        
        if len(same_named_crew_members) == 1:
            crew_member_object = same_named_crew_members[0]
            print(crew_member_object.print_crew_member_object_info())
                
        else:
 
            numbered_crew_member_dict = self.llapi.get_numbered_employee_dict(same_named_crew_members)
            
            for number, crew_member_object in numbered_crew_member_dict.items():
                print(f"{number} {crew_member_object.name}")

            input_number = int(self.get_number_from_user(numbered_crew_member_dict))

            crew_member_object = self.llapi.get_employee_object_from_numbered_dict(numbered_crew_member_dict, input_number)
            print(crew_member_object.print_pilot_info())
            print()

        print(f"\n1{crew_member_object.name}'s flight schedule")
        print("2 Edit information about pilot")
        print("B Back")

        action_str = self.choose_action()

        if action_str == "1":
            self.show_flight_schedule_of_cabincrew_member()

        elif action_str == "2":
            self.show_cabincrew_member_edit_form()

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()


    def show_flight_schedule_of_cabincrew_member(self, crew_member_object):
        """Calls a class that makes a list of their voyages and prints it"""

        print(self.LENGTH_STAR * "*")

        print("Enter date from")
        year_from = input("Enter year from: ")
        month_from = input("Enter month from: ")
        day_from = input("Enter day from: ")
        date_from = datetime.datetime(year_from, month_from, day_from, 0, 0, 0).isoformat()

        print("Enter date to")
        year_to = input("Enter year to:")
        month_to = input("Enter month to: ")
        day_to = input("Enter day to: ")
        date_to = datetime.datetime(year_to, month_to, day_to, 23, 59, 0).isoformat()


        print(self.LENGTH_STAR * "*")
        print(f"{crew_member_object.name}'S FLIGHT SCHEDULE")

        flights_object = self.llapi.get_schedule_crew_member_by_date(pilot_object, date_from, date_to)
        
        #vantar kóða hér


        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
    
    def show_cabincrew_member_edit_form(self, crew_member_object):
        """This prints the edit form for a cabin crew member"""
        
        print(self.LENGTH_STAR * "*")
        print("EDIT CABIN CREW MEMBER")
        print(pilot_object.print_pilot_info())

        print(f"You are changing the information for pilot: {crew_member_object.name}, {crew_member_object.ssn}")
       
        new_address = self.employeesUI.get_address()
        new_rank = self.employeesUI.get_crew_member_rank()
        mobile_number = self.employeesUI.get_mobile_number()
        new_email = self.employeesUI.get_email()
        
        print("S Save \nB Back\n")

        action_str = self.choose_action()

        if action_str == "s":
            updated_crew_member_object = [crew_member_object.ssn, crew_member_object.name, new_rank, new_address, mobile_number, new_email]
            
            updated_crew_member = self.llapi.update_new_crew_member_information(updated_crew_member_object)
            

            print("Crew member's information successfully changed\n")

            return 

        elif action_str == "b":
            return

        else:
            print("Invalid action!")
            action_str = self.choose_action()

    
    def show_cabincrew_member_create_form(self):
        """This prints the create a cabin crew member form"""

        print(self.LENGTH_STAR * "*")
        print("CREATE A NEW CABIN CREW MEMBER\n")
        name = self.employeesUI.get_name()
        rank = self.employeesUI.get_cabin_crew_rank()
        ssn = self.employeesUI.get_ssn()
        address = self.employeesUI.get_address()
        mobile_number = self.employeesUI.get_mobile_number()
        email = self.employeesUI.get_email()
       

        print("\nS Save \nB Back \n")

        action_str = self.choose_action()

        if action_str == "s":
            new_crew_member_object = CabinCrewModel(ssn, name, "Cabin crew", rank, address, mobile_number, email)
            added_to_file = self.llapi.create_new_cabin_crew(new_crew_member_object)

            print(f"Crew member {new_crew_member_object.name} successfully created\n")

            return 

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
