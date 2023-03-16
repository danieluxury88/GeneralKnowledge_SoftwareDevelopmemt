# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import ninety_nine_hours
import chat_gpt_handler_api
import dev_test


class CLIMenuHandler:

    # Define a function to display a menu and get user input</h1>
    def __init__(self):
        self.chatgpt_app = chat_gpt_handler_api.ChatGPTHandler()
        self.nnnh_app = ninety_nine_hours.NinetyNineHours()
        self.dev_app = dev_test.App()
    
        self.MAIN_MENU = {
            ' ': 'Question',
            'n': '99Hours',
            't': 'Enter new task',
            'd': 'DevTest',
            
            '1': 'Option 1',
            '2': 'Option 2',
            '3': 'Nested Options',
            'c': 'Clear',
            'o': 'Fast Options',
            'q': 'Quit',
            '0': 'Exit'
        }

        self.NESTED_MENU_1 = {
            '1': 'Nested Option 1',
            '2': 'Nested Option 2',
            '0': 'Back'
        }

        self.NESTED_MENU_2 = {
            '1': 'Nested Option 3',
            '2': 'Nested Option 4',
            '0': 'Back'
        }

        self.NESTED_MENUS = {
            '1': self.NESTED_MENU_1,
            '2': self.NESTED_MENU_2,
            '0': 'Back'
        }



        self.FAST_OPTIONS_MENUS = {
            'e': 'endulzar',
            'd': 'default mode',
            '0': 'Back',
        }
        os.system('cls' if os.name == 'nt' else clear)

        

    def get_user_choice(self, menu):
        for key, value in menu.items():
            print(f'{key}: {value}')
        choice = input('Please enter your choice: ')
        return choice



    # Define a function to execute the selected menu option+
    def execute_choice(self, choice):
        if choice == '1':
            print('Selected option 1.')
        elif choice == '2':
            print('Selected option 2.')
        elif choice == '3':
            nested_choice = ''
            while nested_choice != '0':
                nested_choice = self.get_user_choice(self.NESTED_MENUS)
                if (nested_choice == 0):
                    return
                self.execute_choice(nested_choice)
        elif choice == '0' or choice == 'q':
            print('Exiting')
            exit()
        elif choice == 'c':
            os.system("clear")
        elif choice == 'o':
            nested_choice = ''
            while nested_choice != '0':
                nested_choice = self.get_user_choice(self.FAST_OPTIONS_MENUS)
                if (nested_choice == '0'):
                    return
                elif nested_choice == 'e':
                    self.chatgpt_app.configure('e')
                    return
            self.execute_choice(nested_choice)

        elif choice == 'n':
            self.nnnh_app.run()
        elif choice == 't':
            self.nnnh_app.add_task()
        elif choice == 'd':
            self.dev_app.run()
        else:
            question = choice
            self.chatgpt_app.execute(question)


    def run(self):
        while(True):
            choice = self.get_user_choice(self.MAIN_MENU)
            self.execute_choice(choice)
            os.system('cls' if os.name == 'nt' else clear)


if __name__ == "__main__":
    menu_handler = CLIMenuHandler()
    menu_handler.run()
    