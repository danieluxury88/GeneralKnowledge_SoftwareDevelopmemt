def printl(list):
    for i, item in enumerate(list):
        print(i, item)


import os,json


class JsonHandler():

    def __init__(self):
        self.filename = None
        self.data = None
        self.temp_data = None
        self.num_elements = 0

    def open_json_file(self, filename):
        self.filename = filename
        print("open json")
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.data = json.load(file)
                self.num_elements = len(self.data)
        else:
            self.data = []
            self.num_elements = 0

    def save_json_file(self):
        print(type(self.temp_data))
        print(type(self.data))
        with open(self.filename, "w") as file:
            json.dump(self.temp_data, file)

    def get_json_data(self):
        return self.data
    
    def add_json_data(self, new_data):
        self.temp_data = new_data
        self.save_json_file()