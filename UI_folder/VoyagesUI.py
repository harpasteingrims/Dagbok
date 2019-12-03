class VoyagesUI():
    LENGTH_STAR = 20
    def __init__(self):
        pass
    
    def show_overview_voyage(self):
        """ This prints the overview of all voyages """
        print("\n{}".format(self.LENGTH_STAR*"*"))
        print("OVERVIEW OF VOYAGES")
        print("\nflugvel lala")

    def show_voyage_menu(self):
        """ This prints out the voyage menu """
        print(self.LENGTH_STAR*"*")
        print("VOYAGES")
        print()
        print("1 Print overview of voyages\n2 Create a voyage\n3 Assign crew to flights\nB Back")
        print()
        action_str = input("Choose action: ")
        if action_str == "1":
            self.show_overview_voyage()
        elif action_str == "2":
            self.show_create_voyage_menu()
        elif action_str == "3":
            self.show_not_staffed_voyages()
        elif action_str == "B" or action_str == "b":
            from MainmenuUI import MainmenuUI
            MainmenuUI.show_main_menu()

    def show_assign_staff_form(self):
        """ This prints out the form to assign a staff to a voyage """
        print("\n{}".format(self.LENGTH_STAR*"*"))
        print("ASSIGN CREW TO VOYAGES")
        self.show_not_staffed_voyages()
        print("B Back")
        print()
        voyage_str = input("Choose a voyage")
        #Þurfum meira hér til að klára þetta fall

    def show_create_voyage_menu(self):
        """ This prints out the menu for create a voyage """
        print("\n{}".format(self.LENGTH_STAR*"*"))
        print("CREATE A VOYAGE")
        print()
        print("1 See common voyages\n2 Create a voyage manually\nB Back")
        print()
        action_str = input("Choose action: ")
        if action_str == "1":
            self.show_see_common()
        elif action_str == "2":
            self.show_create_manually_form()
        elif action_str == "B" or action_str == "b":
            self.show_create_voyage_menu()
    
    def show_see_common(self):
        """ This prints out all the common voyages """
        print("\n{}".format(self.LENGTH_STAR*"*"))
        print("SEE COMMON VOYAGES")

    def show_create_manually_form(self):
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

        voyage_dict = {}
        voyage_dict[voyage_destination] = [voyage_date, voyage_time, voyage_airplane]
        print("\n1 Assign crew to voyage\nS Save\nB Back")
        print()
        action_str = input("Choose action: ")
        if action_str == "1":
            self.show_assign_staff_form()
        elif action_str == "S" or action_str == "s":
            print("\n*Voyage successfully created*")
            self.show_create_voyage_menu()
            pass #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá
        elif action_str == "B" or action_str == "b":
            self.show_create_voyage_menu()

    def show_available_airplane(self):
        """ This prints out all the available airplanes for a voyage """
        pass
    
    def show_time_from_iceland(self):
        """ This prints the flight time from Iceland for the flight """
        pass 

    def show_date_from_iceland(self):
        """ This prints what date is for the flight """
        pass 

    def show_destinations(self):
        """ This prints out all the destinations """
        pass 

    def show_not_staffed_voyages(self):
        """ This prints out all the not fully staffed voyages that are available """
        #Vantar meira hér til þess að klára


