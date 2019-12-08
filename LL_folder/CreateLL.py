class CreateLL():
    '''Subclass of LLAPI that is only designed to create something'''
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def create_pilot(self, new_pilot):
        '''Method that creates a new pilot'''
        new_pilot_list = []
        new_pilot_list.append(new_pilot)
        pass

    def create_cabincrew(self, new_cabincrew):
        '''Method that creates a new cabincrew member'''
        new_cabincrew_list = []
        new_cabincrew_list.append(new_cabincrew)
        pass
    
    def create_voyage(self, new_voyage):
        '''Method that creates a new voyage'''
        new_voyage_list = []
        new_voyage_list.append(new_voyage)
        pass

    def create_destination(self, new_destination):
        '''Method that creates a new destination'''
        new_destination_list = []
        new_destination_list.append(new_destination)
        pass
    
    def create_airplane(self, new_airplane):
        '''Method that creates a new airplane'''
        new_airplane_list = []
        new_airplane_list.append(new_airplane)
        pass
    
    def create_common_voyage(self, common_voyages):
        '''Method that creates common voyages'''
        common_voyages_list = []
        pass