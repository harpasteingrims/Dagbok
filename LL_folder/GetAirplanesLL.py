import datetime
import dateutil.parser

class GetAirplanesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_all_airplanes(self):
        """ Calls the IOAPI to get a list of all airplanes """
        return self.ioapi.get_airplane_list()

    def list_available_airplanes_by_date(self, voyage_date):
        """Gets a date and makes a list of all avaliable airplanes and returns it """

        airplane_list = self.list_all_airplanes()
        voyage_list = self.ioapi.get_all_voyages_list()
        
        
        # First it goes through the voyage list to find and make a list of the airplanes that are not avaliable 
        unavailable_airplane_list = []
        for voyage_ob in voyage_list:
            input_voyage_date = dateutil.parser.parse(voyage_date)
            parsed_date = dateutil.parser.parse(voyage_ob.departure_time)
            if [input_voyage_date.year, input_voyage_date.month, input_voyage_date.day] == [parsed_date.year, parsed_date.month, parsed_date.day]:
                unavailable_airplane_list.append(voyage_ob.aircraftID)

        # Then it goes through the airplane list to check if they are in the unavaliable airplane list
        available_airplane_list = []
        for airplane_ob in airplane_list:
            if airplane_ob.planeID not in unavailable_airplane_list:
                available_airplane_list.append(airplane_ob.planeID)
        
        return available_airplane_list
    
    def get_airplane_type_list(self):
        """Makes a list of all airplanetypes and returns it"""
    
        airplane_ob_list = self.list_all_airplanes()
        plane_list = []

        for airplane_ob in airplane_ob_list:
            if airplane_ob.airplane_type not in plane_list:
                plane_list.append(airplane_ob.airplane_type)

        return plane_list