class GetIO():
    def __init__(self):
        pass

    def get_employee():
        file_object = open("crew.csv","r")
        
        new_crew_list = []
        for line in file_object:
            line = line.strip().split(",")
            SSN = line[0]
            Name = line[1]
            Role = line[2]
            Rank = line[3]
            licens = line[4]
            employee = {}
            employee[Name] = [SSN,Role,Rank,licens]
            new_crew_list.append(employee)
            employee.clear
        crew_list = []
        for obj in new_crew_list[1:]:
            crew_list.append(obj)
        print(crew_list)

        return crew_list
        

def main():
    crew_list = GetIO.get_employee()
    return crew_list
        
main() 