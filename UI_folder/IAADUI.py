from LL_folder.LLAPI import LLAPI
import datetime

class IAADUI():
    LENGTH_STAR = 20
    
    def __init__(self, llapi):
        self.llapi = llapi

    def choose_action(self):
        action_str = input("Choose action: ").lower()
        print()
        return action_str

    def show_IAAD_menu(self, user_input_date, user_input_time=0):
        """This prints the employee menu"""
    
        action_str = ""

        while True:
            print()
            print(self.LENGTH_STAR * "*")
            print("1 Available employees")
            print("2 Unavailable employees")
            print("3 Status of airplanes")
            print("B Back")
            print()
            
            action_str = self.choose_action()

            if action_str == "1":
                self.show_available_employees(user_input_date)

            elif action_str == "2":
                self.show_unavailable_employees(user_input_date)

            elif action_str == "3":
                self.show_enter_time_menu_airplane(user_input_date)

            elif action_str == "b":
                return
                
            else:
                print("Invalid action!")

    def show_enter_date_menu(self):
        """This prints the menu for choosing date to get information about""" 

        print()
        print(self.LENGTH_STAR * "*")
        print("INFORMATION ABOUT A DAY")
        print()
        iaad_year = self.get_iaad_year()
        iaad_month = self.get_iaad_month(iaad_year)
        iaad_day = self.get_iaad_day(iaad_month, iaad_year)
        year, month, day = int(iaad_year), int(iaad_month), int(iaad_day)
        print()
        user_input_date = datetime.datetime(year, month, day, 0, 0, 1).isoformat()

        self.show_IAAD_menu(user_input_date)
        """ This prints out, input date """
        return user_input_date

    def show_enter_time_menu_voyage(self, user_input_date):
        iaad_hour = input("Enter hour (hh): ")
        iaad_minute = input("Enter minute(mm): ")
        print()
        list_user_input_date = list(user_input_date)
        list_user_input_date[11:13] = iaad_hour
        list_user_input_date[14:16] = iaad_minute
        user_input_time = "".join(list_user_input_date)
        self.show_voyages_status(user_input_time)

    def show_enter_time_menu_airplane(self, user_input_date):
        iaad_hour = input("Enter hour (hh): ")
        iaad_minute = input("Enter minute(mm): ")
        print()
        list_user_input_date = list(user_input_date)
        list_user_input_date[11:13] = iaad_hour
        list_user_input_date[14:16] = iaad_minute
        list_user_input_date[17:19] = "00"
        user_input_time = "".join(list_user_input_date)
        self.show_airplane_status(user_input_time)
    
    def show_available_employees(self, user_input_date):
        """This prints the available employees from a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AVAILABLE EMPLOYEES")

        available_employees_list = self.llapi.get_available_emp_by_date(user_input_date)
        for employee_ob in available_employees_list:
            print(f"\nName: {employee_ob.name}, rank: {employee_ob.rank}")
        

        print()
        print("B Back")
       
        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_unavailable_employees(self, user_input_date): #Hérna þurfa að fylgja til hvaða áfangastaði starfsmennirnar eru að fara
        """This prints the unavailable employees on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("UNAVAILABLE EMPLOYEES")

        unavailable_employess = self.llapi.get_unavailable_emp_by_date(user_input_date)
        for employee_elem in unavailable_employess:
            print(f"\nName: {employee_elem[0]}, destination: {employee_elem[1]}")

        print()
        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_airplane_status(self, user_input_date):
        """This prints the status of airplanes on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AIRPLANE STATUS")

        airplane_status = self.llapi.get_airplane_status_by_date(user_input_date)
        counter = 1
        if airplane_status != []:
            for airplane_elem in airplane_status:
                    print(f"\n{counter}.\nDestination: {airplane_elem[0]} \nAirplane name: {airplane_elem[1]} \nAirplane type: {airplane_elem[2]} \nSeat amount: {airplane_elem[3]}Flight number: {airplane_elem[4]} \nNext available time: {airplane_elem[5]}")
                    counter += 1

        else:
            print("\nNo airplne is flying at this time")

        print()
        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def get_iaad_year(self):
        iaad_year = input("Enter year (yyyy): ")
        iaad_year_check = self.llapi.check_iaad_year(iaad_year)

        if iaad_year_check:
            return iaad_year_check
        else:
            print("\nInvalid year\n")
            self.get_iaad_year()

    def get_iaad_month(self, iaad_year):
        iaad_month = input("Enter month (mm): ")
        iaad_month_check = self.llapi.check_iaad_month(iaad_month, iaad_year)

        if iaad_month_check:
            return iaad_month_check
        else:
            print("\nInvalid month\n")
            self.get_iaad_month(iaad_year)

    def get_iaad_day(self, iaad_month, iaad_year):
        iaad_day = input("Enter day (dd): ")
        iaad_day_check = self.llapi.check_iaad_day(iaad_day, iaad_month, iaad_year)

        if iaad_day_check:
            return iaad_day_check
        else:
            print("\nInvalid day\n")
            self.get_iaad_day(iaad_month, iaad_year)