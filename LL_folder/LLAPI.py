from IOAPI import IOAPI

class LLAPI():
    def __init__(self):
        self.IOAPI = IOAPI()
        
        self.createll = getcreatell #Þetta á að vera klasi
        self.updatell = getupdatell
        self.getvoyages = getvoyages
        self.getairplanes = getairplanes
        self.getdestinations = getdestinations
    

    """Setti þetta inn hér þetta var það sem ég var byrjuð á í UIAPI"""
    
''' EMPLOYEES '''    
    def get_employee_overwiew(self):
        pass
        # employees = self.__employee_service.get_employee_overwiew()

    def get_pilot_overview(self):
        pass

    def get_cabin_crew_overwiew(self):
        pass
    
    def get_info_about_pilot_by_name(self):
        pass

    ''' DESTINATIONS '''
    def get_destination_overview(self):
        # fall fyrir show_destination_overview, í því falli á að prenta út overview af destinations
        #kalla á LL-layer klasann sem er með lista af destinations
        #return
        pass
    def new_destination(self):
        # fall fyrir show_create_des_form, þarf að senda nýja 
        pass

    def get_voyages_overview(self):
        return self.__voyage_repo.get_voyages()

    #__init__(self):
        #self.llayer = LLAPI()
        #self.mainmenu = MainmenuUI()
        #...


    def add_employee(self):
        pass

    def get_employee(self):
        pass #Listar allar employeea