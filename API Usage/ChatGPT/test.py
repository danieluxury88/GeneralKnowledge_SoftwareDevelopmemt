# import json

# # Create a JSON object
# json_obj = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# # Convert the JSON object to a string
# json_str = json.dumps(json_obj)

# # Print the JSON string
# print(json_str)

# # Access the elements of the JSON object
# print(json_obj["name"])
# print(json_obj["age"])
# print(json_obj["city"])


# #Sencon program

# import json

# my_list = [1, 2, 3, 4, 5]

# # Convert list to JSON formatted string
# json_string = json.dumps(my_list)

# # Write JSON string to a file
# with open('my_list.json', 'w') as file:
#     file.write(json_string)


#Third program
# import os
# import json

# filename = "data.json"

# if os.path.exists(filename):
#     # Load existing data from the file
#     with open(filename, "r") as file:
#         data = json.load(file)
# else:
#     # Create an empty list if the file doesn't exist
#     data = []

# # Add new data to the list
# new_data = {"key": "value"}
# data.append(new_data)

# # Save the updated data to the file
# with open(filename, "w") as file:
#     json.dump(data, file)

# print(data)

# import json
# import os

# os.system('clear')

# json_str = '{"name": "John", "age": 30}'



# filename = "test.json"
# if os.path.exists(filename):
#     with open(filename, "r") as file:
#         data = json.load(file)
#         user_request_index = len(data)
# else:
#     data = []
#     user_request_index = 0

# user_request = {
#     "index": user_request_index,
#     "question": "This is a question"
# }

# chatgpt_reponse = {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "You can add a key-value pair to a JSON object in Python by first loading the JSON into a dictionary, adding the key-value pair, and then dumping the dictionary back to a JSON string. Here's an example:\n\n```python\nimport json\n\n# JSON string\njson_str = '{\"name\": \"John\", \"age\": 30}'\n\n# Load JSON string into dictionary\ndata = json.loads(json_str)\n\n# Add key-value pair to dictionary\ndata['city'] = 'New York'\n\n# Dump dictionary to JSON string\nnew_json_str = json.dumps(data)\n\nprint(new_json_str)  # Output: {\"name\": \"John\", \"age\": 30, \"city\": \"New York\"}\n```\n\nIn this example, we first load the JSON string into a dictionary using the `json.loads()` method. We then add the key-value pair `\"city\": \"New York\"` to the dictionary. Finally, we dump the updated dictionary back to a JSON string using the `json.dumps()` method.",
#         "role": "assistant"
#       }
#     }
#   ],
#   "created": 1678380998,
#   "id": "chatcmpl-6sDrCasz5w4B0fTHX3MG9go9MveFc",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 207,
#     "prompt_tokens": 63,
#     "total_tokens": 270
#   }
# }

# query = {
#     "user_request": user_request,
#     "chatgpt_response": chatgpt_reponse,
#     "timestamp": datetime.datetime.now()
# }


# new_data = {"query": query}
# data.append(new_data)

# with open(filename, "w") as file:
#     json.dump(data, file)


# # print(query)
# # print(data)


# # # Load JSON string into dictionary
# # data = json.loads(json_str)

# # # Add key-value pair to dictionary
# # data['city'] = 'New York'

# # # Dump dictionary to JSON string
# # new_json_str = json.dumps(data)

# count = len([elem for elem in query ])
# counta = len(data)

# print(data[12]['query']['user_request'])
# response = data[user_request_index]['query']['chatgpt_response']['choices'][0]['message']['content']
# completion_tokens = data[user_request_index]['query']['chatgpt_response']['usage']['completion_tokens']
# prompt_tokens = data[user_request_index]['query']['chatgpt_response']['usage']['prompt_tokens']
# total_tokens = data[user_request_index]['query']['chatgpt_response']['usage']['total_tokens']

#   # "usage": {
#   #   "completion_tokens": 207,
#   #   "prompt_tokens": 63,
#   #   "total_tokens": 270
#   # }
# print(response)
# print(completion_tokens)
# print(prompt_tokens)
# # print(total_tokens)

# a =input("opcion 1")
# pause()
# b =input("opcion 1")


# <h1>Define the main menu options</h1>

MAIN_MENU = {
    '1': 'Option 1',
    '2': 'Option 2',
    '3': 'Nested Options',
    '0': 'Exit'
}

# <h1>Define the nested menus and their options</h1>

NESTED_MENU_1 = {
    '1': 'Nested Option 1',
    '2': 'Nested Option 2',
    '0': 'Back'
}

NESTED_MENU_2 = {
    '1': 'Nested Option 3',
    '2': 'Nested Option 4',
    '0': 'Back'
}

NESTED_MENUS = {
    '1': NESTED_MENU_1,
    '2': NESTED_MENU_2,
    '0': 'Back'
}

# Define a function to display a menu and get user input</h1>

def get_user_choice(menu):
  for key, value in menu.items():
    print(f'{key}: {value}')
  choice = input('Please enter your choice: ')
  return choice



# Define a function to execute the selected menu option

def execute_choice(choice):
  if choice == '1':
    print('Selected option 1.')
  elif choice == '2':
    print('Selected option 2.')
  elif choice == '3':
    nested_choice = ''
    while nested_choice != '0':
      nested_choice = get_user_choice(NESTED_MENUS)
    if (nested_choice == 0):
      return
      execute_choice(nested_choice)
  elif choice == '0':
    print('Exiting')
    exit()
  else:
    print('Choice...'+ choice + "/")

# <h1>Use a loop to continuously display the main menu until the user selects to exit

if __name__ == "__main__":
  while(True):
    choice = get_user_choice(MAIN_MENU)
    execute_choice(choice)
    dir(MAIN_MENU)