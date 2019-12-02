#adding airplane

airplane_id = input("Enter airplane id: ")
airplane_type = input("Enter airplane type: ")
airplane_manufacturer = input("Enter airplane manufacturer: ")
airplane_seat_amount = input("Enter airplane seat amount: ")

airplane_dict = {}
airplane_dict[airplane_id] = [airplane_type, airplane_manufacturer, airplane_seat_amount]

print(airplane_dict)


#adding pilot
full_name = input("Enter full_name: ")
ssn = input("Enter social security number: ")
address = input("Enter address: ")
home_number = input("Enter home number: ")
mobile_number = input("Enter home number: ")
email = input("Enter email: ")
license_type = input("Enter license type: ")

pilot_dict = {}
pilot_dict[full_name] = [ssn, address, home_number, mobile_number, email, license_type]

print(pilot_dict)
