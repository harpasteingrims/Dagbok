class IOAPI:
    def __init__(self, filename):
        self.filename = filename
        
class GetIO:
    def __init__(self, filename):
        IOAPI.__init__(self, filename)

    def get_employee():                     '''Retrieves employees and sends to Get LL'''
        pass

    def get_airplane():                     '''Retrieves airplanes and sends to Get LL'''
        pass
        
    def get_destinations():                 '''Retrieves destinations and sends to Get LL'''
        pass

    def get_voyage():                       '''Retrieves voyages and sends to Get LL'''
        pass

class CreateIO:
    def __init__(self, filename):          
        IOAPI.__init__(self, filename)

    def add_employee():                     '''Retrieves employees and sends to Create LL'''
        pass

    def add_airplane():                     '''Retrieves airplanes and sends to Create LL'''
        pass
        
    def add_destination():                  '''Retrieves destinations and sends to Create LL'''
        pass

    def add_voyage():                       '''Retrieves voyages and sends to Create LL
        pass
    
class UpdateIO:
    def __init__(self, filename):
        IOAPI.__init__(self, filename)

    def update_employee():                  '''Retrieves employees and sends to Update LL'''
        pass

    def update_destination():               '''Retrieves destinations and sends to Update LL'''
        pass

    def update_voyage():                    '''Retrieves voyages and sends to Update LL'''
        pass
