from models.DestinationsModel import DestinationsModel
from LL_folder.LLAPI import LLAPI

class DestinationsUI():
    LENGTH_STAR = 20

    def __init__(self, llapi):
        self.llapi = llapi
    
    def choose_action(self, valid_list):
        """Gets a list of valid actions and asks the user for an action and if the action is in the valid actions it returns it else it returns False"""
        action_str = input("Choose action: ").lower()
        print()
        
        if action_str in valid_list:
            return action_str
            
        else:
            print("Invalid action!")
            return False
            
    def get_input_number(self, ob_list):
        """Asks user for a number, sends to InputCheck and then returns it"""
        
        chosen_number = input("\nChoose a number: ")
        chosen_object = self.llapi.check_chosen_number(chosen_number, ob_list)
        
        if chosen_object:
            return chosen_object

        else:
            print("\nInvalid input!")
            self.get_input_number(ob_list)

    def show_destination_menu(self):
        """Prints the destination menu"""

        action_str = ""

        while True:
            
            print(self.LENGTH_STAR * "*")
            print("DESTINATION MENU\n")
            print("1 Print overview of destinations")
            print("2 Create a new destination")
            print("3 Edit information about destination")
            print("B Back\n")
            
            action_str = self.choose_action(["1", "2", "3", "b"])
            while action_str == False:
                action_str = self.choose_action(["1", "2", "3", "b"])

            if action_str == "1":
                self.show_destination_overview()

            elif action_str == "2":
                self.show_create_desti_form()

            elif action_str == "3":
                self.show_edit_desti_menu()

            elif action_str == "b":
                return

    def show_destination_overview(self):
        """Prints the overview of all destinations"""

        print("*"*self.LENGTH_STAR)
        print("OVERVIEW OF DESTINATIONS")

        counter = self.print_desti_list("*")
        print(f"\nNAN AIR flies to {counter} destinations")

        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        while action_str == False:
                action_str = self.choose_action(["b"])

        if action_str == "b":
            return

    def show_create_desti_form(self):
        """Prints the create a destination form and calls the methods to get the information it needs"""

        print("*" * self.LENGTH_STAR)
        print("CREATE A NEW DESTINATION\n")
        
        print("B Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
                action_str = self.choose_action(["b", "c"])
        if action_str == "b":
            return
        elif action_str == "c":

            country = self.get_country()
            while country == False:
                country = self.get_country()
            airport = self.get_airport()
            while airport == False:
                airport = self.get_airport()
            flight_duration = self.get_flight_duration()
            while flight_duration == False:
                flight_duration = self.get_flight_duration()
            distance = self.get_distance()
            while distance == False:
                distance = self.get_distance()
            contact = self.get_contact()
            while contact == False:
                contact = self.get_contact()
            contact_number = self.get_contact_number()
            while contact_number == False:
                contact_number = self.get_contact_number()
            destiID = self.llapi.get_destiID()

            print("\nS Save \nB Back\n")

            action_str = self.choose_action(["b", "s"])
            while action_str == False:
                action_str = self.choose_action(["b", "s"])
            
            if action_str == "s":
                new_destination_object = DestinationsModel(country, airport, flight_duration, distance, contact, contact_number, str(destiID))
                self.llapi.create_new_destination(new_destination_object)
                
                print(f"Destination {new_destination_object.country} successfully created\n")
                return

            elif action_str == "b":
                return

    def print_desti_list(self, str_infront):
        """Prints the overview of destinations either with * in front of or counter depending on whether you want to just see the overview or select a destination to edit"""
        
        destinations_ob_list = self.llapi.get_destination_overview()
        
        counter = 0
        for desti_ob in destinations_ob_list:
            if str_infront == "*":
                print(desti_ob.print_destinations(str_infront))
            else:
                print(desti_ob.print_destinations(str_infront))
                str_infront += 1
            
            counter += 1
        return counter

    def show_edit_desti_menu(self):
        """This prints the emergency contact menu"""

        print("*"*self.LENGTH_STAR)
        print("EDIT INFORMATION ABOUT DESTINATION\n")
        
        print("B Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
            action_str = self.choose_action(["b", "c"])
        
        if action_str == "b":
            return
        elif action_str == "c":
            destinations_ob_list = self.llapi.get_destination_overview()
            self.print_desti_list(1)
            chosen_destination_ob = self.get_input_number(destinations_ob_list)
            print("\n" + "*" * self.LENGTH_STAR)
            print(f"EDIT {chosen_destination_ob.country.upper()}, {chosen_destination_ob.airport.upper()}'S INFO")
                
            print(f"\n1 Edit {chosen_destination_ob.country.capitalize()}, {chosen_destination_ob.airport.capitalize()}'s contact name")
            print(f"2 Edit {chosen_destination_ob.country.capitalize()}, {chosen_destination_ob.airport.capitalize()}'s contact number")
            print("\nB Back")

            action_str = self.choose_action(["1","2","b"])
            while action_str == False:
                action_str = self.choose_action(["1","2","b"])

            self.show_edit_desti_form(chosen_destination_ob, action_str)

    def show_edit_desti_form(self, chosen_destination_ob, action_str):
        """Prints the edit destination form"""

        if action_str == "1":
            print(self.LENGTH_STAR * "*")
            print(f"You are changing {chosen_destination_ob.country.capitalize()}, {chosen_destination_ob.airport.capitalize()}'s contact name\nThe current address is: {chosen_destination_ob.contact_name}\n")
            new_name = self.get_contact()
            while new_name == False:
                new_name = self.get_contact()
            self.check_action_edit_form(chosen_destination_ob, action_str, new_name)

        elif action_str == "2":
            print(self.LENGTH_STAR * "*")
            print(f"You are changing {chosen_destination_ob.country.capitalize()}, {chosen_destination_ob.airport.capitalize()}'s emergency phone number\nThe current address is: {chosen_destination_ob.contact_phone_number}\n")
            new_emergency_num = self.get_contact_number()
            while new_emergency_num == False:
                new_emergency_num = self.get_contact_number()
            self.check_action_edit_form(chosen_destination_ob, action_str, new_emergency_num)

        elif action_str == "b":
            return

    def check_action_edit_form(self, chosen_destination_ob, number, new_info):
        """Receives changes info from the edit menu and sends it too LLAPI where it then goes on to change in the csv file"""
        
        print("\nS Save \nB Back\n")
        action_str = self.choose_action(["s","b"])
        while action_str == False:
            action_str = self.choose_action(["s", "b"])

        if action_str == "s":
            if number == "1":
                updated_destination = DestinationsModel(chosen_destination_ob.country, chosen_destination_ob.airport, chosen_destination_ob.flight_dur_from_Ice, chosen_destination_ob.dist_from_Ice, new_info, chosen_destination_ob.contact_phone_number, chosen_destination_ob.destiID)
            elif number == "2":
                updated_destination = DestinationsModel(chosen_destination_ob.country, chosen_destination_ob.airport, chosen_destination_ob.flight_dur_from_Ice, chosen_destination_ob.dist_from_Ice, chosen_destination_ob.contact_name, new_info, chosen_destination_ob.destiID)
            print(f"Emergency contact of {chosen_destination_ob.country} information successfully changed\n")
            self.llapi.update_new_emerg_contact(updated_destination)
        
        elif action_str == "b":
            return

    """The get methods below ask the user for a certain input, sends it to InputCheck and then returns it"""
    
    def get_country(self):
        country = input("Enter country: ")
        country_check = self.llapi.check_country(country)

        if country_check:
            return country_check

        else:
            print("\nInvalid country")
            return country_check

    def get_airport(self):
        airport = input("Enter airport: ")
        airport_check = self.llapi.check_airport(airport)

        if airport_check:
            return airport_check

        else:
            print("\nInvalid airport")
            return airport_check

    def get_flight_duration(self):
        flight_duration = input("Enter flight duration {hh:mm}: ")
        flight_duration_check = self.llapi.check_flight_duration(flight_duration)

        if flight_duration_check:
            return flight_duration_check

        else:
            print("\nInvalid flight duration")
            return flight_duration_check

    def get_distance(self):
        distance = input("Enter distance from Iceland {x km}: ")
        distance_check = self.llapi.check_distance(distance)

        if distance_check:
            return distance_check

        else:
            print("\nInvalid distance")
            return distance_check

    def get_contact(self):
        contact = input("Enter emergency contact name {first name} {last name}: ")
        contact_check = self.llapi.check_name(contact)

        if contact_check:
            return contact_check

        else:
            print("\nInvalid contact")
            return contact_check

    def get_contact_number(self):
        contact_number = input("Enter emergency contact phone number: ")
        contact_number_check = self.llapi.check_mobile_number(contact_number)

        if contact_number_check:
            return contact_number_check

        else:
            print("\nInvalid emergency contact phone number: ")
            return contact_number_check