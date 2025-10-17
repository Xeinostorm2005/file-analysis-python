# Imports from /src folder
from src.functions.logo import logo
from src.stages.select_file import file_selection
from src.stages.results import results_menu


# The main function that will handle the program
def main():

    # Temporary data to keep track of where the user is at in the program
    stage = 'select_file'


    # Keeps the program running
    while True:

        # Prints the meta data (e.g Logo, Title and description)
        logo()


        # Checks where the user is at in the program
        if stage == 'select_file':
            
            # Executes select_file stage
            # Will return 'completed' or 'empty'
            status = file_selection()

            # Checks if the stage has been completed
            if status == 'completed':
                stage = 'results'
                continue

            # Checks if the sage has failed
            elif status == 'empty':
                stage = 'select_file'

                print('\nPlease add a text file to the input directory.\n')
                input('\nPress enter to continue...')
                continue
            
            # Checks if the user has chosen to exit the program.
            elif status == 'exit':
                stage = 'exit'
                continue


        # Checks if it's time to show results
        # Thats after the user choosing a file to analyze
        # The file will NOT be empty
        elif stage == 'results':
            status = results_menu()

            if status == 'exit':
                stage = 'exit'
                continue


        # Checks if the user wants to exit the program.
        # Going to do this instead of using exit()
        # Because Jupyter Sucks!!
        else:
            print('Thank you for using our File Analyzer! :)\n')
            break
            
        
    