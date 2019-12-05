from IO_folder.getIO import GetIO
import csv
# spurningar fyrir morgundaginn
#á update að hafa tenginu við file eða getIO?
#nota modelclasa?
#hvaðan fær updateIO upplysingarnar um að breyta og hvað?
#notum við dict? man ekki hvernig það virkar
class UpdateIO:
    def __init__(self):
        self.get = GetIO() # ef við viljum að update noti get til að updatea
        

    def update_emergency_contact(self, update_contact):               
        ''' Updates an emergency contact for a certain country'''

        destination_file = open("Destinations.csv", 'r+')
        for line in destination_file:
            if line[0] == update_contact[0]:
                line[4:] = update_contact[4:]
                    
        destination_file.close()
        #hverju á ég að returna?

    def update_voyage(self, update_voyage):                    
        '''Updates a voyage'''
        pass
    def update_pilot(self, update_pilot):
        ''' Updates a pilot '''
        pass
    
    def update_cabincrew(self, update_cabincrew):
        pass


    