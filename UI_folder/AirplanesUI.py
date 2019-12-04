class AirplanesUI():
    def __init__(self):
        pass

    def show_airplane_menu(self):
        """ This prints the airplane menu """
        action = input("Choose action: ")
        print()
                
        if action == "1":
            self.show_airplane_overview()

        elif action == "2":
            self.show_create_airplane_form()

        elif action == "B":
            from MainmenuUI import MainmenuUI
            main_menu.main_menu()

    def show_airplane_overview(self):
        """ This prints the overview of all airplanes """
        print("OVERVIEW OF AIRPLANES")

        #calls the method that makes a list of all airplanes and prints it
        print("B Back\n")

        action = input("Choose action: ")
        print()

        if action == "B":
            self.show_airplane_menu()

    def show_create_airplane_form(self):
        """ This prints the add a airplane form """
        print("CREATE A NEW AIRPLANE \n")
        airplane_id = input("Enter airplane ID: ")
        airplane_type = input("Enter airplane type: ")
        manufacturer = input("Enter manufacturer: ")
        seat_amount = input("Enter seat amount: ")
        
        print("\nS Save \nB Back\n")

        action = input("Choose action: ")
        print()

        if action == "S":
            """ Takes the info and adds it to the airplane list"""
            #calls the method that adds the info to a list of airplanes
            
            print("Airplane successfully created\n")
            self.show_airplane_menu()

        elif action == "B":
            self.show_airplane_menu()
