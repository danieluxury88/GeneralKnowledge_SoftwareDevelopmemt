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
import os
import json

filename = "data.json"

if os.path.exists(filename):
    # Load existing data from the file
    with open(filename, "r") as file:
        data = json.load(file)
else:
    # Create an empty list if the file doesn't exist
    data = []

# Add new data to the list
new_data = {"key": "value"}
data.append(new_data)

# Save the updated data to the file
with open(filename, "w") as file:
    json.dump(data, file)

print(data)
