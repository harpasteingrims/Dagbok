class UIAPI():
    def __init__(self):
        pass

class VoyagesUI(UIAPI):
    def __init__(self):
        pass

    def show_overview_voyage(self):
        """ This prints the overview of a voyage """
        pass

    def show_assign_staff_form(self):
        """ This prints the form for assigning staff to a voyage """
        pass
    
    def show_add_menu(self):
        """ This prints the menu for add a voyage """
        pass 

    def show_see_common(self):
        """ This prints all the common voyages """
        pass 

    def show_create_manually_form(self):
        """ This prints the form to add a voyage manually """
        pass 

    def show_available_airplane(self):
        """ This prints all the available airplanes for a voyage """
        pass

    def show_time_from_iceland(self):
        """ This prints the flight time from Iceland for the flight """
        pass 

    def show_date_from_iceland(self):
        """ This prints what date is for the flight """
        pass 

    def show_destinations(self):
        """ This prints all the destinations """
        pass 


class DestinationUI(UIAPI):
    def __init__(self):
        pass

    def show_destination_menu(self):
        """ This prints the menu for destinations """
        pass 

    def show_destination_overview(self):
        """ This prints all the destination """
        pass 

    def show_add_des_form(self):
        """ This prints the add a destination form """
        pass 

    def show_emerg_country_menu(self):
        """ This prints the emergency contact menu """
        pass 

    def show_emergency_contact(self):
        """ This prints the emergency contact for a specific country """
        pass

    def show_emergency_cont_form(self):
        """ This prints the emergency contact form """
        pass


class AirplaneUI(UIAPI):
    def __init__(self):
        pass

    def show_airplane_menu(self):
        """ This prints the airplane menu """
        pass

    def show_airplane_overview(self):
        """ This prints the overview of all airplanes """
        pass

    def show_add_airplane_form(self):
        """ This prints the add a airplane form """
        pass


class IAADUI(UIAPI):
    def __init__(self):
        pass

    def show_enter_date(self):
        """ This prints, input date """
        pass

    def show_available_employees(self):
        """ This prints the available employees from a certain date """
        pass

    def show_unavailable_employees(self):
        """ This prints the unavailable employees from a certain date """
        pass

    def show_airplane_status(self):
        """ This prints the status of a airplane from a certain date """
        pass

    def show_voyages_status(self):
        """ This prints the status of a voyage from a certain date """
        pass

    def show_IAAD_menu(self):
        """ This prints the information about a date menu """
        pass
