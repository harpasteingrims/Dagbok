import datetime

class InputCheckLL():
    """Subclass of LLAPI that is designed to create something and error checking the input"""
    
    def __init__(self, ioapi, llapi):
        self.ioapi = ioapi
        self.llapi = llapi

    """CHECKING INPUT FOR EMPLOYEES"""

    def check_name(self, name):
        """Receives a string and returns it if it's valid with every word capitalized"""

        if len(name.split()) > 1 and name.replace(" ", "").isalpha() and len(name) < 40:
            return name.title()
        else: 
            return False

    def check_pilot_rank(self, rank):
        """Receives a string and returns the appropriate term for the selected role if the input is valid"""

        if rank == "1":
            rank = "Captain"
            return rank
        elif rank == "2":
            rank = "Copilot"
            return rank
        else:
            return False
        
    def check_crew_member_rank(self, rank):
        """Receives a string and returns the appropriate term for the selected role if the input is valid"""

        if rank == "1":
            rank = "Flight Service Manager"
            return rank
        elif rank == "2":
            rank = "Flight Attendant"
            return rank
        else:
            return False

    def check_ssn(self, ssn):
        """Receives a string and returns the ssn if it's valid"""

        employee_list = self.ioapi.get_list_of_all_employees()
        for employee_ob in employee_list:
            if ssn != employee_ob.ssn:
                if int(ssn[4:6]) > 20:
                    if len(ssn) == 10 and ssn.isdigit() and self.check_date(["19" + ssn[4:6], ssn[2:4], ssn[0:2]]) != False:
                        return ssn
                    else:
                        return False
                elif ssn[4] == "0" and 0 < int(ssn[5]) < 4:
                    if len(ssn) == 10 and ssn.isdigit() and self.check_date(["20" + ssn[4:6], ssn[2:4], ssn[0:2]]) != False:
                        return ssn
                    else:
                        return False
            else:
                return False
        else:
            return False
    
    def check_address(self, address):
        """Receives a string and returns the address if it's valid with the address name capitalized and spaces in between"""

        if len(address) == 3 and len(address[2]) == 3 and address[0].isalpha() and address[1].isdigit() and address[2].isdigit():
                return address[0].capitalize() + " " + str(address[1]) + " " + str(address[2])
        else: 
            return False

    def check_mobile_number(self, mobile_number):
        """Receives a string and returns the mobile number if it's valid"""

        if len(mobile_number) == 7 and mobile_number.isdigit():
            return mobile_number
        else:
            return False

    def check_email(self, email):
        """Receives a string and returns the email if it's valid with every letter in lowercase"""

        if "@" in email and "." in email:
            return email.lower()
        else:
            return False
    
    def check_license_type(self, license_type_num, plane_list):
        """Receives a string and returns the license if there is a plane for it"""

        try:
            license_type_int = int(license_type_num)
            
            if license_type_int and 1 <= license_type_int <= len(plane_list):
                chosen_license_ob = plane_list[license_type_int-1]
                return chosen_license_ob

        except ValueError:
            return False

    """CHECKING INPUT FOR VOYAGES"""
    
    def check_time(self, date, unavailable_time_list):
        """Receives the day and time in a list and a list of unavailable times and returns it if it's in a valid form and not in the list of unavailable times"""   
        
        date_time = ":".join(date[3:])
        new_list = []
        for unavailable_time_ob in unavailable_time_list:
            new_list.append(unavailable_time_ob.departure_time[11:])
        if date_time not in new_list:
            try:
                valid_time = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), 0).isoformat()
                return valid_time
            except ValueError:
                return False
        else:
            return False

    """CHECKING INPUT FOR DESTINATIONS"""

    def check_country(self, country):
        """Receives a string and returns the country if it's valid with every word capitalized"""

        if " " in country:
            country_list = country.split()
            for element in country_list:
                element.isalpha()
            
            return country.title()

        elif country.isalpha():
            return country.title()

        else:
            return False

    def check_airport(self, airport):
        """Receives a string and returns the airport if it's valid with every word capitalized"""

        if " " in airport:
            airport_list = airport.split()
            for element in airport_list:
                element.isalpha()
            
            return airport.title()
        
        elif airport.isalpha():
            return airport.title()
            
        else:
            return False

    def check_flight_duration(self, flight_duration):
        """Receives a string and returns the flight duration if it's valid"""

        if len(flight_duration) == 5 and flight_duration[0:1].isdigit() and flight_duration[3:5].isdigit() and flight_duration[2] == ":" and int(flight_duration[3:5]) < 60:
            return flight_duration
        else:
            return False

    def check_distance(self, distance):
        """Receives a string and returns the distance if it's valid with a space in between the number and "km" """

        if distance[-3:] == " km" and distance[:-3].isdigit() and int(distance[:-3]) > 50:
            return distance 
        elif distance[-2:] == "km" and distance[:-2].isdigit() and int(distance[:-2]) > 50:
            return distance[:-2] + " " + distance[-2:]
        else:
            return False

    """ CHECKING INPUT FOR AIRPLANES"""

    def check_airplane_id(self, airplane_id):
        """Receives a string and returns the airplane ID if it's valid with every letter capitalized"""
        
        if len(airplane_id) == 6 and airplane_id[2] == "-" and airplane_id[0:2].isalpha() and airplane_id[3:6].isdigit():
            return airplane_id.upper()
        else: 
            return False

    def check_airplane_type(self, airplane_type):
        """Receives a string and returns the airplane type capitalized if it's valid"""

        if any(char.isdigit() for char in airplane_type) and any(char.isalpha() for char in airplane_type):
            return airplane_type.capitalize()
        else:
            return False

    def check_manufacturer(self, manufacturer):
        """Receives a string and returns the manufacturer capitalized if it's valid"""

        if manufacturer.isalpha():
            return manufacturer.capitalize()
        else:
            return False

    def check_seat_amount(self, seat_amount):
        """Receives a string and returns the seat amount if it's valid"""

        if seat_amount.isdigit() and 2 <= int(seat_amount) <= 800:
            return seat_amount
        else:
            return False


    """CHECKING INPUT FOR IAAD"""

    def check_iaad_time(self, time):
        """Receives the time in a list and returns it in a string format if it's valid"""

        try:
            valid_time = datetime.datetime(2019, 1, 1, int(time[0]), int(time[1]), 0).isoformat()
            return valid_time[-8:]
        except ValueError:
            return False

    def check_iaad_voyage_date(self, date):
        """Receives the date in a list and returns it in a datetime format if it's valid"""
        
        if len(date[0]) == 4:
            try:
                valid_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 00, 00, 0).isoformat()
                return valid_date
            except ValueError:
                return False
        else:
            return False

    """CHECKING INPUT FOR OTHER"""

    def check_date_interval(self, date_from, date_to):
        """Receives two dates in a datetime format and checks if the latter date is later than the former date"""

        if date_from <= date_to:
            return True
        else:
            return False

    def check_date(self, date):
        """Receives a date and time in a list and returns it in "2019-11-18" format if it's valid"""

        if len(date[0]) == 4:       #Fyrsta stakið er árið, það verður að koma á formi fjögurra stafa því annars bætir datetime 0 við og úr verður algjört bull
            try:
                valid_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 00, 00, 0).isoformat()
                return valid_date[0:10]
            except ValueError:
                return False
        else:
            return False

    def check_dates(self, date):
        """Receives the day and time in a list and returns it in a datetime form if it's valid"""

        if len(date[0]) == 4:   #Fyrsta stakið er árið, það verður að koma á formi fjögurra stafa því annars bætir datetime 0 við og úr verður algjört bull
            try:
                valid_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), int(date[5])).isoformat()
                return valid_date
            except ValueError:
                return False
        else:
            return False

    def check_input_number(self, chosen_number, ob_list):
        """Receives an input from the user and checks if was one of the available actions"""

        try:
            chosen_number = int(chosen_number)
            if chosen_number and 1 <= chosen_number <= len(ob_list):
                chosen_ob = ob_list[chosen_number-1]
                return chosen_ob
            else:
                return False
        except ValueError:
            return False