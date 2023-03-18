import json
import os


class JsonFileHandler():
    def __init__(self):
        print("hello W")
        self.filename = None
        self.data = None

    def open_json_file(self, filename):
        self.filename = filename
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.data = json.load(file)
                self.user_request_index = len(self.data)
        else:
            self.data = []
            self.user_request_index = 0
        print("Opened file")


    def get_json_data(self):
        return self.data

    def save_json_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file)
        print("Saved file")

    def add_json_data(self, data):
        self.data.append(data)