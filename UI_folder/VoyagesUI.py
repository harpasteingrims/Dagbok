from models.VoyagesModel import VoyagesModel
from LL_folder.LLAPI import LLAPI

class VoyagesUI():
    LENGTH_STAR = 20
    def __init__(self, llapi):
        self.llapi = llapi
    
    def show_overview_voyage(self):
        """ This prints the overview of all voyages """
        print("\n{}".format(self.LENGTH_STAR*"*"))
        print("OVERVIEW OF VOYAGES")
        voyages = self.llapi.get_voyages_overview() #Kallar á fall i llapanum sem returnar öllum vinnuferðum
        print(voyages)

    def show_voyage_menu(self):
        """ This prints out the voyage menu """
        print(self.LENGTH_STAR*"*")
        print("VOYAGES \n\n1 Print overview of voyages\n2 Create a voyage\n3 Assign crew to flights\nB Back")
        print()
        action_str = input("Choose action: ").lower()
        if action_str == "1":
            self.show_overview_voyage()
        elif action_str == "2":
            self.show_create_voyage_menu()
        elif action_str == "3":
            self.show_not_staffed_voyages()
        elif action_str == "b":
            return

    def show_assign_staff_form(self):
        """ This prints out the form to assign a staff to a voyage """
        print("\n{}".format(self.LENGTH_STAR*"*"))
        print("ASSIGN CREW TO VOYAGES")
        print("\nB Back") #Kannski sleppa
        #Listi yfir alla lausa pilots og þar þarf IO og fá date til að sjá hverjir eru lausar þennan dag
        pilot = input("Enter a pilot: ")
        #Listi yfir alla lausa cabincrew
        cabincrew = input("Enter a cabincrew: ")
        
        print()
        
        #Þurfum meira hér til að klára þetta fall

    def show_create_voyage_menu(self):
        """ This prints out the menu for create a voyage """
        print("\n{}".format(self.LENGTH_STAR*"*"))
        print("CREATE A VOYAGE \n\n1 See common voyages\n2 Create a voyage manually\nB Back")
        print()
        action_str = input("Choose action: ").lower()
        if action_str == "1":
            self.show_see_common()
        elif action_str == "2":
            self.show_create_manually_form()
        elif action_str == "b":
            self.show_create_voyage_menu()
    
    def show_see_common(self):
        """ This prints out all the common voyages """
        print("\n{}".format(self.LENGTH_STAR*"*"))
        print("SEE COMMON VOYAGES")
        self.llapi.get_common_voyages() #Þessi listi þarf að vera númeraður

    def create_a_common_voyage(self):
        """ This creates a voyage from the common voyages but with a new date and a new id """
        pass #Eftir að klára þetta :)

    def show_create_manually_form(self): #Lista upp alla áfangastaði allar tímasetningar sem eru uppteknar allar flugvélar sem eru lausar
        """ This prints out the form to add a voyage manually """
        print("\n{}".format(self.LENGTH_STAR*"*"))
        print("CREATE A VOYAGE MANUALLY")
        print("\nDate")
        voyage_date = input("Enter outbound departure date(dd/mm/yy): ")
        print("\nTime")
        voyage_time = input("Enter outbound departure time(hh:mm): ")
        print("\nDestination")
        voyage_destination = input("Enter destination: ")
        print("\nAirplane")
        voyage_airplane = input("Enter airplane: ")

        print("\n1 Assign crew to voyage\nS Save\nB Back")
        print()
        action_str = input("Choose action: ").lower()
        if action_str == "1":
            self.show_assign_staff_form()
        elif action_str == "s":
            print("\n*Voyage successfully created*")
            new_voyage = VoyagesModel(voyage_date, voyage_time, voyage_destination, voyage_airplane)
            self.show_create_voyage_menu()
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá
        elif action_str == "b":
            self.show_create_voyage_menu()

    def show_available_airplane(self):
        """ This prints all the available airplanes for a voyage """
        pass
    
    def show_time_from_iceland(self):
        """ This prints the flight time from Iceland for the flight """
        pass 

    def show_date_from_iceland(self):
        """ This prints what date is for the flight """
        pass 

    def show_destinations(self):
        """ This prints all the destinations """
        pass 

    def show_not_staffed_voyages(self):
        """ This prints out all the not fully staffed voyages that are available """
        not_staffed = self.llapi.get_not_staffed_voyages() #Þessi listi þarf að vera númeraður
        print(not_staffed)
        voyage_str = input("Choose a voyage")
        self.show_assign_staff_form() #Hérna fer ég með voyage_str í fallið
        