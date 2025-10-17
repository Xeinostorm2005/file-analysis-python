# Imports necessary packages
import os
import json

# A function that analyzes a txt file then writes the results to json file
def analyze_file(path, file_name):

    # Check file size
    file_size_in_bytes = os.path.getsize(path)
    file_size_in_Mb = file_size_in_bytes / (1024 ** 2)

    # Stores the analyzed data
    # Will be dumped/written in JSON file
    data = {
        'file_name': file_name,
        'file_path': path,
        'file_size': round(file_size_in_Mb, 2),
        'basic_statistics': {
            'lines': 0,
            'words': 0,
            'characters': 0,
            'characters_without_spaces': 0,
            'words_per_line': 0,
            'character_per_word':0
        }
    }

    # Opens a file, then analyzes it
    with open(path, 'r', encoding='utf-8') as f:

        # Analyzes the file by collecting line for line
        for line in f:

            # Basic Statistics
            data['basic_statistics']['lines'] += 1
            data['basic_statistics']['words'] += len(line.split(' '))
            data['basic_statistics']['characters'] += len(line)
            data['basic_statistics']['characters_without_spaces'] += len(line.replace(' ', ''))
    
    # Basic Statistics
    data['basic_statistics']['words_per_line'] = round(data['basic_statistics']['words'] / data['basic_statistics']['lines'], 2)
    data['basic_statistics']['character_per_word'] = round(data['basic_statistics']['characters'] / data['basic_statistics']['words'], 2)



    # Writes the analyzed data to a JSON file
    with open('./src/data/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)