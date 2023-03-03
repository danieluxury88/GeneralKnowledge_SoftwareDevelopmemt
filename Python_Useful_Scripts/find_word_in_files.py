import os
import re

folder_path = 'E:/MyProjects/'
file_name_pattern = "views.py"
word_to_search = "context"

print(f"searching {word_to_search} in {folder_path}" )

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith(file_name_pattern):
            file_path = os.path.join(root, file_name)
            with open(file_path, "r") as f:
                line_number = 0
                for line in f:
                    line_number += 1
                    if re.search(word_to_search, line, re.IGNORECASE):
                        print(f"Found '{word_to_search}' in file {file_path} {file_name} at line {line_number}:")
                        print(line.strip())
