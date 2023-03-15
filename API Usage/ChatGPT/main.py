# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import datetime
import json
import os

import markdown2
import openai


class ChatGPTHandler:

    chat_role = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: January 2022 Current date: March 2023"
    request_type =""
    def __init__(self):
        filename = None
        data = None
        user_request_index = 0
        max_tokens = 300


    def open_json_file(self, filename):
        self.filename = filename
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.data = json.load(file)
                self.user_request_index = len(self.data)
        else:
            self.data = []
            self.user_request_index = 0

    def save_json_file(self):

        with open(self.filename, "w") as file:
            json.dump(self.data, file)

    def look_for_api_key(self):
        api_key = os.environ.get("GPT_API_KEY")
        if api_key:
            print(f"The API validated")
            openai.api_key = api_key
            return True
        else:
            print("The API key is not set.")
            # return False
            exit(1)

    def get_request_type(self):
        if self.request_type == "endulzar":
           return "puedes endulzar esta frase: "
        return self.request_type

    def ask_chat_gpt(self, question):
        user_request = {
            "index": self.user_request_index,
            "question": question,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        primer = self.chat_role
        # question = "how can I request for use to input a string response in python? something similar to scanf or cin"
        # question = "Can you list the 20 most appreciated mid level free certificates in Computer Science industry?"
        chatgpt_reponse = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": primer},
                {"role": "user", "content": self.request_type + ' ' + question},
                # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                # {"role": "user", "content": "Where was it played?"}
                # {"role": "assistant", "content": "One example is edx CS50."},
            ],
        )

        query = {"option": self.request_type, "user_request": user_request, "chatgpt_response": chatgpt_reponse}
        new_data = {"query": query}
        self.data.append(new_data)
        self.save_json_file()

    def get_last_response(self):
        return self.data[-1]["query"]["chatgpt_response"]["choices"][0]["message"][
            "content"
        ]

    def get_last_question(self):
        return self.data[-1]["query"]["user_request"]["question"]

    def format_as_markdown(self, content):
        return markdown2.markdown(content)

    def log_last_query_tokens_usage(self):
        completion_tokens = self.data[-1]["query"]["chatgpt_response"]["usage"][
            "completion_tokens"
        ]
        prompt_tokens = self.data[-1]["query"]["chatgpt_response"]["usage"][
            "prompt_tokens"
        ]
        total_tokens = self.data[-1]["query"]["chatgpt_response"]["usage"][
            "total_tokens"
        ]
        tokens_usage = f"Total Tokens: {total_tokens} (Completion: {completion_tokens}/Prompt: {prompt_tokens})"
        print(tokens_usage)

    def run(self):
        self.look_for_api_key()
        self.open_json_file("data.json")
        while True:
            option = input("Enter a question or 'quit' to exit: ")
            if option in ["quit", "exit"]:
                break
            elif option in ["endulzar"]:
                self.request_type = "endulzar"
            elif option == "clear":
                os.system("clear")
                os.system("clswhat")
            elif option == "set role":
                role = input(
                    "Instruct the role of ChatGPT : \nie: You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: January 2022 Current date: March 2023\n"
                )
                self.chat_role = role
            # elif option == "set max tokens":
            #     max_tokens = input("Set max tokens")
            #     self.max_tokens = max_tokens
            else:
                question = option
                self.ask_chat_gpt(question)
                question = self.get_last_question()
                response = self.get_last_response()
                response_md = self.format_as_markdown(response)

                print(question, end="\n\n")
                print(response_md, end="\n\n")
                self.log_last_query_tokens_usage()


    def execute(self, question):
        self.look_for_api_key()
        self.open_json_file("data.json")
        self.ask_chat_gpt(question)
        question = self.get_last_question()
        response = self.get_last_response()
        response_md = self.format_as_markdown(response)

        print(question, end="\n\n")
        print(response_md, end="\n\n")
        self.log_last_query_tokens_usage()

    def configure(self, option):
        if option =='e':
            self.request_type = "endulzar"
        elif option =='d':
            self.request_type = ""




# <h1>Define the nested menus and their options</h1>


class CLIMenuHandler:

    # Define a function to display a menu and get user input</h1>
    def __init__(self):
        app = None
        self.MAIN_MENU = {
            ' ': 'Question',
            '1': 'Option 1',
            '2': 'Option 2',
            '3': 'Nested Options',
            'c': 'Clear',
            'o': 'Fast Options',
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


    def set_app(self, app):
        self.app = app
        

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
        elif choice == '0':
            print('Exiting')
            exit()
        elif choice == 'c':
            os.system("clear")
            os.system("clswhat")
        elif choice == 'o':
            nested_choice = ''
            while nested_choice != '0':
                nested_choice = self.get_user_choice(self.FAST_OPTIONS_MENUS)
                if (nested_choice == '0'):
                    return
                elif nested_choice == 'e':
                    self.app.configure('e')
                    return
            self.execute_choice(nested_choice)
        else:
            question = choice
            self.app.execute(question)


    def run(self):
        while(True):
            choice = self.get_user_choice(self.MAIN_MENU)
            self.execute_choice(choice)


if __name__ == "__main__":
    menu_handler = CLIMenuHandler()
    chat_gpt_app = ChatGPTHandler()
    menu_handler.set_app(chat_gpt_app)
    menu_handler.run()
    