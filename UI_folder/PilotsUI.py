from models.PilotModel import PilotsModel
import datetime
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


    def show_pilots_overview(self):
        """ Prints the overview of all pilots"""
        
        print(self.LENGTH_STAR * "*")
        print("OVERVIEW OF PILOTS\n")
        
        pilots_ob_list = self.llapi.get_pilot_overview() # Calls the class that makes a list of all pilots and prints it
        
        counter = 1
        for pilot_ob in pilots_ob_list:
            print(pilot_ob.print_pilot_info_in_line(counter))
            counter += 1
        
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


    def get_the_right_pilot_ob(self, common_named_pilots):
        """ Gets an number from user and checks if it is right """
        
        pilot_ob_number = int(input("\nChoose a number for pilot's information: "))
        
        try:
            if pilot_ob_number and 1 <= pilot_ob_number <= len(common_named_pilots):
                chosen_pilot_ob = common_named_pilots[pilot_ob_number-1]
                return chosen_pilot_ob

        except ValueError:
            print("\nInvalid number!")
            self.get_number_from_user(common_named_pilots)


    def show_enter_name_to_search(self):
        """ This prints the search for a pilot window """

        print(self.LENGTH_STAR * "*")
        print("\nSEARCH FOR A PILOT\n")
        
        common_named_pilots_list, input_name = self.get_pilot_name_and_common_list()
        
        while common_named_pilots_list == False:
            print("Pilot does not exist!\n")
            common_named_pilots_list, input_name = self.get_pilot_name_and_common_list()
        
        if len(common_named_pilots_list) == 1:
            pilot_ob = same_named_pilots[0]
            print()
            print(pilot_ob.print_pilot_info())

        else: 
            
            counter = 1
            for pilot_ob in common_named_pilots_list:

                print(pilot_ob.print_pilot_info_in_line(counter))

                counter += 1 

            pilot_ob = self.get_the_right_pilot_ob(common_named_pilots_list)

            print()
            print(pilot_ob.print_pilot_info())

        print(f"\n1 {pilot_ob.name}'s flight schedule")
        print(f"2 Edit information about {pilot_ob.name}")
        print("B Back\n")

        action_str = self.choose_action()

        if action_str == "1":
            self.show_flight_schedule_of_pilot(chosen_pilot_ob)

        elif action_str == "2": 
            self.show_pilot_edit_form(chosen_pilot_ob)

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
    

    def show_flight_schedule_of_pilot(self, pilot_ob):
        """Calls a class that makes a list of their voyages and prints it"""
         
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
        print(f"{pilot_ob.name}'S FLIGHT SCHEDULE")
        
        flight_schedule = self.llapi.get_employee_schedule_by_date(pilot_ob, date_from, date_to)
    
        #vantar kóða hér


        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()


    def show_pilot_edit_form(self, pilot_ob):
        """This prints the edit form for an employee"""
        
        print(self.LENGTH_STAR * "*")
        print("EDIT PILOT")

        print(pilot_ob.print_pilot_info())

        print(f"You are changing the information for pilot: {pilot_ob.name}, {pilot_ob.ssn}")
       
        new_address = self.employeesUI.get_address()
        new_rank = self.employeesUI.get_pilot_rank()
        mobile_number = self.employeesUI.get_mobile_number()
        new_email = self.employeesUI.get_email()
        new_license_type = self.employeesUI.get_license_type()
        
        print("S Save \nB Back\n")

        action_str = self.choose_action()

        if action_str == "s":
            updated_pilot_ob = PilotsModel(ssn, name, rank, ssn, address, mobile_number, email, license_type)
            
            updated_pilot = self.llapi.update_new_pilot_information(updated_pilot_ob)
            
            print("Pilot's information successfully changed")
            return

        elif action_str == "b":
            return

        else:
            print("Invalid action!")
            action_str = self.choose_action()


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