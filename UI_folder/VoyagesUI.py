from models.VoyagesModel import VoyagesModel
from LL_folder.LLAPI import LLAPI
import datetime

class VoyagesUI():
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

    
    def show_voyage_menu(self):
        """Prints the voyage menu"""

        action_str = ""

        while True:
            print(self.LENGTH_STAR * "*")
            print("VOYAGE MENU\n")
            print("1 Print overview of voyages")
            print("2 Create a voyage")
            print("3 Assign crew to flights")
            print("B Back\n")

            action_str = self.choose_action(["1","2","3","b"])
            while action_str == False:
                action_str = self.choose_action(["1", "2", "3", "b"])

            if action_str == "1":
                self.show_voyage_overview()
            elif action_str == "2":
                self.show_create_voyage_menu()
            elif action_str == "3":
                print("B Back\nC Continue\n")
                action_str = self.choose_action(["b", "c"])
                while action_str == False:
                        action_str = self.choose_action(["b", "c"])
                if action_str == "b":
                    return
                elif action_str == "c":
                    self.show_not_staffed_voyages()
            elif action_str == "b":
                return

    def show_voyage_overview(self):
        """Prints the overview of all voyages"""
        
        print(self.LENGTH_STAR*"*")
        print("OVERVIEW OF VOYAGES")

        voyages_elem_list = self.llapi.get_voyages_overview() #Kallar á fall i llapanum sem returnar öllum vinnuferðum og prenta út flugnúmer beggja flugferða
        for voyage_elem in voyages_elem_list:
            print(f"\nDeparture time: {voyage_elem[0]}, arrival time: {voyage_elem[1]}, destination: {voyage_elem[2]}, aircraftID: {voyage_elem[3]}, #1 flight number: {voyage_elem[4]}, #2 flight number: {voyage_elem[5]}, flight status: {voyage_elem[6]}")

        print(f"\nNAN AIR has {len(voyages_elem_list)} voyages")
        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        while action_str == False:
                action_str = self.choose_action(["b"])

        if action_str == "b":
            return

    def show_create_voyage_menu(self):
        """Prints the menu for create a voyage"""
        
        print(self.LENGTH_STAR*"*")
        print("CREATE A VOYAGE \n\n1 See/create common voyages\n2 Create a voyage manually\nB Back\n")
        action_str = self.choose_action(["1", "2", "b"])
        while action_str == False:
                action_str = self.choose_action(["1", "2", "b"])

        if action_str == "1":
            self.show_see_common()
        elif action_str == "2":
            self.show_create_manually_form()
        elif action_str == "b":
            return

    def show_see_common(self):
        """Prints all the common voyages"""
        
        print(self.LENGTH_STAR * "*")
        print("SEE/CREATE COMMON VOYAGES")
        
        print("\nB Back\nC Continue\n")
        
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
            action_str = self.choose_action(["b", "c"])
        if action_str == "b":
            return
    
        elif action_str == "c":

            common_voyages_list = self.llapi.get_common_voyages()
            print("Common voyages:\n")
            counter = 1
            for voyage_elem in common_voyages_list:
                print(f"\n{counter} Destination: {voyage_elem[0]}, time: {voyage_elem[1][0:]}")
                counter += 1
            chosen_voyage_elem = self.get_a_number(common_voyages_list)
            while chosen_voyage_elem == -1:
                chosen_voyage_elem = self.get_a_number(common_voyages_list)

            self.show_create_a_common_voyage_form(chosen_voyage_elem)
            return chosen_voyage_elem

    def show_create_a_common_voyage_form(self, chosen_voyage_elem):
        """Creates a voyage from the common voyages but with a new date and a new id"""
        
        print(self.LENGTH_STAR * "*")
        print("INPUT DEPARTURE DATE AND ARIPLANE ID")
        print("\nB Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
                action_str = self.choose_action(["b", "c"])
        
        if action_str == "b":
            return
        elif action_str == "c":

            print("Enter outbound departure date")
        
            departure_hour, departure_minute, departure_second = chosen_voyage_elem[1].split(":")
            date = self.get_year_month_day_voy()
            while date == False:
                date = self.get_year_month_day_voy()
            departure_year, departure_month,  departure_day = date.split("-")
            departure_date = datetime.datetime(int(departure_year), int(departure_month), int(departure_day), int(departure_hour), int(departure_minute), int(departure_second)).isoformat()
            
            print("\nAvaliable airplanes on date:")
            available_airplanes_list = self.llapi.get_available_airplanes_by_date(departure_date)
            chosen_airplane_id = self.print_objects_in_ob_list(available_airplanes_list)

            print("\nS Save\nB Back\n")

            action_str = self.choose_action(["s", "b"])
            while action_str == False:
                action_str = self.choose_action(["s", "b"])

            if action_str == "b":
                return
            elif action_str == "s":
            
                print("\n* Voyage successfully created *\n")
                arrival_time = 0
                new_voyage = VoyagesModel(departure_date, chosen_voyage_elem[0], chosen_airplane_id, arrival_time)
                self.llapi.calculate_outbound_arriv_time(new_voyage)
                self.llapi.calculate_flight_number(new_voyage)
                self.llapi.calculate_return_depart_time(new_voyage)
                self.llapi.calculate_return_arriv_time(new_voyage)
                self.llapi.create_new_voyage(new_voyage)

    def print_objects_in_ob_list(self, ob_list):
        """Prints the object in a certain object list"""

        counter = 1
        for element_ob in ob_list: 
                print(f"\n{counter} {element_ob}")
                counter += 1

        info_list = self.get_a_number(ob_list)
        while info_list == False:
            info_list = self.get_a_number(ob_list)
        
        return info_list

    def show_create_manually_form(self): #Lista upp alla áfangastaði, allar tímasetningar sem eru uppteknar og allar flugvélar sem eru lausar
        """Prints the create a voyage manually form and lets you create a voyage"""
        
        print(self.LENGTH_STAR * "*")
        print("CREATE A VOYAGE MANUALLY")
        
        print("\nB Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
            action_str = self.choose_action(["b", "c"])

        if action_str == "b":
            return
        
        elif action_str == "c":

            print("* Date *\nEnter outbound departure date")
            date = self.get_year_month_day_voy()
            while date == False:
                date = self.get_year_month_day_voy()
            voyage_year, voyage_month,  voyage_day = date.split("-")
            
            unavailable_time = self.llapi.get_unavailable_time_for_voyage(voyage_year, voyage_month, voyage_day) #Þetta prentar alla tímasetningar sem eru ekki í boði
            if unavailable_time != []:
                print("\n* Unavailable time *")
                for time_ob in unavailable_time:
                    time_str = (time_ob.departure_time)[11:]
                    print(f"\n{time_str}")
            
            print("\nEnter outbound departure time")
            voyage_date = self.get_hour_minute_voy(voyage_year, voyage_month, voyage_day)
            while voyage_date == False:
                voyage_date = self.get_hour_minute_voy(voyage_year, voyage_month, voyage_day)
                
            print("\n* Airports *")
            airports = self.llapi.get_airport_overview()
            voyage_airport = self.print_objects_in_ob_list(airports)
            
            print("\n* Airplane *")
            available_airplanes = self.llapi.get_available_airplanes_by_date(voyage_date)
            voyage_airplane = self.print_objects_in_ob_list(available_airplanes)

            print("1 Assign crew to voyage\nS Save\nB Back\n")

            action_str = self.choose_action(["1", "s", "b"])
            while action_str == False:
                action_str = self.choose_action(["1", "s", "b"])

            if action_str == "1" or action_str == "s":
                arrival_time = 0
                new_voyage = VoyagesModel(voyage_date, voyage_airport, voyage_airplane, arrival_time)
                self.llapi.calculate_outbound_arriv_time(new_voyage)
                self.llapi.calculate_flight_number(new_voyage)
                self.llapi.calculate_return_depart_time(new_voyage)
                self.llapi.calculate_return_arriv_time(new_voyage)
                self.llapi.create_new_voyage(new_voyage)

                if action_str == "1":
                    self.show_assign_staff_form(voyage_date, new_voyage)
                    print("\n* Voyage successfully created *\n")
                elif action_str == "s":
                    print("\n* Voyage successfully created *\n")
                    return

            elif action_str == "b":
                return

    def show_assign_staff_form(self, voyage_date, voyage_ob):
        """Prints the form to assign a staff to a voyage"""
        
        print(self.LENGTH_STAR * "*")
        print("ASSIGN CREW TO VOYAGES")

        print("\nB Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
                action_str = self.choose_action(["b", "c"])
        
        if action_str == "b":
            return
        elif action_str == "c":

            available_employees_ob_list = self.llapi.get_available_emp_by_rank(voyage_date, voyage_ob)
            avail_captain_list = available_employees_ob_list[0]
            avail_copilot_list = available_employees_ob_list[1]
            avail_fsm_list = available_employees_ob_list[2]
            avail_fa_list = available_employees_ob_list[3]

            captain_ob = self.process_employee_list("Captain", avail_captain_list, "")
            copilot_ob = self.process_employee_list("Copilot", avail_copilot_list, "")
            senior_cabincrew_member_ob = self.process_employee_list("Flight Service Manager", avail_fsm_list, "")
            cabincrew_member_1_ob = self.process_employee_list("Flight Attendant",avail_fa_list, "")
            cabincrew_member_2_ob = self.process_employee_list("Flight Attendant", avail_fa_list, "")
            if cabincrew_member_1_ob == cabincrew_member_2_ob:
                cabincrew_member_2_ob = self.process_employee_list("Flight Attendant", avail_fa_list, "Can´t pick the same flight attendant, please pick another one :)\n")
            
            print("\nS Save\nB Back\n")

            action_str = self.choose_action(["s", "b"])
            while action_str == False:
                action_str = self.choose_action(["s", "b"])

            if action_str == "b":
                return
            elif action_str == "s":
                crew_list = [captain_ob.ssn, copilot_ob.ssn, senior_cabincrew_member_ob.ssn, cabincrew_member_1_ob.ssn, cabincrew_member_2_ob.ssn]
                updated_voyage_ob = VoyagesModel(voyage_ob.departure_time, voyage_ob.destination, voyage_ob.aircraftID, voyage_ob.arrival_time, crew_list, voyage_ob.outbound_flight_num, voyage_ob.return_flight_num, voyage_ob.return_departure_time, voyage_ob.return_arrival_time)
                self.llapi.update_voyage(updated_voyage_ob)
                
                print("Staff assigned to voyage!")

    def process_employee_list(self, staff_rank, employee_ob_list, message_str):
        """Prints out all the available employees for a certain flight"""

        counter = 1
        print(f"\nAvaliable {staff_rank.lower()}s:")
        for employee_ob in employee_ob_list:
            print(f"\n{counter} {employee_ob.name} {employee_ob.rank}")
            counter += 1

        print(f"\n\n{message_str}* Pick a number for {staff_rank.lower()} *")

        chosen_ob = self.get_a_number(employee_ob_list)
        
        while chosen_ob == False:
            chosen_ob = self.get_a_number(employee_ob_list)

        return chosen_ob

    def show_not_staffed_voyages(self):
        """Prints all the not fully staffed voyages"""
        
        print(self.LENGTH_STAR * "*")
        print("NOT FULLY STAFFED VOYAGES")
        not_staffed_ob_list = self.llapi.get_not_staffed_voyages()
        counter = 1
        for voyage_ob in not_staffed_ob_list:
            print(voyage_ob.print_voy_out(counter))
            counter += 1
        
        voyage_ob = self.get_a_number(not_staffed_ob_list)
        while voyage_ob == False:
            voyage_ob = self.get_a_number(not_staffed_ob_list)
        self.show_assign_staff_form(voyage_ob.departure_time, voyage_ob)

    """The get methods below ask the user for a certain input, sends it to InputCheck and then returns it"""

    def get_a_number(self, ob_list):
        chosen_number = input("\nChoose a number: ")
        ob_item = self.llapi.check_chosen_number(chosen_number, ob_list)
        if ob_item:
            return ob_item
        else:
            print("Invalid number!")
            return ob_item

    def get_year_month_day_voy(self):
        voyage_year = input("Enter year (yyyy): ")
        voyage_month = input("Enter month (mm): ")
        voyage_day = input("Enter day (dd): ")
        date = [voyage_year, voyage_month, voyage_day]
        date_check = self.llapi.check_date(date)
        if date_check:
            return date_check
        else:
            print("\nInvalid date!\n")
            return date_check

    def get_hour_minute_voy(self, voyage_year, voyage_month, voyage_day):
        voyage_hour = input("Enter hour (hh): ")
        voyage_minute = input("Enter minute (mm): ")
        date = [voyage_year, voyage_month, voyage_day, voyage_hour, voyage_minute]
        time_check = self.llapi.check_time(date, voyage_year, voyage_month, voyage_day)
        if time_check:
            return time_check
        else:
            print("\nInvalid time!\n")
            return time_check