class AirplanesUI():
    def __init__(self):
        pass

    @classmethod
    def show_airplane_menu(cls):
        """ This prints the airplane menu """
        action = input("Choose action: ")
        print()
                
        if action == "1":
            AirplanesUI.show_airplane_overview()

        elif action == "2":
            AirplanesUI.show_create_airplane_form()

        elif action == "B":
            from main_menu_UI import main_menu
            main_menu.main_menu()

    @classmethod
    def show_airplane_overview(cls):
        """ This prints the overview of all airplanes """
        print("OVERVIEW OF AIRPLANES")

        #calls the method that makes a list of all airplanes and prints it
        print("B Back\n")

        action = input("Choose action: ")
        print()

        if action == "B":
            EmployeesUI.show_employee_menu()

    @classmethod
    def show_create_airplane_form(cls):
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
            AirplanesUI.show_airplane_menu()

        elif action == "B":
            AirplanesUI.show_airplane_menu()
