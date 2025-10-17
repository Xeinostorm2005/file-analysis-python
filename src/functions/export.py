# Import necessary packages
import os
import json
import datetime

def export_results():
    
    # Store analyzed data
    data = {}

    # Templates to be used when exporting
    templates = {
        'txt': []
    }

    # Upload analyzed data from JSON file to the variable data
    with open('./src/data/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Uploads the TXT template
    with open('./src/data/template.txt', 'r', encoding='utf-8') as f:
        
        # Read line for line
        for line in f:
            
            # Replace {something} with real data
            line = line.replace("{file_name}", f'{data['file_name']}')
            line = line.replace("{file_path}", f'{data['file_path']}')
            line = line.replace("{file_size}", f'{data['file_size']}')

            line = line.replace("{number_of_lines}", f'{data['basic_statistics']['lines']}')
            line = line.replace("{number_of_words}", f'{data['basic_statistics']['words']}')
            line = line.replace("{number_of_characters}", f'{data['basic_statistics']['characters']}')
            line = line.replace("{words_per_line}", f'{data['basic_statistics']['words_per_line']}')
            line = line.replace("{character_per_word}", f'{data['basic_statistics']['character_per_word']}')

            # Adds the line to the template['txt'] variable
            templates['txt'].append(line)

    # Current timestamp:
    curtime = datetime.datetime.now()

    # The output path
    output_path = f'./output/{data['file_name']}-{curtime}/'
 
    # Checks if the directory exsists or not
    # If it doesn't, it will create a new one
    os.makedirs(output_path, exist_ok = True)

    # Export Analyzed Data into a TXT file using the provided template
    with open(f'{output_path}{data['file_name']}.txt', 'w', encoding='utf-8') as f:
        f.writelines(templates['txt'])


