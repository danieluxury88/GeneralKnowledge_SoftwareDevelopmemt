import utils.utils as utils
from utils.os_control import clear_terminal
from datetime import datetime
from utils.json_file_handler import JsonFileHandler
from utils.utils import DeltaTemplate

class ListHandler():

    def __init__(self, filename = None):
        print("Start App")
        self.jsonHandler = JsonFileHandler()
        self.filename = 'data/list.json' if filename is None else filename
        self.jsonHandler.open_json_file(self.filename)   
        self.list  = self.jsonHandler.get_json_data()

    def run(self):
        print("Run App")
        clear_terminal()
        option = input("Enter option: ")
        if option == 'n':
            self.__append_new_element_on_list()
        elif option == 'v':
            self.__print_tasks()
            input("Press a button to continue")
        elif option == 'vc':
            self.__print_current_task()
            input("Press a button to continue")
        print("Return to main")
            

    def __print_tasks(self):
        utils.printl(self.list)

    def __print_current_task(self):

        if not len(self.list) :
            print("Empty list")
        else:

            # parse the JSON object into a Python dictionary
            item = json.loads(self.list[-1])

            # access each value in the dictionary by key
            type_value = item['type']
            title_value = item['title']
            content_value = item['content']
            est_time_value = item['est_time']
            start_time_value = item['start_time']
            end_time_value = item['end_time']
            missing_time_value = item['missing_time']


            print(title_value, '-','Estimated time: ', est_time_value, ' minutes' )
            print(content_value, '\n')

            print("Current time: ", datetime.datetime.now())

            dt = datetime.datetime.strptime(start_time_value, '%Y-%m-%dT%H:%M:%S.%f')
            formatted_time = dt.strftime('%H:%M')
            print("Start time: ", formatted_time) 

            dt = datetime.datetime.strptime(end_time_value, '%Y-%m-%dT%H:%M:%S.%f')
            formatted_time = dt.strftime('%H:%M')
            print("End time:", formatted_time)

            print("Left time: ", missing_time_value/60, 'minutes') 






    def __append_new_element_on_list(self):
        clear_terminal()
        print("Append new element on list")
        title = input("Enter title:")
        content = input("Enter content: ")
        time = input("Enter estimated time: ")
        item = Item(title, content, int(time))
        serialized_item = item.serialize()
        self.jsonHandler.add_json_data(serialized_item)
        self.jsonHandler.save_json_file()
        self.list.append(serialized_item)
        

    
import datetime,json

class Item():
    def __init__(self, title, content, est_time):
        self.type = None
        self.title = title
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
        return f'{self.title} - StartTime: {self.start_time} - Est time: {self.est_time} minutes Mis: {missing_time_str}'
    

    def serialize(self):
        serialized_task = {
            'type' : 'D',
            'title': self.title,
            'content' : self.content,
            'est_time': self.est_time,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'missing_time': self.missing_time.total_seconds()
        }
        return json.dumps(serialized_task)

