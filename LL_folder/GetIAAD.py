import datetime
import dateutil.parser

class GetIAAD():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_available_emp_by_date(self, user_input_date):
        employee_list = self.ioapi.get_list_of_all_employees()
        available_employees_list = []
        for employee_ob in employee_list:
            if self.list_unavailable_emp_by_date(user_input_date) != []:
                for i in range(len(self.list_unavailable_emp_by_date(user_input_date))):
                    if employee_ob.name not in self.list_unavailable_emp_by_date(user_input_date)[i]:
                        available_employees_list.append(employee_ob)
                        break
            else:
                available_employees_list.append(employee_ob)

        return available_employees_list

    def list_unavailable_emp_by_date(self, user_input_date):
        voyage_list = self.ioapi.get_all_voyages_list()
        employee_list = self.ioapi.get_list_of_all_employees()
        unavailable_emp_ssn_list = []
        for voyage_ob in voyage_list:
            parsed_date = dateutil.parser.parse(voyage_ob.departure_time)
            user_input_parsed_date = dateutil.parser.parse(user_input_date)
            if [user_input_parsed_date.year, user_input_parsed_date.month, user_input_parsed_date.day] == [parsed_date.year, parsed_date.month, parsed_date.day]:
                if voyage_ob.crew_list != []:
                    unavailable_emp_ssn_list.append([voyage_ob.crew_list[0], voyage_ob.crew_list[1], voyage_ob.crew_list[2], voyage_ob.crew_list[3], voyage_ob.crew_list[4], voyage_ob.destination])
        
        unavailable_emp_name_list = []
        for employee_ob in employee_list:
            for i in range(len(unavailable_emp_ssn_list)):
                if employee_ob.ssn in unavailable_emp_ssn_list[i]:
                    unavailable_emp_name_list.append([employee_ob.name, unavailable_emp_ssn_list[i][5]])

        return unavailable_emp_name_list


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
                                    available_airplane_date = str(parsed_voyage_date.day) + "." + str(parsed_voyage_date.month) + "." + str(parsed_voyage_date.year) + " 00:00:00"
                                    break
                        if available_airplane_date == "":
                            available_airplane_date = str((parsed_input_date.day+1)) + "." + str(parsed_input_date.month) + "." + str(parsed_input_date.year) + " 00:00:00"
                            counter += 1

                    
                    airplane_status_list.append([flights_on_day_list[i].arriving_at,airplane_name, airplane_type, airplane_seat_amount, flight_number, available_airplane_date])

                i += 2
        return airplane_status_list

    def list_voyages_status_by_date(self, user_input_date_from, user_input_date_to):
        """Returns a list of voyages on that day sorted by complete, arrived, in air and not started"""
        voyage_list = self.ioapi.get_all_voyages_list()
        voyage_list_date = []
       
        for voyage_ob in voyage_list:
            if user_input_date_from <= voyage_ob.departure_time <= user_input_date_to:
                voyage_list_date.append(voyage_ob)
        return voyage_list_date