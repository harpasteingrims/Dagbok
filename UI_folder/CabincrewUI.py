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
            print("CABIN CREW MENU\n")

            print("1 Print overview of cabin crew")
            print("2 Search for a cabin crew member")
            print("3 Create a new cabin crew member")
            print("B Back\n")
    
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
        
        counter = 1
        for member in cabin_crew_ob_list:
            print(member.print_crew_member_info_in_line(counter))
            counter += 1
        
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

        common_named_crew_members_list = self.llapi.get_common_named_crew_members(input_name)
        
        return common_named_crew_members_list, input_name


    def get_number_from_user(self, common_named_crew_members_list):
        """ Gets an number from user and checks if it is right """

        user_input = input("\nChoose a number for Crew member's information: ")
        
        try:
            user_input_int = int(user_input)
            if user_input_int and 1 <= user_input_int <= len(common_named_crew_members_list):
                chosen_crew_member_ob = common_named_crew_members_list[crew_member_ob_number-1]
                return chosen_crew_member_ob
            
            else:
                else:
                print("\nInvalid input!")
                self.get_input_number(common_named_crew_members_list)

        except ValueError:
            print("\nInvalid number!")
            self.get_number_from_user(common_named_crew_members_list)


    def show_enter_name_to_search(self):
        """This prints the search for a cabin crew member window"""

        print(self.LENGTH_STAR * "*")
        print("SEARCH FOR A CABIN CREW MEMBER\n")

        common_named_crew_members_list, input_name = self.get_crew_member_name_and_common_list()

        while common_named_crew_members_list == False:
            print("Crew member does not exist")
            common_named_crew_members_list, input_name = self.get_crew_member_name_and_common_list()
        
        counter = 1
        
        if len(common_named_crew_members_list) == 1:
            crew_member_ob = common_named_crew_members_list[0]
            print()
            print(crew_member_ob.print_crew_member_object_info())
                
        else:
 
            counter = 1
            for crew_member_ob in common_named_crew_members_list:

                print(crew_member_ob.print_crew_member_object_info(counter))

                counter += 1 

            crew_member_ob = self.get_the_right_pilot_ob(common_named_pilots_list)

            print()
            print(crew_member_ob.print_crew_member_object_info())

        print(f"\n1 {crew_member_ob.name}'s flight schedule")
        print(f"2 Edit information about {crew_member_ob.name}")
        print("B Back\n")

        action_str = self.choose_action()

        if action_str == "1":
            self.employeesUI.show_flight_schedule_of_employee(crew_member_ob)

        elif action_str == "2":
            self.show_cabincrew_member_edit_form(crew_member_ob)

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
    

    def show_cabincrew_member_edit_form(self, crew_member_ob):
        """This prints the edit form for a cabin crew member"""
        
        print(self.LENGTH_STAR * "*")
        print("EDIT CABIN CREW MEMBER")
        
        print(f"You are changing the information for crew member:\n")
        print(crew_member_ob.print_pilot_info())
        print()

        new_address = self.employeesUI.get_address()
        mobile_number = self.employeesUI.get_mobile_number()
        new_email = self.employeesUI.get_email()
        
        print("\nS Save \nB Back\n")

        action_str = self.choose_action()

        if action_str == "s":
            updated_crew_member_ob = CabinCrewModel(crew_member_ob.ssn, crew_member_ob.name, crew_member_ob.role, crew_member_ob.rank, new_address, mobile_number, new_email)
            
            updated_crew_member = self.llapi.update_new_crew_member_information(updated_crew_member_ob)
            
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
            self.llapi.create_new_cabin_crew(new_crew_member_object)
            print(f"Crew member {new_crew_member_object.name} successfully created\n")
            return 

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
