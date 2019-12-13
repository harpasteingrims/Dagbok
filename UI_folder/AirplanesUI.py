from models.AirplanesModel import AirplanesModel
from LL_folder.LLAPI import LLAPI

class AirplanesUI():
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

    def get_input_number(self, ob_list):
        """Asks user for a number, sends to InputCheck and then returns it"""

        chosen_number = input("\nB Back\n\nSee pilots with a particular airplane license\nChoose number for airplane type: ").lower()
        
        if chosen_number == "b":
            return
        
        else:
            chosen_object = self.llapi.check_chosen_number(chosen_number, ob_list)
        
            if chosen_object:
                return chosen_object
            else:
                print("\nInvalid input!")
                self.get_input_number(ob_list)
        
    def show_airplane_menu(self):
        """Prints the airplane menu"""

        action_str = ""

        while True:
            print(self.LENGTH_STAR * "*")
            print("AIRPLANE MENU\n")
            print("1 Print overview of all airplanes")
            print("2 Create a new airplane")
            print("B Back\n")
            
            action_str = self.choose_action(["1","2","b"])
            while action_str == False:
                action_str = self.choose_action(["1", "2", "b"])

            if action_str  == "1":
                self.show_airplane_overview()
            elif action_str == "2":
                self.show_create_airplane_form()
            elif action_str == "b":
                return

    def show_airplane_overview(self):
        """Prints the overview of all airplanes"""

        print(self.LENGTH_STAR * "*")
        print("OVERVIEW OF AIRPLANES")

        airplanes_ob_list = self.llapi.get_airplanes_overview() 
        counter = 1
        for airplane_ob in airplanes_ob_list:
            print(airplane_ob.print_out_line(counter))
            counter += 1

        print(f"\nNAN AIR has {len(airplanes_ob_list)} airplanes")

        chosen_ob = self.get_input_number(airplanes_ob_list)
        while chosen_ob == False:
            chosen_ob = self.get_input_number(airplanes_ob_list)
        
        if chosen_ob == "Back":
            return 
        
        elif chosen_ob:
            self.list_pilots_with_licence_of_picked_airplane(chosen_ob)

    def list_pilots_with_licence_of_picked_airplane(self, chosen_airplane_ob):
        """Prints a list of pilots that have a license for selected airplane type"""

        all_pilots_list = self.llapi.get_pilot_overview()
        print(f"\nOVERVIEW OF PILOTS WITH A {chosen_airplane_ob.airplane_type.upper()} LICENSE ")
        valid_pilots = []
        for pilot_ob in all_pilots_list:
            if chosen_airplane_ob.airplane_type == pilot_ob.license_type:
                valid_pilots.append(pilot_ob)
                print(pilot_ob.print_available())
        if valid_pilots == []:
            print(f"\nThere are no pilots that have a {chosen_airplane_ob.airplane_type} license ")

        print("\nB Back\n")

        action_str = self.choose_action(["b"])
        while action_str == False:
                action_str = self.choose_action(["b"])
        
        if action_str == "b":
            return

    def show_create_airplane_form(self):
        """Prints the create an airplane form"""

        print(self.LENGTH_STAR * "*")
        print("CREATE A NEW AIRPLANE")

        print("\nB Back\nC Continue\n")
        action_str = self.choose_action(["b", "c"])
        while action_str == False:
                action_str = self.choose_action(["c", "b"])
        
        if action_str == "b":
            return
        elif action_str == "c":

            airplane_id = self.get_airplane_id()
            while airplane_id == False:
                airplane_id = self.get_airplane_id()
            airplane_type = self.get_airplane_type()
            while airplane_type == False:
                airplane_type = self.get_airplane_type()
            manufacturer = self.get_manufacturer()
            while manufacturer == False:
                manufacturer = self.get_manufacturer()
            seat_amount = self.get_seat_amount()
            while seat_amount == False:
                seat_amount = self.get_seat_amount()

            print("\nS Save \nB Back\n")

            action_str = self.choose_action(["s","b"])
            while action_str == False:
                action_str = self.choose_action(["s", "b"])

            if action_str == "s":
                new_airplane_object = AirplanesModel(airplane_id, airplane_type, manufacturer, seat_amount)
                self.llapi.create_new_airplane(new_airplane_object)
                print(f"Airplane {new_airplane_object.planeID} successfully created\n")
                return

            elif action_str == "b":
                return
    
    """The get methods below ask the user for a certain input, sends it to InputCheck and then returns it"""

    def get_airplane_id(self):
        print("L for letter, n for number")
        airplane_id = input("Enter airplane ID {LL-nnn}: ")
        airplane_id_check = self.llapi.check_airplane_id(airplane_id)

        if airplane_id_check:
            return airplane_id_check
        else:
            print("\nInvalid airplane ID")
            return airplane_id_check

    def get_airplane_type(self):
        airplane_type = input("Enter airplane type: ")
        airplane_type_check = self.llapi.check_airplane_type(airplane_type)

        if airplane_type_check:
            return airplane_type_check
        else:
            print("\nInvalid airplane type")
            return airplane_type_check

    def get_manufacturer(self):
        manufacturer = input("Enter manufacturer: ")
        manufacturer_check = self.llapi.check_manufacturer(manufacturer)

        if manufacturer_check:
            return manufacturer_check

        else:
            print("\nInvalid manufacturer")
            return manufacturer_check

    def get_seat_amount(self):
        seat_amount = input("Enter seat amount: ")
        seat_amount_check = self.llapi.check_seat_amount(seat_amount)

        if seat_amount_check:
            return seat_amount_check

        else:
            print("\nInvalid seat amount")
            return seat_amount_check