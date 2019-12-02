class IOAPI:
    def __init__(self, filename):
        self.filename = filename
        
class GetIO:
    def __init__(self, filename):
        IOAPI.__init__(self, filename)

    def get_employee():
        pass

    def get_airplane():
        pass
        
    def get_destinations():
        pass

    def get_voyage():
        pass

class CreateIO:
    def __init__(self, filename):
        IOAPI.__init__(self, filename)

    def add_employee():
        pass

    def add_airplane():
        pass
        
    def add_destination():
        pass

    def add_voyage():
        pass
    
class UpdateIO:
    def __init__(self, filename):
        IOAPI.__init__(self, filename)

    def update_employee():
        pass

    def update_destination():
        pass

    def update_voyage():
        pass
