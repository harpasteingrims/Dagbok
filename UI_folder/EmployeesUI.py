class EmployeesUI():
    lenght_star = 20
    
    def __init__(self):
        pass

    @classmethod
    def show_employee_menu(cls):
        print(lenght_star*20)
        print("EMPLOYEES MENU \n\n1 Print overview of all employees \n2 Search for an employee \n3 Pilots \n4 Cabin Crew \nB Back \n")
        
        action = input("Choose action: ")
        print()

        if action == "1":
            cls.show_overview_of_all_employees()

        elif action == "2":
            from PilotUI import PilotsUI
            PilotsUI.show_pilot_menu()

        elif action == "3":
            from CabincrewUI import CabincrewUI
            CabincrewUI.show_cabin_crew_menu()

        elif action == "B":
            from MainmenuUI import MainmenuUI
            Main_menu.show_main_menu()

    @classmethod
    def show_overview_of_all_employees(cls):
        print("OVERVIEW OF EMPLOYEES")

        # calls the method that makes a list of all emps and prints it
        print("B Back\n")

        action = input("Choose action: ")
        print()

        if action == "B":
            cls.show_employee_menu()
