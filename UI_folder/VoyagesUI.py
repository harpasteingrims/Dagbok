from models.VoyagesModel import VoyagesModel
from LL_folder.LLAPI import LLAPI
import datetime

class VoyagesUI():
    LENGTH_STAR = 20
    def __init__(self, llapi):
        self.llapi = llapi
    
    def choose_action(self):
        action_str = input("Choose action: ").lower()
        print()
        return action_str
    
    def show_voyage_menu(self):
        """This prints the voyage menu"""

        action_str = ""

        while True:
            print()
            print(self.LENGTH_STAR * "*")
            print("VOYAGE MENU")
            print()
            print("1 Print overview of voyages")
            print("2 Create a voyage")
            print("3 Assign crew to flights")
            print("B Back")
            print()

            action_str = input("Choose action: ").lower()

            if action_str == "1":
                self.show_voyage_overview()
            elif action_str == "2":
                self.show_create_voyage_menu()
            elif action_str == "3":
                self.show_not_staffed_voyages()
            elif action_str == "b":
                return

    def show_voyage_overview(self):
        """This prints the overview of all voyages"""
        
        print(self.LENGTH_STAR*"*")
        print("OVERVIEW OF VOYAGES")

        voyages_ob_list = self.llapi.get_voyages_overview() #Kallar á fall i llapanum sem returnar öllum vinnuferðum og prenta út flugnúmer beggja flugferða
        for voyage_ob in voyages_ob_list:
            print(f"\n{voyage_ob.departure_time}, {voyage_ob.arrival_time}, {voyage_ob.destination}, {voyage_ob.aircraftID}, {voyage_ob.crew_list}")

        print("B Back\n")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
    
    def show_create_voyage_menu(self):
        """This prints the menu for create a voyage"""
        
        print(self.LENGTH_STAR*"*")
        print("CREATE A VOYAGE \n\n1 See common voyages\n2 Create a voyage manually\nB Back")
        print()

        action_str = self.choose_action()

        if action_str == "1":
            self.show_see_common()
        elif action_str == "2":
            self.show_create_manually_form()
        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_see_common(self):
        """This prints all the common voyages"""
        
        print(self.LENGTH_STAR*"*")
        print("SEE COMMON VOYAGES")
        self.llapi.get_common_voyages() #Þessi listi þarf að vera númeraður
        common_voyage = input("Choose a number for a common voyage: ") #Þetta fer inní create a common voyage fallið
        #Hér þarf að vera einhver counter kóði eins og í emergency contact destinations :)

    def show_create_a_common_voyage_form(self):
        """This creates a voyage from the common voyages but with a new date and a new id"""
        
        print(self.LENGTH_STAR * "*")
        print("INPUT DEPARTURE DATE AND ARIPLANE ID")
        print("Enter outbound departure date") #Hérna þarf ég að kalla á available airplanes by date
        departure_year = input("Enter departure year: ")
        departure_month = input("Enter departure month: ")
        departure_day = input("Enter departure day: ") #Hérna þarf að villutékka hvort það sé flug á þessum degi á þessum tíma
        departure_date = datetime.datetime(departure_year, departure_month, departure_day)
        airplane_id = input("Enter airplane ID: ")
        pass #Eftir að klára þetta :)

    def show_create_manually_form(self): #Lista upp alla áfangastaði allar tímasetningar sem eru uppteknar allar flugvélar sem eru lausar
        """This prints the create a voyage manually form"""
        
        print(self.LENGTH_STAR*"*")
        print("CREATE A VOYAGE MANUALLY")
        print("\nDate")
        print("Enter outbound departure date")
        voyage_year = input("Enter year: ")
        voyage_month = input("Enter month: ")
        voyage_day = input("Enter day: ")
        print("\nTime")
        unavailable_time = self.llapi.get_unavailable_time_for_voyage(voyage_year, voyage_month, voyage_day) #Þetta prentar alla tímasetningar sem eru ekki í boði
        print(unavailable_time)
        print("Enter outbound departure time")
        voyage_hour = input("Enter hour: ")
        voyage_minute = input("Enter minute: ")
        year, month, day, hour, minute = voyage_year, voyage_month, voyage_day, voyage_hour, voyage_minute
        voyage_date = datetime.datetime(year, month, day, hour, minute, 0).isoformat()
        print("\nDestination")
        airports = self.llapi.get_airport_overview() #Þetta prentar alla áfangastaði, þetta þarf að vera númerað
        print(airports)
        voyage_airport = input("Choose number of airport: ")
        print("\nAirplane")
        available_airplanes = self.llapi.get_available_airplanes_by_date(voyage_date)
        print(available_airplanes)
        voyage_airplane = input("Choose number of airplane: ")

        print("\n1 Assign crew to voyage\nS Save\nB Back\n")

        action_str = self.choose_action()

        if action_str == "1":
            #Takes the info and adds it to the voyage list
            print("\n*Voyage successfully created*")
            arrival_time = 0 #format fyrir date time
            new_voyage = VoyagesModel(voyage_date,arrival_time, voyage_airport, voyage_airplane) #Pæling að gera þetta ekki fyrr en í hinu fallinu, eða veit ekki
            #self.voyage.create_voyage(new_voyage)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá
            self.show_assign_staff_form(voyage_date, new_voyage)

        elif action_str == "s":
            #Takes the info and adds it to the voyage list
            print("\n*Voyage successfully created*")
            new_voyage = VoyagesModel(voyage_date, voyage_time, voyage_airport, voyage_airplane)
            #self.voyage.create_voyage(new_voyage)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá
            return

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_assign_staff_form(self, voyage_date, voyage):
        """This prints the form to assign a staff to a voyage"""
        
        print(self.LENGTH_STAR*"*")
        print("ASSIGN CREW TO VOYAGES")
        print("\nB Back") #Kannski sleppa
        #Listi yfir alla lausa pilots og þar þarf IO og fá date til að sjá hverjir eru lausar þennan dag
        available_employess_ob_list = self.llapi.get_available_emp_by_date(voyage_date)
        for employee_ob in available_employess_ob_list:
            print(f"\n{employee_ob.name}, {employee_ob.role}")

        captain = input("Choose number for captain: ")
        copilot = input("Choose number for copilot: ")

        senior_cabincrew_member = input("Choose number for senior cabin crew member: ")
        cabincrew_member_1 = input("Choose number for cabincrew member #1: ")
        cabincrew_member_2 = input("Chooose number for cabincrew member #2: ")
        
        print()
        
        #Þurfum meira hér til að klára þetta fall

    def show_not_staffed_voyages(self):
        """This prints all the not fully staffed voyages that are available"""
        
        print(self.LENGTH_STAR * "*")
        print("NOT FULLY STAFFED VOYAGES")
        not_staffed_ob_list = self.llapi.get_not_staffed_voyages() #Þessi listi þarf að vera númeraður
        counter = 1
        for voyage_ob in not_staffed_ob_list:
            print(f"\n{counter}. {voyage_ob.departure_time}, {voyage_ob.destination}, {voyage_ob.aircraftID}") #Pæling að gera þetta öðruvísi með númerin
            counter += 1
        
        voyage_number = self.choose_a_number()
        try:
            voyage_number = int(voyage_number)
        except ValueError:
            print("Invalid input!")
            voyage_number = self.choose_a_number()

        if 1 <= int(voyage_number) <= len(not_staffed_ob_list):
            chosen_voyage_ob = not_staffed_ob_list[voyage_number]
            self.show_assign_staff_form(chosen_voyage_ob)
        else:
            print("Invalid number!")

    
    def choose_a_number(self):
        chosen_number = input("Choose a number: ")
        return chosen_number
                
        
        