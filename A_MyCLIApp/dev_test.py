# import utils
# import os

# class App():
#     low_level_task = []

#     def __init__(self):
#         print("init devApp")
#         self.jsonHandler = JsonHandler()
#         self.jsonHandler.open_json_file('test2.json')   
#         self.test_list  = self.jsonHandler.get_json_data()
#         print(self.test_list)

#     def run(self):
#         os.system('cls' if os.name == 'nt' else clear)
#         option = input("Enter option: ")
#         if option == 'n':
#             self.create_new_task()
#         elif option == 'v':
#             self.print_tasks()
#         elif option == 't':
#             self.test()


#     def print_tasks(self):
#         os.system('cls' if os.name == 'nt' else clear)
#         print("Low Level Task:")
#         utils.printl(self.test_list)
#         input("Press a button to continue")

#     def create_new_task(self):
#         os.system('cls' if os.name == 'nt' else clear)
#         task = input("Enter task: ")
#         time = input("Enter estimated time: ")
#         task = Task(task, int(time))
#         self.jsonHandler.add_json_data(task.serialize())
#         self.print_tasks()
        


#     def test(self):
#         print("hello")
#         js = JsonHandler()
#         js.open_json_file('test.json')
#         task = Task('test 1', 3)
#         js.add_json_data(task.serialize())
#         input("Press a button to continue")


# from string import Template

# class DeltaTemplate(Template):
#     delimiter = "%"

#     @staticmethod
#     def strfdelta(tdelta, fmt):
#         d = {"D": tdelta.days}
#         d["H"], rem = divmod(tdelta.seconds, 3600)
#         d["M"], d["S"] = divmod(rem, 60)
#         d["H"] = d["H"] + tdelta.days * 24
#         t = DeltaTemplate(fmt)
#         return t.substitute(**d)
    
# import datetime,json

# class Task():
#     def __init__(self, task, est_time, project = None):
#         self.task = task
#         self.est_time = est_time
#         self.start_time = datetime.datetime.now()
#         self.end_time = self.start_time + datetime.timedelta( minutes=est_time)
#         current_time = datetime.datetime.now()
#         self.missing_time = self.end_time - current_time



#     def __str__(self):
#         current_time = datetime.datetime.now()
#         missing_time = self.end_time- current_time
#         missing_time_str = DeltaTemplate.strfdelta(missing_time, "%M")
#         return f'{self.task} - StartTime: {self.start_time} - Est time: {self.est_time} minutes Mis: {missing_time_str}'
    

#     def serialize(self):
#         serialized_task = {
#             'task': self.task,
#             'est_time': self.est_time,
#             'start_time': self.start_time.isoformat(),
#             'end_time': self.end_time.isoformat(),
#             'missing_time': self.missing_time.total_seconds()
#         }
#         return json.dumps(serialized_task)


# # def log_details(self):
# #     missing_time = self.end_time- current_time
# #     print ('Time left: ', DeltaTemplate.strfdelta(missing_time, "%H:%M:%S"))
# #     return f'{self.task} - StartTime: {self.start_time} - Est time: {self.est_time} minutes'

