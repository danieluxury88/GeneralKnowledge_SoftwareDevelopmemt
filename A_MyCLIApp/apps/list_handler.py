import utils.utils as utils
import os
from utils.json_file_handler import JsonFileHandler
from utils.utils import DeltaTemplate

class ListHandler():

    def __init__(self):
        print("Start App")
        self.jsonHandler = JsonFileHandler()
        self.jsonHandler.open_json_file('data/test_list.json')   
        self.list  = self.jsonHandler.get_json_data()

    def run(self):
        print("Run App")
        os.system('cls' if os.name == 'nt' else clear)
        option = input("Enter option: ")
        if option == 'n':
            self.__append_new_element_on_list()
        elif option == 'v':
            self.__print_tasks()
            input("Press a button to continue")
        elif option == 'vc':
            self.__print_current_task()
            input("Press a button to continue")
        elif option == 't':
            self.test()
        print("Return to main")
            

    def __print_tasks(self):
        utils.printl(self.list)

    def __print_current_task(self):
        if len(self.list) :
            print(self.list[-1])
        else:
            print("Empty list")

    def __append_new_element_on_list(self):
        os.system('cls' if os.name == 'nt' else clear)
        print("Append new element on list")
        content = input("Enter task: ")
        time = input("Enter estimated time: ")
        item = Item(content, int(time))
        serialized_item = item.serialize()
        self.jsonHandler.add_json_data(serialized_item)
        self.jsonHandler.save_json_file()
        self.list.append(serialized_item)
        

    
import datetime,json

class Item():
    def __init__(self, content, est_time, project = None):
        self.type = None
        self.content = content
        self.est_time = est_time
        self.start_time = datetime.datetime.now()
        self.end_time = self.start_time + datetime.timedelta( minutes=est_time)
        current_time = datetime.datetime.now()
        self.missing_time = self.end_time - current_time



    def __str__(self):
        current_time = datetime.datetime.now()
        missing_time = self.end_time- current_time
        missing_time_str = DeltaTemplate.strfdelta(missing_time, "%M")
        return f'{self.task} - StartTime: {self.start_time} - Est time: {self.est_time} minutes Mis: {missing_time_str}'
    

    def serialize(self):
        serialized_task = {
            'type' : 'D',
            'content' : self.content,
            'est_time': self.est_time,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'missing_time': self.missing_time.total_seconds()
        }
        return json.dumps(serialized_task)

