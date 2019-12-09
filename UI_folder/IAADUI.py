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

    def show_IAAD_menu(self, user_input_date):
        """This prints the employee menu"""
    
        action_str = ""

        while True:
            print()
            print(self.LENGTH_STAR * "*")
            print("1 Available Employees")
            print("2 Unavailable Employees")
            print("3 Status of voyages")
            print("4 Status of Airplanes")
            print("B Back")
            print()
            
            action_str = self.choose_action()

            if action_str == "1":
                self.show_available_employees(user_input_date)

            elif action_str == "2":
                self.show_unavailable_employees(user_input_date)

            elif action_str == "3":
                self.show_voyages_status(user_input_date)

            elif action_str == "4":
                self.show_airplane_status(user_input_date)

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
        iaad_year = input("Enter year: ")
        iaad_month = input("Enter month: ")
        iaad_day = input("Enter day: ")
        print()
        year, month, day = iaad_year, iaad_month, iaad_day
        user_input_date = datetime.datetime(year, month, day, 0, 0, 0).isoformat()

        self.show_IAAD_menu(user_input_date)
        """ This prints out, input date """
        return user_input_date

    
    def show_available_employees(self, user_input_date):
        """This prints the available employees from a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AVAILABLE EMPLOYEES")

        available_employess = self.llapi.get_available_emp_by_date(user_input_date)
        print(available_employess)

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
        print(unavailable_employess)

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
        print(airplane_status)

        print()
        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
   
    def show_voyages_status(self, user_input_date):
        """This prints the status of a voyage on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("VOYAGE STATUS")
        
        voyage_status = self.llapi.get_voyages_status_by_date(user_input_date)
        print(voyage_status)

        print()
        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()