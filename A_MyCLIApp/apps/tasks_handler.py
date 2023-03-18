import utils.utils as utils
import os
from utils.json_file_handler import JsonFileHandler
from utils.utils import DeltaTemplate

class TasksHandler():
    low_level_task = []

    def __init__(self):
        self.jsonHandler = JsonFileHandler()
        self.jsonHandler.open_json_file('data/tasks.json')   
        self.tasks_list  = self.jsonHandler.get_json_data()

    def run(self):
        os.system('cls' if os.name == 'nt' else clear)
        option = input("Enter option: ")
        if option == 'n':
            self.create_new_task()
        elif option == 'v':
            self.print_tasks()
            input("Press a button to continue")
        elif option == 'vc':
            self.print_current_task()
            input("Press a button to continue")
        elif option == 't':
            self.test()
            

    def print_tasks(self):
        utils.printl(self.tasks_list)

    def print_current_task(self):
        print(self.tasks_list[-1])

    def create_new_task(self):
        os.system('cls' if os.name == 'nt' else clear)
        task = input("Enter task: ")
        time = input("Enter estimated time: ")
        task = Task(task, int(time))
        serialized_task = task.serialize()
        self.jsonHandler.add_json_data(serialized_task)
        self.jsonHandler.save_json_file()
        self.tasks_list.append(serialized_task)
        

    
import datetime,json

class Task():
    def __init__(self, task, est_time, project = None):
        self.task = task
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
            'task': self.task,
            'est_time': self.est_time,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'missing_time': self.missing_time.total_seconds()
        }
        return json.dumps(serialized_task)

