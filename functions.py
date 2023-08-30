import os
import sys
from pathlib import Path
import re
from colorama import init, Fore
import constants
from lexicon import LEXICON

init(autoreset=True)


def clear():
    os.system("clear||cls")


def _create_contact_info() -> str:
    """
    Helper function for creating a new or changing an old contact
    :rtype: str
    :return: String that contains a new contact
    """
    answer: list = []
    for i in range(len(constants.patterns)):
        while True:
            string: str = input(Fore.GREEN + constants.patterns[i][0]).capitalize()
            if re.fullmatch(rf'{constants.patterns[i][1]}', string):
                answer.append(string)
                break
            else:
                clear()
                print(Fore.RED + constants.patterns[i][2])

    line: str = f"{answer[0]} {answer[1]} {answer[2]} {answer[3]} {answer[4]} {answer[5]}\n"
    return line


def show_all_contacts() -> None:
    """
    Function to display all available contacts
    :rtype: None
    """
    with open(constants.file_name, mode='r', encoding='utf-8') as file:
        clear()
        number: int = 1
        contacts: list = file.readlines()
        pages: int = len(contacts) // constants.contacts_per_page if len(
            contacts) % constants.contacts_per_page == 0 else (len(contacts) // constants.contacts_per_page) + 1
        print(LEXICON['list_of_contacts'])
        for line in contacts:
            print(Fore.LIGHTGREEN_EX + f"{number}: {line.strip()}")
            if number % constants.contacts_per_page == 0 and (number // constants.contacts_per_page) < pages:
                print(Fore.LIGHTCYAN_EX + f"Страница {(number // constants.contacts_per_page)} из {pages}".center(
                    os.get_terminal_size().columns))
                input(LEXICON['next_page'])
                clear()
                print(LEXICON['list_of_contacts'])

            elif number % constants.contacts_per_page == 0 and (number // constants.contacts_per_page) == pages:
                print(Fore.LIGHTCYAN_EX + f"Страница {pages} из {pages}".center(os.get_terminal_size().columns))
                input(LEXICON['exit'])
            elif number % constants.contacts_per_page != 0 and (
                    number // constants.contacts_per_page) + 1 == pages and line == contacts[-1]:
                print(Fore.LIGHTCYAN_EX + f"Страница {pages} из {pages}".center(os.get_terminal_size().columns))
                input(LEXICON['exit'])
            number += 1
    clear()


def add_contact() -> None:
    """
    Function to add a new contact to the phone book
    :rtype: None
    """
    clear()
    contact: str = _create_contact_info()
    with open(constants.file_name, 'a+', encoding='utf-8') as file:
        file.write(contact)
    print(constants.separator)


def search_contact() -> None:
    """
    Function to search for an existing contact
    :rtype: None
    """
    clear()
    while True:
        pattern: list = input(LEXICON['feature']).split()
        if not pattern:
            clear()
            print(LEXICON['no_feature'])
        else:
            break
    count: int = 0
    with open(constants.file_name, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            characters = [i.lower() for i in line.split()]
            a = all([i in characters for i in pattern])
            if a:
                print(line.strip())
                count += 1
    if not count:
        print(LEXICON['no_contact'])
    print(Fore.LIGHTCYAN_EX + constants.separator)


def change_contact_information() -> None:
    """
    Function to change an existing contact
    :rtype: None
    """
    clear()
    while True:
        pattern: list = input(LEXICON['feature']).split()
        if not pattern:
            clear()
            print(LEXICON['no_feature'])
        else:
            break
    count = 0
    with open(constants.file_name, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            characters = [i.lower() for i in line.split()]
            a = all([i in characters for i in pattern])
            if a:
                count += 1
                while True:
                    answer = input(f"{line.strip()} -- изменить этот контакт? Да/Нет: ").lower()
                    if answer not in constants.answer:
                        print(LEXICON['not_yes_no'])
                    else:
                        break
                if answer in constants.positive:
                    old_data = line
                    new_data = _create_contact_info()
                    path = Path(constants.file_name)
                    path.write_text(path.read_text().replace(old_data, new_data))
                    break
    if not count:
        print(LEXICON['no_contact'])
    print(constants.separator)


def telephone_book() -> None:
    """
    A function to process user input and send it to the appropriate function
    :rtype: None
    """
    print(LEXICON['hello'])
    try:
        action: int = int(input(LEXICON['input']))
    except ValueError:
        clear()
        print(LEXICON['wrong_input'])
    else:
        match action:
            case 0:
                sys.exit(print(LEXICON['goodbye']))
            case 1:
                show_all_contacts()
            case 2:
                add_contact()
            case 3:
                change_contact_information()
            case 4:
                search_contact()
            case _:
                clear()
                print(LEXICON['not_number'])
