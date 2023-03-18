from datetime import datetime
import datetime
import os
import utils.utils as utils
import json

from string import Template
from utils.utils import DeltaTemplate


class NinetyNineHours:


    def __init__(self) -> None:
        os.system('cls' if os.name == 'nt' else clear)
        self.init_time = datetime.datetime(2023,3,15,8,30,0)
        self.end_time = self.init_time + datetime.timedelta(hours=99, minutes=59)


    def run(self):
        os.system('cls' if os.name == 'nt' else clear)
        current_time = datetime.datetime.now()
        print('Start: ', self.init_time.strftime('%A\t%Y-%m-%d %H:%M:%D'))
        print('Current: ',current_time.strftime('%A\t%Y-%m-%d %H:%M:%D'))
        print('End: ', self.end_time.strftime('%A\t\t%Y-%m-%d %H:%M:%D'))


        missing_time = self.end_time- current_time
        print ('Hours Left: ', DeltaTemplate.strfdelta(missing_time, "%H:%M:%S"))

        percent_time_elapsed = ((current_time - self.init_time) / (self.end_time - self.init_time)) * 100
        print('Percentaje Elapsed: ', round(percent_time_elapsed,2) , "%")

        a = input("Press enter to continue")
        os.system('cls' if os.name == 'nt' else clear)

        
    #     print('\n')
    #     print("Goals:")
    #     utils.printl(self.tasks)


    #     nnh_done = []
    #     nnh_done.append({'Fix clean and not lose old tasks', 20})
    #     nnh_done.append({'Allow entering tasks by cli command', 20})
    #     nnh_done.append({'Clear screen in next run ', 5})
    #     nnh_done.append({'Input to allow view tables', 5})
    #     nnh_done.append({'Fix menu, allow quiting'})
    #     nnh_done.append({'dont allow less than 2 letters'})
    #     nnh_done.append({'Make 99_hours a class', 20})
    #     nnh_done.append({'Make print list above other', 10})
    #     print('\n')
    #     print("Tasks Done:")
    #     utils.printl(nnh_done)




    #     Milestones = []
    #     Milestones.append({'project':'MYCliApp ', 'Prio':'1', 'Milestone':'Basic version of 99 hours organization'})
    #     Milestones.append({'project':'D4E ', 'Prio':'2', 'Milestone':'End all lessons'})
    #     print('\n')
    #     print("Milestones:")
    #     utils.printl(Milestones)



    #     class Project():
    #         pass


    #     questions = []
    #     questions.append('From which class should I inherit to create an app')
    #     questions.append('TDD in Python')
    #     print('\n')
    #     print("Questions:")
    #     utils.printl(questions)

    #     rules_alignments = []
    #     rules_alignments.append("Estas a tu ritmo, lo que te importa es aprender")
    #     rules_alignments.append("No cellphone on desk")
    #     rules_alignments.append("Do it without thinking to much")
    #     rules_alignments.append("Don't celebrate. Dont't blame. No excuses. ")
    #     rules_alignments.append("Create a schedule and respect it")
    #     rules_alignments.append("One day weekly to work on my personal project")

    #     print('\n')
    #     print("Rules:")
    #     utils.printl(rules_alignments)
    #     a = input("Press enter to continue")
    #     os.system('cls' if os.name == 'nt' else clear)

    
    # def load_tasks(self):
    #     self.tasks.append({'Small code organization', 10})
    #     self.tasks.append({'Persist task on json', 10})
    #     # self.tasks.append({'Enter a task manually', 15})
    #     self.tasks.append({'Add starting session time logic ', 15})
    #     self.tasks.append({'Fix chatpgt app integration', 15})
    #     self.tasks.append({'Join all cli applications into one, allow multiple apps to connect to menu', 60})
    #     self.tasks.append({'Fix time format at begginning', 10})
    #     self.tasks.append({'Fix saving in json, app init', 20})
    #     self.tasks.append({'Implement test driven development', 3 * 24 * 60})
    #     self.tasks.append({'Allow entering this options not by code', 40})
    #     self.tasks.append({'chatgpt: add hability to call directly from root', 120})
    #     self.tasks.append({'Configure chatGPT to manage context', 1 * 24* 60})
    #     self.tasks.append({'Divide in classes ie: Project, Goal, Task, Achievements, Rules, Alignments', 1 * 24* 60})
    #     self.tasks.append({'Make a new profile as a python proficient', 1 * 24 * 60})



        
