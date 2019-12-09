import datetime
import dateutil.parser

class GetAirplanesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_all_airplanes(self):
        """ Calls the IOAPI to get a list of all airplanes """
        return self.ioapi.get_airplane_list()

    def list_available_airplanes_by_date(self, voyage_date):
        airplane_list = self.list_all_airplanes()
        voyage_list = self.ioapi.get_all_voyages_list()
        unavailable_airplane_list = []
        for voyage_ob in voyage_list:
            input_voyage_date = dateutil.parser.parse(voyage_date)
            parsed_date = dateutil.parser.parse(voyage_ob.departure_time)
            if [input_voyage_date.year, input_voyage_date.month, input_voyage_date.day] == [parsed_date.year, parsed_date.month, parsed_date.day]:
                unavailable_airplane_list.append(voyage_ob.aircraftID)

        for airplane_ob in airplane_list:
            if airplane_ob.planeID in unavailable_airplane_list:
                airplane_list.remove(airplane_ob.planeID)
        return airplane_list

    #searched_pilot_info = []

        #pilot_list = self.get_all_pilots()

        #for pilot in self.pilot_list:
            #if pilot.name == name:
                # TODO handle if found
            #    pass
        # TODO handle if none is found

        #hver flugvél flýgur bara einu sinni á dag, fá year month og day í sitthvoru

    #import datetime
    #year, month, day, hour, minute = 2020, 12, 24, 18, 0

    #new_date = datetime.datetime(year, month, day, hour, minute, 0).isoformat()
    #print(new_date) Þetta prentar 2020-12-24T18:00:00
    #new_date.day -þá fáum við daginn

    #import dateutil.parser

    #date = "2019-11-08T06:35:00"
    #parsed_date = dateutil.parser.parse(date)

    #parsed_date.minute : 35
    #parsed_date.year : 2019

    def make_numbered_airplane_dict(self, airplane_list):
        numbered_airplane_dict = {}
        counter = 1

        for airplane_ob in airplane_list:
                
            numbered_airplane_dict[counter] = airplane_ob

            counter += 1

        return numbered_airplane_dict
    
    def get_airplane_object_from_numbered_dict(self, numbered_airplane_dict, input_number):
        
        for number, airplane_ob in numbered_airplane_dict.items():
            if number == input_number:
                return airplane_ob