import csv
def load_all_voyages():
        voyages_file = open("csv_files\Voyages.csv","r")

        counter = 1
        for line in voyages_file:
            if counter == 1:
                counter +=1
            else:
                date = line[0]
                time = line[1]
                destination = line[2]
                airplaneID = line[3]
                date, time, destination, airplaneID = line.split(",")
                voyages = VoyagesModel(date, time, destination, airplaneID)
                self.voyages_list.append(voyages)

            return self.voyages_list

load_all_voyages()
