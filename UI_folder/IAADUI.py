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

    def show_enter_date_menu(self):
        """This prints the menu for choosing date to get information about""" 

        print()
        print(self.LENGTH_STAR * "*")
        print("INFORMATION ABOUT A DAY")
        print()
        iaad_date = self.get_iaad_date()
        print()

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
            print("3 Status of airplanes")
            print("B Back")
            print()
            
            action_str = self.choose_action()

            if action_str == "1":
                self.show_available_employees(iaad_date)

            elif action_str == "2":
                self.show_unavailable_employees(iaad_date)

            elif action_str == "3":
                self.show_enter_time_menu_airplane(iaad_date)

            elif action_str == "b":
                return
                
            else:
                print("Invalid action!")

    def show_enter_time_menu_airplane(self, iaad_date):
        time = self.get_iaad_time()
        date_new = iaad_date + "T" + time
        self.show_airplane_status(date_new)
    
    def show_available_employees(self, user_input_date):
        """This prints the available employees from a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AVAILABLE EMPLOYEES")

        available_employees_list = self.llapi.get_available_emp_by_date(user_input_date)
        for employee_ob in available_employees_list:
            print(f"\nName: {employee_ob.name}, rank: {employee_ob.rank}")
        

        print()
        print("\nB Back")
       
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
            print("\nNo airplane is flying at this time")

        print()
        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

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
            self.get_iaad_date()

    def get_iaad_time(self):
        iaad_hour = input("Enter hour (hh): ")
        iaad_minute = input("Enter minute (mm): ")
        time = [iaad_hour, iaad_minute]

        time_check = self.llapi.check_iaad_time(time)

        if time_check:
            return time_check
        else:
            print("\nInvalid time\n")
            self.get_iaad_time()