
class DestinationsUI():
    LENGTH_STAR = 20
    def __init__(self):
        pass
    
    def show_destination_menu(self):
        """ This prints out the menu for destinations """
        print("*"*self.LENGTH_STAR)
        print("DESTINATIONS\n")
        print("1 Print overview of destinations \n2 Create a new destination \n3 Get emergency contact ")
        print("B back\n")
        action = input("Choose action: ").lower()

        if action == "1":
            self.show_destination_overview()
        elif action == "2":
            self.show_create_des_form()
        elif action == "3":
            self.show_emerg_country_menu()
        elif action == "b":
            return

    def show_destination_overview(self):
        """ This prints all the destination """
        print("*"*self.LENGTH_STAR)
        print("OVERVIEW OF DESTINATIONS\n")
        #print(destinations)
        #HÉR ÞARF ÉG AÐ SÆKJA SKRÁ 

        print("B back\n")
        action = input("Choose action: ").lower() 
        if action == "b":
            return
            #self.show_destination_menu()

    def show_create_des_form(self):
        """ This prints the create destination form"""
        print("*"*self.LENGTH_STAR)
        print("CREATE A NEW DESTINATION\n")
        country = input("Enter country: ")
        airport = input("Enter airport: ")
        flight_duration = input("Enter flight duration from Iceland: ")
        distance = input("Enter distance from Iceland: ")
        contact = input("Enter name of contact: ")
        contact_phone = input("Enter emergency contact")
        new_destination = Destinations(country, airport, flight_duration, distance, contact, contact_phone)
        self.??.create_destination(new_destination)

        new_dest = {}
        new_dest[country] = [airport, flight_duration, distance, contact, contact_phone]

        action = input("Choose action: ").lower() 
        #if action == "s" or action == "S":
            #from UI-layer import FALL SEM VINNUR MEÐ ÞETTA
        if action == "b": #Á AÐ VERA ELIF HÉR 
            return

    def show_emerg_country_menu(self):
        """ This prints out the emergency contact menu """
        print("*"*self.LENGTH_STAR)
        print("GET EMERGENCY CONTACT\n")
        #tekur inn countries_list
        #counter = 1
        #find_country = {}
        #finc_country_list = []
        #for country in countries_list:
            #print(counter," ",country)
            #find_country[counter] = country
            #find_country_list.append(find_country)
            #country += 1

        print("B back")
        action = input("Choose action: ").lower()
        
        if action == "b":
            return 

    def show_emergency_contact(self):
        """ This prints out the emergency contact for a specific country """
        print("*"*self.LENGTH_STAR)
        print("EMERGENCY CONTACT OF", country,"\n")
        #ÞARF AÐ FINNA LANDIÐ MEÐ ÞVÍ AÐ SÆKJA LISTA AF CONTACTS Í LL-LAYER
        #CONTACTS ERU GEYMDIR Í DICT MEÐ LAND SEM KEY, FINN NAFN SEM 
        #ER SAMA NAFN OG VALUE 
        # info_of_contact = # Calls the class that holds the information of contact and prints it
        # Name:
        # Phone:
        print("1 Edit contact \n2 B Back")
        action = input("Choose action: ").lower()

        if action == "1":
            self.show_emerg_country_menu()
        elif action == "2":
            self.show_emergency_cont_form()
        elif action == "b":
            return
            
    def show_emergency_cont_form(self):
        """ This prints out the emergency contact form """
        #ÞARF AÐ FINNA LANDIÐ MEÐ ÞVÍ AÐ SÆKJA LISTA AF CONTACTS Í LL-LAYER
        #CONTACTS ERU GEYMDIR Í DICT MEÐ LAND SEM KEY, FINN NAFN SEM 
        #ER SAMA NAFN OG VALUE 
        print("*"*self.LENGTH_STAR)
        print("EDIT CONTACT \n")
        name = input("Name: ")
        phone = input("Phone: ")
        #ÉG HLÝT AÐ FÁ INN DICT HÉR ÚR LL-LAYER. ÉG ÞARF ÞÁ AÐ BREYTA HENNI EFTIR ÞVÍ HVAÐ NOTANDINN GERÐI
        #nafniðádict[land] = [name, phone]
        print("S save \nB Back")
        action = input("Choose action: ").lower()
        
        #if action == "s":
            #sendi dict í listann af dict contacts í LL-layer
        if action == "b": #Á AÐ VERA ELIF HÉR
            return






