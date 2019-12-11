from models.DestinationsModel import DestinationsModel
from LL_folder.LLAPI import LLAPI

class DestinationsUI():
    LENGTH_STAR = 20

    def __init__(self, llapi):
        self.llapi = llapi
    
    def choose_action(self):
        action_str = input("Choose action: ").lower()
        print()
        return action_str

    def show_destination_menu(self):
        """This prints the destination menu"""

        action_str = ""

        while True:
            
            print(self.LENGTH_STAR * "*")
            print("DESTINATION MENU\n")

            print("1 Print overview of destinations")
            print("2 Create a new destination")
            print("3 Edit information about destination")
            print("B Back\n")
            
            action_str = self.choose_action()

            if action_str == "1":
                self.show_destination_overview()

            elif action_str == "2":
                self.show_create_desti_form()

            elif action_str == "3":
                self.show_edit_country_menu()

            elif action_str == "b":
                return
                
            else:
                print("Invalid action!")


    def show_destination_overview(self):
        """This prints the overview of all destinations"""

        print("*"*self.LENGTH_STAR)
        print("OVERVIEW OF DESTINATIONS\n")

        counter = self.print_desti_list("*")
        print(f"NAN AIR flies to {counter} destinations")

        print("\nB Back\n")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_create_desti_form(self):
        """ This prints the create a destination form"""

        print("*" * self.LENGTH_STAR)
        print("CREATE A NEW DESTINATION\n")

        country = self.get_country()
        airport = self.get_airport()
        flight_duration = self.get_flight_duration()
        distance = self.get_distance()
        contact = self.get_contact()
        contact_number = self.get_contact_number()
        destiID = self.llapi.get_destiID()

        print("\nS Save \nB Back\n")

        action_str = self.choose_action()
        
        if action_str == "s":
            #Takes the info and adds it to the destination list
            
            new_destination_object = DestinationsModel(country, airport, flight_duration, distance, contact, contact_number, destiID)
            self.llapi.create_new_destination(new_destination_object)
            
            print(f"Destination {new_destination_object.country} successfully created\n")
            return

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def get_input_number(self):
        """ Gets an number from user and checks if it is right """
        destinations_ob_list = self.llapi.get_destination_overview()
        user_input = input("\nChoose a number of country to edit the information: ")
        
        try:
            user_input_int = int(user_input)
            if user_input_int and 1 <= user_input_int <= len(destinations_ob_list):
                chosen_country_ob = destinations_ob_list[user_input_int-1]
                return chosen_country_ob

        except ValueError:
            print("\nInvalid input!")
            return self.get_input_number()

    def print_desti_list(self, str_infront):
        
        destinations_ob_list = self.llapi.get_destination_overview() #Hérna kallar hann í fall í llapanum sem heitir get_destinations_overview sem returnar lista yfir alla áfangastaði
        
        counter = 0

        for desti_ob in destinations_ob_list:
            if str_infront == "*":
                print(desti_ob.print_destinations(str_infront))

            else:
                print(desti_ob.print_destinations(str_infront))
                str_infront += 1
            
            counter += 1
        
        return counter


    def show_edit_country_menu(self):
        """This prints the emergency contact menu"""

        print("*"*self.LENGTH_STAR)
        print("EDIT INFORMATION ABOUT DESTINATION\n")
        
        self.print_desti_list(1)
        chosen_country_ob = self.get_input_number()

        print("*"*self.LENGTH_STAR)
        print(chosen_country_ob.print_emergency())

        name = self.llapi.check_name()
        emergency_num = self.llapi.check_mobile_number()
        print("\nB Back\n")
        action_str = self.choose_action()
        
        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_emergency_contact(self):
        """This prints the emergency contact for a specific country"""

        print("*"*self.LENGTH_STAR)
        print("EMERGENCY CONTACT OF\n") #Hérna vantar að setja inn country
        #ÞARF AÐ FINNA LANDIÐ MEÐ ÞVÍ AÐ SÆKJA LISTA AF CONTACTS Í LL-LAYER
        #CONTACTS ERU GEYMDIR Í DICT MEÐ LAND SEM KEY, FINN NAFN SEM 
        #ER SAMA NAFN OG VALUE 
        # info_of_contact = # Calls the class that holds the information of contact and prints it
        # Name:
        # Phone:

        print("1 Edit contact \n2 B Back")

        action_str = self.choose_action()

        if action_str == "1":
            self.show_emerg_country_menu()
        elif action_str == "2":
            self.show_emergency_cont_form()
        elif action_str == "b":
            return
        else:
            print("Invalid action!")
            action_str = self.choose_action()
            
    def show_emergency_cont_form(self):
        """This prints the edit form for an emergency contact"""
        
        print("*"*self.LENGTH_STAR)
        print("EDIT CONTACT \n")
        name = input("Name: ")
        phone = input("Phone: ")
    
        print("S Save \nB Back\n")
        
        action_str = self.choose_action()
        
        if action_str == "s":
            #Takes the new info, changes and adds it to the emergency contact list
            #Calls the class that stores the info about the emergency contact to change it... 
            print("Emergency contact information successfully changed")
            return

        elif action_str == "b":
            return

        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def get_country(self):
        country = input("Enter country: ")
        country_check = self.llapi.check_country(country)

        if country_check:
            return country_check

        else:
            print("\nInvalid country")
            self.get_country()

    def get_airport(self):
        airport = input("Enter airport: ")
        airport_check = self.llapi.check_airport(airport)

        if airport_check:
            return airport_check

        else:
            print("\nInvalid airport")
            self.get_airport()

    def get_flight_duration(self):
        flight_duration = input("Enter flight duration (hh:mm): ")
        flight_duration_check = self.llapi.check_flight_duration(flight_duration)

        if flight_duration:
            return flight_duration

        else:
            print("\nInvalid flight duration")
            self.get_flight_duration()

    def get_distance(self):
        distance = input("Enter distance from Iceland (x km): ")
        distance_check = self.llapi.check_distance(distance)

        if distance_check:
            return distance_check

        else:
            print("\nInvalid distance")
            self.get_distance()

    def get_contact(self):
        contact = input("Enter emergency contact name: ")
        contact_check = self.llapi.check_name(contact)

        if contact_check:
            return contact_check

        else:
            print("\nInvalid contact")
            self.get_contact()

    def get_contact_number(self):
        contact_number = input("Enter emergency contact phone number: ")
        contact_number_check = self.llapi.check_contact_number(contact_number)

        if contact_number_check:
            return contact_number_check

        else:
            print("\nInvalid emergency contact phone number: ")
            self.get_contact_number()