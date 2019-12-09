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

        airplane_id = input("Enter airplane ID: ")
        airplane_type = input("Enter airplane type: ")
        manufacturer = input("Enter manufacturer: ")
        seat_amount = input("Enter seat amount: ")
        
        print("\nS Save \nB Back\n")

        action_str = self.choose_action()

        if action_str == "s":
            #Takes the info and adds it to the airplane list
            print("Airplane successfully created\n")
            new_airplane = AirplanesModel(airplane_id, airplane_type, manufacturer, seat_amount)
            #self.llapi.create_new_airplane(new_airplane)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá
            
            self.show_airplane_menu()

        elif action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()