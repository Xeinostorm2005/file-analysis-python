# Imports packages
import os

# Import from /src folder
from src.functions.color import color
from src.functions.analyze import analyze_file

# File Selection - User chooses a file from the 'input' directory that MIGHT have .txt files.
# We will only showcase the '.txt' files even if there are other files in the directory.
def file_selection():

    # Temporary data to store
    data = { 
        'length': 0, 
        'selected_path': '',
        'paths': ['Exit']
    }

    title = '\nFile Selection - Select a .txt file from the "input" directory\n'
    print(color(title, fg='255; 94; 0', bold=True))

    # Checks which files/folders are in the directory.
    # Appends only TXT files!
    for file in os.listdir('./input/'):
        if file.endswith('.txt'):
            data['length'] += 1
            data['paths'].append(file)
    

    # Checks how many files found in the directory
    # If there are 0 files then it will raise an Error
    if data['length'] == 0:
        message = '\nThere are no .TXT files in the input directory!\n'
        print(color(message, fg='255; 0; 0'))
        return 'empty'
    
    print('Found these files in the input directory:\n')

    # Prints the .txt files that has been found in the directory
    for index, path in enumerate(data['paths']):
        message = f'{index: >3} - {path}'
        print(color(message, fg= '90; 90; 90'))

    print(f'\nSelect a file to analyze: {color(f'(0-{data['length']})')}')

    # A loop to keep the answer/input running until it is valid
    while True:

        # Asks the user for the input and then catches any value- or zero division error
        try:
            select_option = int(input('\n~> '))

            # Checks if the input is less/larger than 0/length
            if select_option < 0 or select_option > data['length']:
                raise ValueError
            
            # Checks if the user wants to exit
            if select_option == 0:
                return 'exit'
            # Updates selected_path
            else:
                data['selected_path'] = data['paths'][select_option]
            
            # Forwards the selected path and the name of the file to the file analyzer function
            analyze_file(f'./input/{data['selected_path']}', f'{data['selected_path'].replace('.txt', '')}')
            break

        # Handels when user inputs less/larger than 0/length
        except ValueError:
            message = '\nInvalid option, please try again.\n'
            print(color(message, fg='255; 0; 0'))
            continue
        
        # Handels empty files.
        except ZeroDivisionError:
            message = '\nFile is empty! Please try again.\n'
            print(color(message, fg='255; 0; 0'))
            continue
    
    return 'completed'