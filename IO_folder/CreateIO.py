from IO_folder.getIO import GetIO
from models.CabinCrewModel import CabinCrewModel
from models.PilotModel import PilotsModel
from models.AirplanesModel import AirplanesModel

class CreateIO():
    def __init__(self):
        pass
    
    def add_pilot(self):
        GetIO.get_all_pilots(self)
        
        #hér er ég að sækja listann af employees sem get er búinn að búa til
        #IOAPI.get_employee(self)

        #vantar að setja kannski id number 
    
    def add_cabincrew(self):
        cabincrew_list = getIO.get_cabincrew()
        cabincrew = models.CabinCrewModel()
        cabincrew_list.append(cabincrew)
        
    def add_airplane(self):
        airplane_list = DataLayer_folder.GetIO()
        airplane = models.AirplanesModel()
        airplane_list.append(airplane)

    def add_destiantions(self):
        pass

    def add_voyage(self):
        pass
