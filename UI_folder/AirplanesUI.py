from models.AirplanesModel import AirplanesModel
from LL_folder.LLAPI import LLAPI

class AirplanesUI():
    LENGTH_STAR = 20
    def __init__(self, llapi):
        self.llapi = llapi

    def show_airplane_menu(self):
        """ This prints the airplane menu """

        action = ""
        while(action != "q"):
            print(self.LENGTH_STAR * "*")
            print("AIRPLANE MENU")
            print("1 Print overview of all airplanes")
            print("2 Create a new airplane")
            print("B Back")
            print("Q Quit")
            action_str = input("Choose action: ").lower()
            print()

            if action == "1":
                self.show_airplane_overview()
            elif action == "2":
                self.show_create_airplane_form()
            elif action == "b":
                return

    def show_airplane_overview(self):
        """This prints the overview of all airplanes"""

        print("OVERVIEW OF AIRPLANES")

        airplanes = self.llapi.get_airplanes_overwiew() #Hérna kallar hann í fall í llapanum sem heitir get_destinations_overview sem returnar lista yfir alla áfangastaði
        print(airplanes)

        #calls the method that makes a list of all airplanes and prints it
        print("B Back\n")

        action = input("Choose action: ").lower()
        print()

        if action == "b":
            self.show_airplane_menu()

    def show_create_airplane_form(self):
        """This prints the create an airplane form"""

        print("CREATE A NEW AIRPLANE \n")
        airplane_id = input("Enter airplane ID: ")
        airplane_type = input("Enter airplane type: ")
        manufacturer = input("Enter manufacturer: ")
        seat_amount = input("Enter seat amount: ")
        
        print("\nS Save \nB Back\n")

        action = input("Choose action: ").lower()
        print()

        if action == "s":
            #Takes the info and adds it to the airplane list
            print("Airplane successfully created\n")
            new_airplane = AirplanesModel(airplane_id, airplane_type, manufacturer, seat_amount)
            #self.airplane.create_airplane(new_airplane)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá
            self.show_airplane_menu()

        elif action == "b":
            self.show_airplane_menu()