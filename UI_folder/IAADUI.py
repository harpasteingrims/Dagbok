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

    def show_enter_date_menu(self):
        """This prints the menu for choosing date to get information about""" 

        print()
        print(self.LENGTH_STAR * "*")
        print("INFORMATION ABOUT A DAY\n")
        iaad_date = self.get_iaad_date()
        while iaad_date == False:
            iaad_date = self.get_iaad_date()

        self.show_IAAD_menu(iaad_date)
        """ This prints out, input date """
        return iaad_date

    def show_IAAD_menu(self, iaad_date):
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
                self.show_available_employees(iaad_date)

            elif action_str == "2":
                self.show_unavailable_employees(iaad_date)
            
            elif action_str == "3":
                self.show_enter_time_menu_voyage(iaad_date)

            elif action_str == "4":
                self.show_enter_time_menu_airplane(iaad_date)

            elif action_str == "b":
                return

    def show_enter_time_menu_airplane(self, iaad_date):
        time = self.get_iaad_time()
        while time == False:
            time = self.get_iaad_time()
        date_new = iaad_date + "T" + time
        #date_new = str(datetime.datetime(int(iaad_date[0:4]), int(iaad_date[5:7]), int(iaad_date[8:10]), int(time[0:2]), int(time[3:5]), int(time[6:8])))
        print(date_new)
        self.show_airplane_status(date_new)

    def show_available_employees(self, user_input_date):
        """This prints the available employees from a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AVAILABLE EMPLOYEES")

        available_employees_list = self.llapi.get_available_emp_by_date(user_input_date)
        for employee_ob in available_employees_list:
            print(f"\nName: {employee_ob.name}, rank: {employee_ob.rank}")

        parsed_input_date= dateutil.parser.parse(user_input_date)
        print(f"\nNAN AIR has {len(available_employees_list)} avaliable employees on {parsed_input_date.day}/{parsed_input_date.month}/{parsed_input_date.year}")
        print("\nB Back\n")
       
        action_str = self.choose_action(["b"])
        while action_str == False:
            action_str = self.choose_action(["b"])

        if action_str == "b":
            return

    def show_unavailable_employees(self, user_input_date): #Hérna þurfa að fylgja til hvaða áfangastaði starfsmennirnar eru að fara
        """This prints the unavailable employees on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("UNAVAILABLE EMPLOYEES\n")

        unavailable_employees_list = self.llapi.get_unavailable_emp_by_date(user_input_date)
        for employee_elem in unavailable_employees_list:
            
            if employee_elem != []:
                print(f"\nName: {employee_elem[0]}, destination: {employee_elem[1]}")
                parsed_input_date = dateutil.parser.parse(user_input_date)
                print(f"\nNAN AIR has {len(unavailable_employees_list)} uavaliable employees on {parsed_input_date.day}/{parsed_input_date.month}/{parsed_input_date.year}")
            else:
                print("There are no unavailable employees for that day")

        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        while action_str == False:
            action_str = self.choose_action(["b"])

        if action_str == "b":
            return

    def show_airplane_status(self, user_input_date):
        """This prints the status of airplanes on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AIRPLANE STATUS\n")

        airplane_status = self.llapi.get_airplane_status_by_date(user_input_date)
        counter = 1
        
        if airplane_status != []:
            for airplane_elem in airplane_status:
                    print(f"\n{counter}.\nDestination: {airplane_elem[0]} \nAirplane name: {airplane_elem[1]} \nAirplane type: {airplane_elem[2]} \nSeat amount: {airplane_elem[3]} \nFlight number: {airplane_elem[4]} \nNext available time: {airplane_elem[5]}")
                    counter += 1

        else:
            print("\nNo airplane is flying at this time")

        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        while action_str == False:
            action_str = self.choose_action(["b"])

        if action_str == "b":
            return

    def show_voyages_status(self, user_input_date):
        """This prints the status of a voyage on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("VOYAGE STATUS\n")
        
        voyage_status = self.llapi.get_voyages_status_by_date(user_input_date)
        print(voyage_status)

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