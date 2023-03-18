import os
import apps.chat_gpt_handler_api as chat_gpt_handler_api
import apps.ninety_nine_hours as ninety_nine_hours

import apps.list_handler as list_handler
import apps.tasks_handler as tasks_handler
import apps.milestones_handler as milestone_handler

import devtests.dev_test as dev_test


class CLIMenuHandler:
    def __init__(self):
        print("Init Main")
        self.chatgpt_app = chat_gpt_handler_api.ChatGPTHandler()
        self.nnnh_app = ninety_nine_hours.NinetyNineHours()
        self.tasks_app = tasks_handler.TasksHandler()
        self.list_app = list_handler.ListHandler('data/list.json')
        self.milestone_app = milestone_handler.MilestoneHandler('data/milestone.json')
        self.bugs_app = milestone_handler.MilestoneHandler('data/bugs.json')

        self.MAIN_MENU = {
            ' ': 'Question',
            'c': 'Configure Chat',
            'n': '99Hours',
            'm': 'Milestones',
            't': 'Tasks',
            'b': 'Bugs',
            'l': 'List',
            'd': 'DevTest',
            'q': 'Quit',
        }
        os.system('cls' if os.name == 'nt' else clear)
 

    def get_user_choice(self, menu):
        for key, value in menu.items():
            print(f'{key}: {value}')
        choice = input('Please enter your choice: ')
        return choice


    def execute_choice(self, choice):
        if choice == '0' or choice == 'q':
            print('Exiting')
            exit()
        elif choice == 'd': # Development
            self.dev_app.run()
        elif choice == 'l': # List
            self.list_app.run()
        elif choice == 'n': # 99 Hours
            self.nnnh_app.run()
        elif choice == 'm': # Milestones
            self.milestone_app.run()
        elif choice == 't': # Tasks
            self.tasks_app.run()
        elif choice == 'b': # Bugs
            self.bugs_app.run()
        elif choice == 'c': # Configure Chat
            self.chatgpt_app.configure()
        else:
            question = choice   #Chat GPT question
            self.chatgpt_app.execute(question)


    def run(self):
        print("Start Main")
        while(True):
            choice = self.get_user_choice(self.MAIN_MENU)
            self.execute_choice(choice)
            os.system('cls' if os.name == 'nt' else clear)


if __name__ == "__main__":
    menu_handler = CLIMenuHandler()
    menu_handler.run()
    #! Feature: add ability to print current task when closing program
    menu_handler.tasks_app.print_current_task()
    