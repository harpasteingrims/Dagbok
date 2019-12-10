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

        voyages_elem_list = self.llapi.get_voyages_overview() #Kallar á fall i llapanum sem returnar öllum vinnuferðum og prenta út flugnúmer beggja flugferða
        for voyage_elem in voyages_elem_list:
            print(f"\nDeparture time: {voyage_elem[0]}, arrival time: {voyage_elem[1]}, destination: {voyage_elem[2]}, aircraftID: {voyage_elem[3]}, #1 flight number: {voyage_elem[4]}, #2 flight number: {voyage_elem[5]}, flight status: {voyage_elem[6]}")

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
        
        print(self.LENGTH_STAR * "*")
        print("SEE COMMON VOYAGES")
        common_voyages = self.llapi.get_common_voyages()
        counter = 1
        for voyage_elem in common_voyages:
            print(f"\n{counter} {voyage_elem[0]}, {voyage_elem[1]}")
            counter += 1
        chosen_number = self.choose_a_number()

        if 1 <= int(chosen_number) <= len(common_voyages):
            chosen_voyage_elem = common_voyages[int(chosen_number)-1]
            self.show_create_a_common_voyage_form(chosen_voyage_elem)
        else:
            print("Invalid number!")
            chosen_number = self.choose_a_number()
        return chosen_voyage_elem

    def show_create_a_common_voyage_form(self, chosen_voyage_elem):
        """This creates a voyage from the common voyages but with a new date and a new id"""
        
        print(self.LENGTH_STAR * "*")
        print("INPUT DEPARTURE DATE AND ARIPLANE ID")
        print("Enter outbound departure date")
        departure_date = self.get_year_month_day(chosen_voyage_elem)
        available_airplanes_list = self.llapi.get_available_airplanes_by_date(departure_date)
        counter = 1
        for airplane_elem in available_airplanes_list:
            print(f"{counter} {airplane_elem}")
            counter += 1
        airplane_id = self.choose_a_number()
        if 1 <= int(airplane_id) <= len(available_airplanes_list):
            chosen_airplane_id = available_airplanes_list[int(airplane_id)-1]
            print("\n*Voyage successfully created*")
            new_voyage = VoyagesModel(departure_date, chosen_voyage_elem[0], chosen_airplane_id) #Á eftir að klára þetta
        else:
            print("Invalid number!")
            airplane_id = self.choose_a_number()


    def show_create_manually_form(self): #Lista upp alla áfangastaði, allar tímasetningar sem eru uppteknar og allar flugvélar sem eru lausar
        """This prints the create a voyage manually form"""
        
        print(self.LENGTH_STAR * "*")
        print("CREATE A VOYAGE MANUALLY")
        print("\n*Date*")
        print("\nEnter outbound departure date")
        voyage_year = input("Enter year: ")
        voyage_month = input("Enter month: ")
        voyage_day = input("Enter day: ")
        print("\n*Unavailable time*")
        unavailable_time = self.llapi.get_unavailable_time_for_voyage(voyage_year, voyage_month, voyage_day) #Þetta prentar alla tímasetningar sem eru ekki í boði
        for time_elem in unavailable_time:
            print(f"\n{time_elem}")
        
        print("\nEnter outbound departure time")
        voyage_hour = input("Enter hour: ")
        voyage_minute = input("Enter minute: ")
        voyage_date = datetime.datetime(int(voyage_year), int(voyage_month), int(voyage_day), int(voyage_hour), int(voyage_minute), 0).isoformat()
        print("\n*Airports*")
        airports = self.llapi.get_airport_overview() #Þetta prentar alla áfangastaði, þetta þarf að vera númerað
        counter = 1
        for airports_ob in airports:
            print(f"\n{counter} {airports_ob}")
            counter += 1
        voyage_airport = self.choose_a_number()
        print("\n*Airplane*")
        available_airplanes = self.llapi.get_available_airplanes_by_date(voyage_date)
        count = 1
        for airplane_ob in available_airplanes:
            print(f"\n{count} {airplane_ob}")
            count += 1
        voyage_airplane = self.choose_a_number()

        print("\n1 Assign crew to voyage\nS Save\nB Back\n")

        action_str = self.choose_action()

        if action_str == "1":
            print("\n*Voyage successfully created*")
            arrival_time = 0 #format fyrir date time
            new_voyage = VoyagesModel(voyage_date,voyage_airport,arrival_time = "", voyage_airport, voyage_airplane) #Pæling að gera þetta ekki fyrr en í hinu fallinu, eða veit ekki
            self.llapi.calculate_arrival_time(new_voyage)
            #self.voyage.create_voyage(new_voyage)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá
            self.show_assign_staff_form(voyage_date, new_voyage)

        elif action_str == "s":
            print("\n*Voyage successfully created*")
            new_voyage = VoyagesModel(voyage_date,voyage_airport, arrival_time = "", voyage_airplane)
            self.llapi.calculate_arrival_time(new_voyage)
            print(new_voyage)
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
        counter = 1
        for employee_ob in available_employess_ob_list:
            if employee_ob.rank == "Captain":
                print(employee_ob.print_available_pilot_info(counter))
                counter += 1
        print("\n*Pick a number for captain*")
        captain = self.choose_a_number()

        counter = 1
        for employee_ob in available_employess_ob_list:
            if employee_ob.rank == "Copilot":
                print(employee_ob.print_available_pilot_info(counter))
                counter += 1
        print("*\nPick a number for copilot*")
        copilot = self.choose_a_number()

        counter = 1
        for employee_ob in available_employess_ob_list:
            if employee_ob.rank == "FlightServiceManager":
                print(employee_ob.print_available_crew_info(counter))
                counter += 1
        print("\n*Pick a number for senior cabin crew member*")
        senior_cabincrew_member = self.choose_a_number()

        counter = 1
        for employee_ob in available_employess_ob_list:
            if employee_ob.rank == "FlightAttendant":
                print(employee_ob.print_available_crew_info(counter))
                counter += 1
        print("\n*Pick a number for cabincrew member #1*")
        cabincrew_member_1 = self.choose_a_number()
        
        counter = 1
        for employee_ob in available_employess_ob_list:
            if employee_ob.rank == "FlightAttendant":
                print(employee_ob.print_available_crew_info(counter))
                counter += 1
        print("\n*Pick a number for cabincrew member #2*")
        cabincrew_member_2 = self.choose_a_number()
        
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

        if 1 <= int(voyage_number) <= len(not_staffed_ob_list):
            chosen_voyage_ob = not_staffed_ob_list[int(voyage_number)-1]
            self.show_assign_staff_form(chosen_voyage_ob.departure_time, chosen_voyage_ob)
        else:
            print("Invalid number!")
            voyage_number = self.choose_a_number()

    
    def choose_a_number(self):
        chosen_number = input("\nChoose a number: ")
        return chosen_number
                
        
    def get_year_month_day(self, chosen_voyage_elem): #get_date_for_common_voyage
        departure_year = input("Enter departure year: ")
        departure_month = input("Enter departure month: ")
        departure_day = input("Enter departure day: ")
        departure_hour, departure_minute, departure_second = chosen_voyage_elem[1].split(":")
        departure_date = datetime.datetime(int(departure_year), int(departure_month), int(departure_day), int(departure_hour), int(departure_minute), int(departure_second)).isoformat() #Þetta þyrfti að vera í try except uppá intið

        return departure_date
        #Hérna þarf að gera villutékk á departure_date bæði á formatinu og líka hvort það sé flug á þessari tímasetningu

    def get_year_month_day_voy(self):
        pass