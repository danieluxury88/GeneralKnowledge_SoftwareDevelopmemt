# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import datetime
import json
import os

import markdown2
import openai


class ChatGPTHandler:

    chat_role = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: January 2022 Current date: March 2023"

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
            print(f"The API key is: {api_key}")
            openai.api_key = api_key
            return True
        else:
            print("The API key is not set.")
            # return False
            exit(1)

    def ask_chat_gpt(self, question):
        user_request = {
            "index": self.user_request_index,
            "question": question,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        primer = self.chat_role
        mx_tokens = self.max_tokens
        # question = "how can I request for use to input a string response in python? something similar to scanf or cin"
        # question = "Can you list the 20 most appreciated mid level free certificates in Computer Science industry?"
        chatgpt_reponse = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": primer},
                {"role": "user", "content": question},
                # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                # {"role": "user", "content": "Where was it played?"}
                # {"role": "assistant", "content": "One example is edx CS50."},
            ],
        )

        query = {"user_request": user_request, "chatgpt_response": chatgpt_reponse}
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


if __name__ == "__main__":
    handler = ChatGPTHandler()
    handler.run()
