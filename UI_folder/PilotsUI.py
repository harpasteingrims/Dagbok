from models.PilostModel import PilotsModel
class PilotsUI():
    LENGTH_STAR = 20

    def __init__(self, llapi, employeesUI):
        self.llapi = llapi
        self.employeesUI = employeesUI


    def choose_action(self):
        """ Asks the user for an action and returns it """
        action_str = input("Choose action: ").lower()
        print()

        return action_str


    def show_pilot_menu(self):
        """ Prints the pilot menu and calls appropriate functions or prints Invalid action"""

        while True:
            print(self.LENGTH_STAR * "*")
            print("PILOT MENU\n")
            
            print("1 Print overview of pilots")
            print("2 Search for a pilot")
            print("3 Create a new pilot")
            print("B Back\n")

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


    def show_pilots_overview(self):
        """ Prints the overview of all pilots"""
        
        print(self.LENGTH_STAR * "*")
        print("OVERVIEW OF PILOTS\n")
        
        pilots_ob_list = self.llapi.get_pilot_overview() # Calls the class that makes a list of all pilots and prints it
        
        for pilot_ob in pilots_ob_list:
            print(pilot_ob.to_csv_string())
        
        print("\nB Back\n")

        action_str = self.choose_action()
        
        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()


    def get_pilot_name_and_common_list(self):
        
        input_name = input("Enter name of pilot: ").lower()
        print()

        common_named_pilots_list = self.llapi.get_common_named_pilots(input_name)
    
        return common_named_pilots_list, input_name


    def get_input_number(self, common_named_pilots_list):
        """ Gets an number from user and checks if it is right """
        
        user_input = input("\nChoose a number for pilot's information: ")
        try:
            user_input_int = int(user_input)
            if user_input_int and 1 <= user_input_int <= len(common_named_pilots_list):
                chosen_pilot_ob = common_named_pilots_list[user_input_int-1]
                return chosen_pilot_ob

            else:
                print("\nInvalid input!")
                self.get_input_number(common_named_pilots_list)


        except ValueError:
            print("\nInvalid input!")
            self.get_input_number(common_named_pilots_list)
        
    
    def show_enter_name_to_search(self):
        """ This prints the search for a pilot window """
         
        print(self.LENGTH_STAR * "*")
        print("SEARCH FOR A PILOT\n")
        
        while True:
        
            common_named_pilots_list, input_name = self.get_pilot_name_and_common_list()
            
            while common_named_pilots_list == False:
                print("Pilot does not exist!\n")
                common_named_pilots_list, input_name = self.get_pilot_name_and_common_list()
            
            if len(common_named_pilots_list) == 1:
                pilot_ob = common_named_pilots_list[0]
                print()
                print(pilot_ob.print_pilot_info())

            else: 
                counter = 1
                for pilot_ob in common_named_pilots_list:

                    print(pilot_ob.print_pilot_info_in_line())
                    counter += 1
                pilot_ob = self.get_input_number(common_named_pilots_list)

        
            print()
            print(self.LENGTH_STAR * "*")
            print(f"{pilot_ob.name}'S INFO\n")
            print(pilot_ob.print_pilot_info())
        
        
            print(f"\n1 {pilot_ob.name}'s flight schedule")
            print(f"2 Edit information about {pilot_ob.name}")
            print("B Back\n")

            action_str = self.choose_action()

            if action_str == "1":
                self.employeesUI.show_flight_schedule_of_employee(pilot_ob)

            elif action_str == "2": 
                self.show_pilot_edit_form(pilot_ob)

            elif action_str == "b":
                return
            
            else:
                print("Invalid action!")
                action_str = self.choose_action()


    def show_pilot_edit_form(self, pilot_ob):
        """This prints the edit form for an employee"""
        
        print(self.LENGTH_STAR * "*")
        print("EDIT PILOT\n")
        
        print(f"You are changing the information for pilot:\n")
        print(pilot_ob.print_pilot_info())
        print()

        new_address = self.employeesUI.get_address()
        mobile_number = self.employeesUI.get_mobile_number()
        new_email = self.employeesUI.get_email()
        
        print("\nS Save \nB Back\n")
        self.check_action_edit_form()

    def check_action_edit_form(self):
        action_str = self.choose_action()

        if action_str == "s":
            updated_pilot_ob = PilotsModel(pilot_ob.ssn, pilot_ob.name, "Pilot", pilot_ob.rank, pilot_ob.license_type, new_address, mobile_number, new_email)
            
            print(f"{updated_pilot_ob.name}'s information successfully changed")
            return

        elif action_str == "b":
            return

        else:
            print("Invalid action!")
            self.check_action_edit_form()


    def show_pilot_create_form(self):
        """ This prints the create a pilot form """

        print(self.LENGTH_STAR * "*")
        print("CREATE A NEW PILOT \n")

        name = self.employeesUI.get_name()
        rank = self.employeesUI.get_pilot_rank()
        ssn = self.employeesUI.get_ssn()
        address = self.employeesUI.get_address()
        mobile_number = self.employeesUI.get_mobile_number()
        email = self.employeesUI.get_email()
        license_type = self.employeesUI.get_license_type()

        print("\nS Save \nB Back\n")

        action_str = self.choose_action()

        if action_str == "s":

            new_pilot_object = PilotsModel(ssn, name, "Pilot", rank, license_type, address, mobile_number, email)
            self.llapi.create_new_pilot(new_pilot_object)
            print(f"Pilot {new_pilot_object.name} successfully created\n")
            return

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()