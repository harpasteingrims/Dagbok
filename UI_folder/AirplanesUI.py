from models.AirplanesModel import AirplanesModel
from LL_folder.LLAPI import LLAPI

class AirplanesUI():
    LENGTH_STAR = 20
    def __init__(self, llapi):
        self.llapi = llapi

    def choose_action(self):
        action_str = input("Choose action: ").lower()
        print()
        return action_str
        
    def show_airplane_menu(self):
        """This prints the airplane menu"""

        action_str = ""

        while True:
            print()
            print(self.LENGTH_STAR * "*")
            print("AIRPLANE MENU")
            print()
            print("1 Print overview of all airplanes")
            print("2 Create a new airplane")
            print("B Back")
            print()
            
            action_str = self.choose_action()

            if action_str  == "1":
                self.show_airplane_overview()
            elif action_str == "2":
                self.show_create_airplane_form()
            elif action_str == "b":
                return
            else:
                print("Invalid action!")

    def show_airplane_overview(self):
        """This prints the overview of all airplanes"""

        print(self.LENGTH_STAR * "*")
        print("OVERVIEW OF AIRPLANES")

        airplanes_ob_list = self.llapi.get_airplanes_overview() #Hérna kallar hann í fall í llapanum sem heitir get_destinations_overview sem returnar lista yfir alla áfangastaði
        for airplane_ob in airplanes_ob_list:
            print(f"\n{airplane_ob.planeID},{airplane_ob.airplane_type},{airplane_ob.manufacturer},{airplane_ob.seat_amount}")

        print("B Back\n")

        action_str = self.choose_action()

        if action_str == "b":
            return
            
        else:
            print("Invalid action!")
            action_str = self.choose_action()   

    def show_create_airplane_form(self):
        """This prints the create an airplane form"""

        print(self.LENGTH_STAR * "*")
        print("CREATE A NEW AIRPLANE \n")

        airplane_id = self.AirplanesUI.get_airplane_id
        airplane_type = self.AirplanesUI.get_airplane_type
        manufacturer = self.AirplanesUI.get_manufacturer
        seat_amount = self.AirplanesUI.get_seat_amount
        
        print("\nS Save \nB Back\n")

        action_str = self.choose_action()

        if action_str == "s":
            #Takes the info and adds it to the airplane list
            new_airplane_object = AirplanesModel(airplane_id, airplane_type, manufacturer, seat_amount)
            self.llapi.create_new_airplane(new_airplane_object)
            print(f"Airplane {new_airplane_object.airplane_id} successfully created\n")
            return

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def get_airplane_id(self):
        airplane_id = input("Enter airplane ID: ")
        airplane_id_check = self.llapi.check_airplane_id(airplane_id)

        if airplane_id_check:
            return airplane_id_check

        else:
            print("\nInvalid airplane ID")
            self.get_airplane_id()

    def get_airplane_type(self):
        airplane_type = input("Enter airplane type")
        return airplane_type

    def get_manufacturer(self):
        manufacturer = input("Enter manufacturer: ")
        manufacturer_check = self.llapi.check_manufacturer(manufacturer)

        if manufacturer_check:
            return manufacturer_check

        else:
            print("\nInvalid manufacturer")
            self.get_manufacturer()

    def get_seat_amount(self):
        seat_amount = input("Enter seat amount: ")
        seat_amount_check = self.llapi.check_seat_amount(seat_amount)

        if seat_amount_check:
            return seat_amount_check

        else:
            print("\nInvalid seat amount")
            self.get_seat_amount()