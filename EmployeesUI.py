class EmployeesUI():
    
    def __init__(self):
        pass

    @classmethod
    def show_employee_menu(cls):
        print("EMPLOYEES MENU \n\n1 Print overview of all employees \n2 Search for an employee \n3 Pilots \n4 Cabin Crew \nB Back \n")
        
        action = input("Choose action: ")
        print()

        if action == "1":
            EmployeesUI.show_oveview_of_all_employees()

        elif action == "2":
            EmployeesUI.show_search_for_employee()

        elif action == "3":
            from PilotUI import PilotsUI
            PilotsUI.show_pilot_menu()

        elif action == "4":
            from CabincrewUI import CabincrewUI
            CabincrewUI.show_cabin_crew_menu()

        elif action == "B":
            from main_menu_UI import main_menu
            main_menu.main_menu()

    @classmethod
    def show_oveview_of_all_employees(cls):
        print("OVERVIEW OF EMPLOYEES")

        # calls the method that makes a list of all emps and prints it
        print("B Back\n")

        action = input("Choose action: ")
        print()

        if action == "B":
            EmployeesUI.show_employee_menu()


    @classmethod
    def show_search_for_employee(cls):
    
        """ This prints out the pilot menu """
        print("Search for an employee to get information")
        
        name = input("Enter name of employee: ")
        
        # info_of_employee = # Calls the class that holds the information of employee and prints it
        """ Name 
            Social security number
            Adress:
            Home number:
            Mobile number:
            Email: 
        """

        print("1 {}'s flight schedule").format(name)
        print("2 Edit information about flight attendant \nB Back")

        action = input("Choose action: ")
        print()

        if action == "1":
            EmployeesUI.show_flight_schedule_of_employee(name)

        elif action == "2": 
            Employees_UI.show_employee_edit_form(name)

        elif action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_employee_menu()

    #Þarf að skoða þetta

    @classmethod
    def show_flight_schedule_of_employee(cls, name):
        """ Calls a class that makes a list of his voyages """
        date_from = input("Enter date from: ")
        date_to = input("Enter date to: ")

        # calls the class that makes a list of the lfight schedule and prints it

        print("B Back")

        action = input("Choose action: ")
        print()

        if action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_employee_menu()

    @classmethod
    def show_employee_edit_form(cls, name):
        """ This prints out the edit form for an employee """

        # name, ssn, .... = #calls the class to get the info of the pilot 
        
        print("You are changing the information for employee: {}, {}".format(name, ssn))
       
        new_address = input("Enter new address")
        new_home_number = input("Enter new home number: ")
        new_mobile_number = input("Enter new mobile number: ")
        new_email = input("Enter new email: ")
        new_licence_type = input("Enter new license type: ")
        
        print("S Save \nB Back\n")

        action = input("Choose action: ")
        print()

        if action == "S":
            """ Takes the new info, changes and adds it to the pilot list"""
            
            # calls the class that stores the info about the pilot to change it...
            print("Pilot's information successfully changed")
            
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_pilot_menu()

        elif action == "B":
            from EmployeeUI import EmployeesUI
            EmployeesUI.show_pilot_menu()

    
