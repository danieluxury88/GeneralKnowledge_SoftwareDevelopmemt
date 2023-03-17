# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import datetime
import os
import markdown2

import openai
from openai.error import RateLimitError

from json_file_handler import JsonFileHandler






class ChatGPTHandler:
    chat_role = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: January 2022 Current date: March 2023"
    request_type =""
    def __init__(self):
        user_request_index = 0
        max_tokens = 300
        self.json_handler = JsonFileHandler()
        self.json_handler.open_json_file('adata1.json')
        self.queries_list = self.json_handler.get_json_data()
        self.look_for_api_key()
        

    def look_for_api_key(self):
        api_key = os.environ.get("GPT_API_KEY")
        if api_key:
            print(f"API key validated")
            openai.api_key = api_key
            return True
        else:
            print("The API key is not set.")
            return False
            

    def get_request_type(self):
        if self.request_type == "endulzar":
           return "puedes endulzar esta frase: "
        return self.request_type

    def ask_chat_gpt(self, question):
        primer = self.chat_role
        user_request = {            
            "question": question,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # question = "how can I request for use to input a string response in python? something similar to scanf or cin"
        # question = "Can you list the 20 most appreciated mid level free certificates in Computer Science industry?"
        try:
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
            self.queries_list.append(new_data)
            self.json_handler.add_json_data(new_data)
            self.json_handler.save_json_file()

        except RateLimitError as error:
            print("Encountered a RateLimitError:", error)
            print("Retry in 30 seconds...")
        
    def get_last_response(self):
        return self.queries_list[-1]["query"]["chatgpt_response"]["choices"][0]["message"][
            "content"
        ]

    def get_last_question(self):
        return self.queries_list[-1]["query"]["user_request"]["question"]

    def format_as_markdown(self, content):
        return markdown2.markdown(content)

    def log_last_conversation(self):
        question = self.get_last_response()
        response = self.get_last_question()
        response_md = self.format_as_markdown(response)
        print(question, end="\n\n")
        print(response_md, end="\n\n")
        self.log_last_query_tokens_usage()
        input("Press a key to continue")

    def log_last_query_tokens_usage(self):
        completion_tokens = self.queries_list[-1]["query"]["chatgpt_response"]["usage"][
            "completion_tokens"
        ]
        prompt_tokens = self.queries_list[-1]["query"]["chatgpt_response"]["usage"][
            "prompt_tokens"
        ]
        total_tokens = self.queries_list[-1]["query"]["chatgpt_response"]["usage"][
            "total_tokens"
        ]
        tokens_usage = f"Total Tokens: {total_tokens} (Completion: {completion_tokens}/Prompt: {prompt_tokens})"
        print(tokens_usage)

    def configure(self):
        option = input("Enter option")
        if option =='e':
            self.request_type = "endulzar"
        elif option =='d':
            self.request_type = ""
        elif option =='r':
            self.log_last_conversation()

    def execute(self, question):
        if len(question) < 3:
            print("Enter at least 3 letters")
            return
        self.look_for_api_key()
        self.ask_chat_gpt(question)
        self.log_last_conversation()
        
