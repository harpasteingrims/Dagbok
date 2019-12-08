from models.PilotModel import PilotsModel
import datetime
class PilotsUI():
    LENGTH_STAR = 20

    def __init__(self, llapi):
        self.llapi = llapi


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
        
        for pilot in pilots_ob_list:
            print(f"{pilot.name}, {pilot.role}, {pilot.SSN}, {pilot.mobile_number}, {pilot.email}")
        
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
        same_named_pilots = self.llapi.get_common_named_pilots_by_name(input_name)
        
        return same_named_pilots, input_name


    def get_number_from_user(self, numbered_pilot_dict):
        """ Gets an number from user and checks if it is right """

        input_number = input("\nChoose the number you want: ")
        print()

        try:
            if int(input_number) in numbered_pilot_dict:
                return int(input_number)
        
        except ValueError or False: 
            print("Not a valid number!")
            self.get_number_from_user(numbered_pilot_dict)


    def show_enter_name_to_search(self):
        """ This prints the search for a pilot window """

        print(self.LENGTH_STAR * "*")
        print("SEARCH FOR A PILOT\n")
         
        same_named_pilots, input_name = self.get_pilot_name_and_common_list()
        
        if same_named_pilots == False:
            print("Pilot does not exist")
            same_named_pilots, input_name = self.get_pilot_name_and_common_list()
        
        counter = 1
        
        if len(same_named_pilots) == 1:
            pilot_object = same_named_pilots[0]
            print(pilot_object.print_pilot_info())
                
        else:
 
            numbered_pilot_dict = self.llapi.get_numbered_employee_dict(same_named_pilots)
            
            for number, pilot_object in numbered_pilot_dict.items():
                print(f"{number} {pilot_object.name}")

            input_number = int(self.get_number_from_user(numbered_pilot_dict))

            pilot_object = self.llapi.get_employee_object_from_numbered_dict(numbered_pilot_dict, input_number)
            print(pilot_object.print_pilot_info())
            print()

        print(f"\n1{pilot_object.name}'s flight schedule")
        print("2 Edit information about pilot")
        print("B Back")

        action_str = self.choose_action()

        if action_str == "1":
            self.show_flight_schedule_of_pilot(pilot_object)

        elif action_str == "2": 
            self.show_pilot_edit_form(pilot_object)

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
    

    def show_flight_schedule_of_pilot(self, pilot_object):
        """Calls a class that makes a list of their voyages and prints it"""
        
        # eftir að klára

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
        print(f"{pilot_object.name}'S FLIGHT SCHEDULE")

        flights_object = self.llapi.get_schedule_pilot_by_date(pilot_object, date_from, date_to)
        
        #vantar kóða hér


        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()


    def show_pilot_edit_form(self, pilot_object):
        """This prints the edit form for an employee"""
        
        print(self.LENGTH_STAR * "*")
        print("EDIT PILOT")

        print(pilot_object.print_pilot_info())

        print(f"You are changing the information for pilot: {pilot_object.name}, {pilot_object.SSN}")
       
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
            return

        elif action_str == "b":
            return

        else:
            print("Invalid action!")
            action_str = self.choose_action()
    
    def get_name(self):
        name = input("Enter full name: ").capitalize()
        name_check = self.llapi.check_name(name)
        
        if name_check:
            return name
            
        else:
            print("invalid name")
            self.get_name()


    def get_pilot_rank(self):
        rank = input("Enter rank, either Captain or Copilot: ").capitalize()
        rank_check = self.llapi.check_pilot_rank(rank)

        if rank_check:
            return rank
        
        else:
            print("Invalid rank")
            self.get_pilot_rank()


    def get_ssn(self):
        ssn = input("Enter social security number: ")
        ssn_check = self.llapi.check_ssn(ssn)

        if ssn_check:
            return ssn
        
        else:
            print("Invalid SSN")
            self.get_ssn()
    

    def get_address(self):
        address = input("Enter address in form; zip code address name house number: ").capitalize()
        address_check = self.llapi.check_address(address)

        if address_check:
            return address
        
        else:
            print("Invalid address")
            self.get_address()


    def get_mobile_number(self):
        mobile_number = input("Enter mobile number: ")
        mobile_number_check = self.llapi.check_mobile_number(mobile_number)

        if mobile_number_check:
            return mobile_number
        
        else:
            print("Invalid mobile_number")
            self.get_mobile_number()
    

    def get_email(self):
        email = input("Enter email: ").capitalize()
        email_check = self.llapi.check_email(email)

        if email_check:
            return email
        
        else:
            print("Invalid email")
            self.get_email()


    def get_license_type(self):
        license_type = input("Enter license type: ").capitalize()
        license_type_check = self.llapi.check_license_type(license_type)

        if license_type_check:
            return license_type
        
        else:
            print("Invalid license_type")
            self.get_license_type()


    def show_pilot_create_form(self):
        """ This prints the create a pilot form """

        print(self.LENGTH_STAR * "*")
        print("CREATE A NEW PILOT \n")

        name = self.get_name()
        rank = self.get_pilot_rank()
        ssn = self.get_ssn()
        address = self.get_address()
        mobile_number = self.get_mobile_number()
        email = self.get_email()
        license_type = self.get_license_type()

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
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()