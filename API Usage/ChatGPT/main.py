# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import json
import openai




class ChatGPTHandler():

    def __init__(self) -> None:
        filename = None
        data = None

    def open_json_file(self, filename):
        self.filename = filename
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        else:
            self.data = []

    def save_json_file(self):
                # Save the updated data to the file
        with open(self.filename, "w") as file:
            json.dump(self.data, file)

    def look_for_api_key(self):
        api_key = os.environ.get('GPT_API_KEY')
        if api_key:
            print(f'The API key is: {api_key}')
            openai.api_key = api_key
            return True
        else:
            print('The API key is not set.')
            # return False
            exit(1)

    def ask_chat_gpt(self, question):
        new_data = {"question": question}
        self.data.append(new_data)



        # question = "how can I request for use to input a string response in python? something similar to scanf or cin"
        # question = "Can you list the 20 most appreciated mid level free certificates in Computer Science industry?"
        primer = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: January 2022 Current date: March 2023"
        json_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": primer},
                {"role": "user", "content": question },
                # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                # {"role": "user", "content": "Where was it played?"}
                # {"role": "assistant", "content": "One example is edx CS50."},

            ]
        )
        print(type(json_response))

        print(json_response)

        print(self.data)
        print(json_response['choices'][0]['message']['content'])


    def run(self):
        self.look_for_api_key()
        self.open_json_file("data.json")
        while True:
            question = input("Enter a question or 'quit' to exit: ")
            if question == "quit":
                break
            else:
                self.ask_chat_gpt(question)

    # Execute code for other commands here

if __name__ == "__main__":
    handler =ChatGPTHandler()
    handler.run()