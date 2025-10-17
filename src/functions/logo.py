# Imports packages
import os

# Imports from /src folder
from src.functions.color import color

# Prints meta data like logo, title and description
def logo():

    # Meta Data
    META = {
        'title': 'Text Analysis - Python Project',
        'description': 'A Python-based text analysis tool that processes large books or documents. \nThe program supports exporting results to multiple file types (TXT,Json and XML)',
        "logo": "\n\n████████╗███████╗██╗  ██╗████████╗     █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗██╗███████╗\n╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██║██╔════╝\n   ██║   █████╗   ╚███╔╝    ██║       ███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗██║███████╗\n   ██║   ██╔══╝   ██╔██╗    ██║       ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║██║╚════██║\n   ██║   ███████╗██╔╝ ██╗   ██║       ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║██║███████║\n   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝╚══════╝"
    }

    # Clears the terminal and Changes the title
    os.system('cls' if os.name == 'nt' else 'clear')

    # Colors then prints the Meta Data
    print(color(text=META['logo'], fg='255; 205; 0' ))
    print("\n\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n")
    print(f"{META['title']} \n{color(text=META['description'], fg='94; 94; 94')}")
    print("\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n")
