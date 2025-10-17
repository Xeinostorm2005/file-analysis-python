# Import from /src folder
from src.functions.color import color
from src.functions.logo import logo
from src.visualize.basic_statistics import basic_statistics
from src.functions.export import export_results
# Results - Where user chooses which results should be displayed
def results_menu():

    # Results Selection
    print(color('Results - View Statistics / Graphs\n', fg='255; 94; 0', bold=True))
    print(color('Select an option:\n', end_fg='80; 80; 80'))

    print(f'{'1':>3} - Basic statistics')
    print(f'{'2':>3} - Word analysis')
    print(f'{'3':>3} - Sentence analysis')
    print(f'{'4':>3} - Character analysis')
    print(f'{'5':>3} - Export all results')
    print(f'{'0':>3} - Exit')

    # Keeps the input running until it's valid
    while True:

        # Catches error
        try:
            select_option = int(input('\n~> '))

            # Checks if it's out of the interval
            if select_option < 0 or select_option > 5:
                raise ValueError
            
            break

        # Catches selected option when it exceeds the interval
        except ValueError:
            print(color('Invalid option, please try again.', fg='255; 0; 0'))
            continue

    # Matches the selected option with the right subject/option
    match select_option:
        case 1:
            menu('basic_statistics')
        case 2:
            menu('word_analysis')
        case 3:
            menu('sentence_analysis')
        case 4:
            menu('character_analysis')
        case 5:
            export_results()
            print('Results are exported')
            input('Press enter to continue...')
        case 0:
            return 'exit'


# Menu for each analysis
def menu(option):

    # Re-loads the metadata
    logo()

    print(f'\nYou have chosen {option.replace('_', ' ')} option\n')

    question = 'Choose one of the following options:'

    print(color(question, end_fg='80; 80; 80'))

    print(f'{'1.':>3} View using Matplotlib')
    print(f'{'2.':>3} View it here in the terminal')
    print(f'{'3.':>3} back')

    while True:
        try:
            selected = int(input('\n~> '))

            match selected:
                case 1:
                    basic_statistics('matplotlib')
                    menu(option)
                case 2:
                    print('Coming soon...')
                case 3:
                    return
        
        except ValueError:
            message = 'Invalid option, please try again.\n'
            print(color(message, fg='255; 0; 0'))