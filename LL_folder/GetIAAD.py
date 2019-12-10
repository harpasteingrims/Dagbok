import datetime
import dateutil.parser

class GetIAAD():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_available_emp_by_date(self, user_input_date):
        employee_list = self.ioapi.get_list_of_all_employees()
        available_employees_list = []
        i = 0
        for employee_ob in employee_list:
            if self.list_unavailable_emp_by_date(user_input_date) != []:
                if employee_ob.ssn not in self.list_unavailable_emp_by_date(user_input_date)[i]:
                    available_employees_list.append(employee_ob)
                    i += 1

            else:
                available_employees_list.append([employee_ob.name, employee_ob.role])

        return available_employees_list

    def list_unavailable_emp_by_date(self, user_input_date):
        voyage_list = self.ioapi.get_all_voyages_list()
        unavailable_employees_list = []
        for voyage_ob in voyage_list:
            parsed_date = dateutil.parser.parse(voyage_ob.departure_time)
            user_input_parsed_date = dateutil.parser.parse(user_input_date)
            if [user_input_parsed_date.year, user_input_parsed_date.month, user_input_parsed_date.day] == [parsed_date.year, parsed_date.month, parsed_date.day]:
                if voyage_ob.crew_list != []:
                    unavailable_employees_list.append(voyage_ob.crew_list)

        return unavailable_employees_list


    def list_airplane_status_by_date(self, user_input_date):
        """Returns a list of airplanes sorted by available and unavailable"""
        voyage_list = self.ioapi.get_all_voyages_list()
        airplane_list = self.ioapi.get_airplane_list()
        flights_list = self.ioapi.get_all_flights_list()
        parsed_input_date = dateutil.parser.parse(user_input_date)
        flights_on_day_list = []
        for flight_ob in flights_list:
            parsed_date = dateutil.parser.parse(flight_ob.departure_time)
            if [parsed_input_date.year, parsed_input_date.month, parsed_input_date.day] == [parsed_date.year, parsed_date.month, parsed_date.day]:
                flights_on_day_list.append(flight_ob)

        airplane_status_list = []

        i = 0
        if flights_on_day_list != []:
            for j in range(len(flights_on_day_list)//2):
                if flights_on_day_list[i].departure_time <= user_input_date <= flights_on_day_list[i+1].arrival_time:
                    for airplane_ob in airplane_list:
                        if flights_on_day_list[i].aircraftID == airplane_ob.planeID:
                            airplane_name = airplane_ob.planeID
                            airplane_type = airplane_ob.airplane_type
                            airplane_seat_amount = airplane_ob.seat_amount
                    if flights_on_day_list[i].departure_time <= user_input_date <= flights_on_day_list[i].arrival_time:
                        flight_number = flights_on_day_list[i].flight_number
                    elif flights_on_day_list[i+1].departure_time <= user_input_date <= flights_on_day_list[i+1].arrival_time:
                        flight_number = flights_on_day_list[i+1].flight_number
                    else:
                        flight_number = "Airplane has landed at destination and will soon get back to Iceland with flight number: {}".format(flights_on_day_list[i+1].flight_number)

                    counter = 1
                    available_airplane_date = ""
                    while available_airplane_date == "":
                        for voyage_ob in voyage_list:
                            parsed_voyage_date = dateutil.parser.parse(voyage_ob.departure_time)
                            if [parsed_input_date.year, parsed_input_date.month, (parsed_input_date.day+counter)] == [parsed_voyage_date.year, parsed_voyage_date.month, parsed_voyage_date.day]:
                                if flights_on_day_list[i].aircraftID != voyage_ob.aircraftID:
                                    availale_airplane_date = str(parsed_voyage_date.day) + "." + str(parsed_voyage_date.month) + "." + str(parsed_voyage_date.year) + " 00:00:00"
                                counter += 1

                    
                    airplane_status_list.append([flights_on_day_list[i].arriving_at,airplane_name, airplane_type, airplane_seat_amount, flight_number, availale_airplane_date])

                i += 2
        return airplane_status_list


            
        #Dags. og tíma þegar flugvél er aftur laus ef hún er í notkun
        #Nafn áfangastaðar ef hún er í notkun
        #Flugnúmer flugferðar ef hún er í loftinu.
        #Nafn, týpu og sætafjölda.

        
        pass

        #Sennilega best að kalla bara á neðsta listann hérna fyrir og samræma employees við þann voyage lista
         #Líka pæling hérna hvar er best að geyma þessar upplýsingar og hvernig er best að ná í þær og vinna úr þeim

    def list_voyages_status_by_date(self, user_input_date):
        """Returns a list of voyages on that day sorted by complete, arrived, in air and not started"""
        voyage_list = self.list_of_all_voyages_for_selected_day(user_input_date)
        
        for voyage in voyage_list:
           voyages_for_selected_day = []
        #    if 
        #Þurfum að finna aðferð til þess að sortera þennan lista af voyages þessa dags eftir complete, arrived, in air og not started
        pass

    def list_of_all_voyages_for_selected_day(self, user_input_date):
        """Returns an unsorted list of voyages on that day that the other functions in this class wil be using. The outcome of this function will never appear in the interface"""
        #voyage_list = self.ioapi.get_all_voyages_list()
        #return voyage_list
        pass