#adding_airplane

airplane_id = input("Enter airplane id: ")
airplane_type = input("Enter airplane type: ")
airplane_manufacturer = input("Enter airplane manufacturer: ")
airplane_seat_amount = input("Enter airplane seat amount: ")
airplane = [airplane_type, airplane_manufacturer, airplane_seat_amount]

airplane_dict = {}
airplane_dict[airplane_id] = airplane

print(airplane_dict)



