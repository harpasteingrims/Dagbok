import datetime
import dateutil.parser
class GetIAAD():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_available_emp_by_date(self, user_input_date):
        employee_list = self.ioapi.get_list_of_all_employees()
        #voyage_list = self.list_voyages_status_by_date(self, user_input_date)
        available_employees_list = []
        voyage_list = self.ioapi.get_all_voyages_list()
        i = 0
        for employee_ob in employee_list:
            if employee_ob.name not in self.list_unavailable_emp_by_date(self, user_input_date)[i]:
                available_employees_list.append(employee_ob.name)
                i += 1

        #for employee in employee_list:
            #available_emps_for_selected_day = []
            #if employee not in (hvernig á ég að athuga allt staff á öllum ferðunum í listanum af objectum?)
                #available_emps_for_selected_day.append(employee)
        #return available_emps_for_selected_day
        pass

    def list_unavailable_emp_by_date(self, user_input_date):
        #employee_list = self.ioapi.get_list_of_all_employees()
        #voyage_list = list_voyages_status_by_date(self, user_input_date)
        voyage_list = self.ioapi.get_all_voyages_list()

        for voyage_ob in voyage_list:
            unavailable_employees_list = []
            date = voyage_ob.date
            parsed_date = dateutil.parser.parse(date)
            if user_input_date.year == parsed_date.year and user_input_date.month == parsed_date.month and user_input_date.day == parsed_date.day: #Hérna þyrftum við líka að tékka hvort almennt það eru starfsmenn á vélinni
                unavailable_employees_list.append([voyage_ob.captain, voyage_ob.copilot, voyage_ob.fsm, voyage_ob.fa1, voyage_ob.fa2, voyage_ob.arriving_at])

            return unavailable_employees_list

        #for employee in employee_list:
        #    available_emps_for_selected_day = []
            #if employee in (hvernig á ég að athuga allt staff á öllum ferðunum í listanum af objectum?)
         #       available_emps_for_selected_day.append(employee)
        #return available_emps_for_selected_day

    def list_airplane_status_by_date(self, user_input_date):
        #airplane_list = self.ioapi.get_airplane_list
        #voyage_list = list_voyages_status_by_date(self, user_input_date)
        #for airplane in airplane_list:
        #    available_planes_for_selected_day = []
            #if employee in (hvernig á ég að athuga allt staff á öllum ferðunum í listanum af objectum?)
                #available_planes_for_selected_day.append(airplane)
        #return available_planes_for_selected_day
        pass

        #Sennilega best að kalla bara á neðsta listann hérna fyrir og samræma employees við þann voyage lista
         #Líka pæling hérna hvar er best að geyma þessar upplýsingar og hvernig er best að ná í þær og vinna úr þeim

    def list_voyages_status_by_date(self, user_input_date):
        #"""Returns a list of voyages on that day sorted by complete, arrived, in air and not started"""
        #voyage_list = self.ioapi.get_all_voyages_list
        #for voyage in voyage_list:
        #    voyages_for selected_day = []
        #    if 
        #Þurfum að finna aðferð til þess að sortera þennan lista af voyages þessa dags eftir complete, arrived, in air og not started
        pass

    def list_of_all_voyages_for_selected_day(self, user_input_date):
        #"""Returns an unsorted list of voyages on that day that the other functions in this class wil be using. The outcome of this function will never appear in the interface"""
        #voyage_list = self.ioapi.get_all_voyages_list()
        #return voyage_list
        pass