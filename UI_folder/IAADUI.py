from LL_folder.LLAPI import LLAPI
import datetime
import dateutil.parser

class IAADUI():
    LENGTH_STAR = 20
    
    def __init__(self, llapi):
        self.llapi = llapi

    def choose_action(self, valid_list):
        action_str = input("Choose action: ").lower()
        print()
        
        if action_str in valid_list:
            return action_str
            
        else:
            print("Invalid action!")
            return False

    def show_IAAD_menu(self):
        """This prints the employee menu"""
    
        action_str = ""

        while True:
            print()
            print(self.LENGTH_STAR * "*")
            print("1 Available employees")
            print("2 Unavailable employees")
            print("3 Status of voyages")
            print("4 Status of airplanes")
            print("B Back\n")
            
            action_str = self.choose_action(["1","2","3","4","b"])
            while action_str == False:
                action_str = self.choose_action(["1","2","3","4","b"])

            if action_str == "1":
                self.show_available_employees()

            elif action_str == "2":
                self.show_unavailable_employees()
            
            elif action_str == "3":
                self.show_voyages_status()

            elif action_str == "4":
                self.show_airplane_status()

            elif action_str == "b":
                return

    def show_enter_date_menu(self):
        """This prints the menu for choosing date to get information about""" 

        print()
        iaad_date = self.get_iaad_date()
        while iaad_date == False:
            iaad_date = self.get_iaad_date()
        """ This prints out, input date """
        return iaad_date

    def show_enter_date_menu_from(self):
        """This prints the menu for choosing date to get information about""" 

        print()
        iaad_date = self.get_iaad_date()
        while iaad_date == False:
            print("Enter date from\n")
            iaad_date = self.get_iaad_date()
        """ This prints out, input date """
        return iaad_date

    def show_enter_date_menu_to(self):
        """This prints the menu for choosing date to get information about""" 

        print()
        iaad_date = self.get_iaad_date()
        while iaad_date == False:
            print("Enter date to\n")
            iaad_date = self.get_iaad_date()
        """ This prints out, input date """
        return iaad_date

    def show_enter_time_menu_airplane(self, iaad_date):
        time = self.get_iaad_time()
        while time == False:
            time = self.get_iaad_time()
        date_new = iaad_date + "T" + time
        return date_new

    def show_available_employees(self):
        """This prints the available employees for a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AVAILABLE EMPLOYEES")

        iaad_date = self.show_enter_date_menu()
        print(iaad_date)

        available_employees_list = self.llapi.get_available_emp_by_date(iaad_date)
        for employee_ob in available_employees_list:
            print(f"\nName: {employee_ob.name}, rank: {employee_ob.rank}")

        parsed_iaad_date= dateutil.parser.parse(iaad_date)
        print(f"\nNAN AIR has {len(available_employees_list)} avaliable employees on {parsed_iaad_date.day}/{parsed_iaad_date.month}/{parsed_iaad_date.year}")
        print("\nB Back\n")
       
        action_str = self.choose_action(["b"])
        while action_str == False:
            action_str = self.choose_action(["b"])

        if action_str == "b":
            return

    def show_unavailable_employees(self): #Hérna þurfa að fylgja til hvaða áfangastaði starfsmennirnar eru að fara
        """This prints the unavailable employees on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("UNAVAILABLE EMPLOYEES\n")

        iaad_date = self.show_enter_date_menu()

        unavailable_employees_list = self.llapi.get_unavailable_emp_by_date(iaad_date)
        parsed_iaad_date = dateutil.parser.parse(iaad_date)
        print(f"\nNAN AIR has {len(unavailable_employees_list)} unavaliable employees on {parsed_iaad_date.day}/{parsed_iaad_date.month}/{parsed_iaad_date.year}")
        if unavailable_employees_list != []:
            for employee_elem in unavailable_employees_list:
                print(f"\nName: {employee_elem[0]}, Destination: {employee_elem[1]}")
        else:
            print("There are no unavailable employees for that day")

        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        while action_str == False:
            action_str = self.choose_action(["b"])

        if action_str == "b":
            return

    def show_airplane_status(self):
        """This prints the status of airplanes on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AIRPLANE STATUS\n")

        iaad_date = self.show_enter_date_menu()
        iaad_date_time = self.show_enter_time_menu_airplane(iaad_date)

        airplane_status = self.llapi.get_airplane_status_by_date(iaad_date_time)

        counter = 1
        if airplane_status != []:
            for airplane_elem in airplane_status:
                    print(f"\n{counter}.\nAirplane ID: {airplane_elem[1]} \nAirplane type: {airplane_elem[2]}\nDestination: {airplane_elem[0]} \nSeat amount: {airplane_elem[3]} \nFlight number: {airplane_elem[4]} \nNext available time: {airplane_elem[5]}")
                    counter += 1

        else:
            print("\nNo airplane is flying at this time")

        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        while action_str == False:
            action_str = self.choose_action(["b"])

        if action_str == "b":
            return

    def show_voyages_status(self):
        """This prints the status of a voyage on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("VOYAGE STATUS\n")

        print("Enter date from")
        iaad_date_from = self.show_enter_date_menu_from()
        print("\nEnter date to")
        iaad_date_to = self.show_enter_date_menu_to()
        print()
        
        voyage_status_ob_list = self.llapi.get_voyages_status_by_date(iaad_date_to, iaad_date_from)
        if voyage_status_ob_list != []:
            for voyage_ob in voyage_status_ob_list:
                if voyage_ob.crew_list == []:
                    crew = "Not fully staffed"
                else:
                    crew = "Fully staffed"
                print(f"Outbound flight number: {voyage_ob.outbound_flight_num}, return flight number: {voyage_ob.return_flight_num}, destination: {voyage_ob.destination}, departure time from Iceland: {voyage_ob.departure_time}, arrival time in Iceland{voyage_ob.return_arrival_time}, {crew}")


        print()
        print("B Back")

        action_str = self.choose_action(["b"])
        while action_str == False:
            action_str = self.choose_action(["b"])

    def get_iaad_date(self):
        iaad_year = input("Enter year (yyyy): ")
        iaad_month = input("Enter month (mm): ")
        iaad_day = input("Enter day (dd): ")
        date = [iaad_year, iaad_month, iaad_day]

        date_check = self.llapi.check_date(date)

        if date_check:
            return date_check
        else:
            print("\nInvalid date\n")
            return date_check

    def get_iaad_time(self):
        iaad_hour = input("Enter hour (hh): ")
        iaad_minute = input("Enter minute (mm): ")
        time = [iaad_hour, iaad_minute]

        time_check = self.llapi.check_iaad_time(time)

        if time_check:
            return time_check
        else:
            print("\nInvalid time\n")
            return time_check