import os
from pathlib import Path
import sys
import re
from colorama import init, Fore

init(autoreset=True)

commands: str = ("---Чтобы вывести все контакты из справочник введите: 1\n"
                 "---Чтобы добавить новую запись в справочник введите: 2\n"
                 "---Чтобы отредактировать уже имеющуюся запись введите: 3\n"
                 "---Чтобы найти запись по характеристикам введите: 4\n"
                 "---Чтобы выйти из справочника введите: 0")
separator: str = '----------------------------------------------------------'


def _create_contact_info() -> str:
    """
    Helper function for creating a new or changing an old contact
    :return: str
    """
    patterns: list = [['Введите фамилию: ', '[a-zA-Zа-яА-ЯёЁ-]+', 'Фамилия должна состоять только из букв'],
                      ['Введите имя: ', '[a-zA-Zа-яА-ЯёЁ-]+', 'Имя должно состоять только из букв'],
                      ['Введите отчество: ', '[a-zA-Zа-яА-ЯёЁ-]+', 'Отчество должно состоять только из букв'],
                      ['Введите название организации\n'
                       '(Название организации необходимо написать без пробелов. '
                       'Допускается использовать символы - \' \"): ', '[a-zA-Zа-яА-Я-\'\"]+',
                       'Неверное название организации'],
                      ['Введите рабочий номер телефона: ', "[0-9+()-]+",
                       'Неверный номер телефона. Допускаются символы +-()'],
                      ['Введите личный номер телефона: ', "[0-9+()-]+",
                       'Неверный номер телефона. Допускаются символы +-()']]
    answer: list = []
    for i in range(len(patterns)):
        while True:
            string: str = input(Fore.GREEN + patterns[i][0]).capitalize()
            if re.fullmatch(rf'{patterns[i][1]}', string):
                answer.append(string)
                break
            else:
                os.system("clear||cls")
                print(Fore.RED + patterns[i][2])

    line: str = f"{answer[0]} {answer[1]} {answer[2]} {answer[3]} {answer[4]} {answer[5]}\n"
    return line


def show_all_contacts() -> None:
    """
    Function to display all available contacts
    :return: None
    """
    with open('telephone_book.txt', mode='r', encoding='utf-8') as file:
        os.system("clear||cls")
        number: int = 1
        contacts: list = file.readlines()
        pages = len(contacts) // 8 if len(contacts) % 8 == 0 else (len(contacts) // 8) + 1
        print(Fore.LIGHTYELLOW_EX + 'Список контактов:'.center(os.get_terminal_size().columns))
        for line in contacts:
            print(Fore.LIGHTGREEN_EX + f"{number}: {line.strip()}")
            if number % 8 == 0 and (number // 8) < pages:
                print(Fore.LIGHTCYAN_EX + f"Страница {(number // 8)} из {pages}".center(os.get_terminal_size().columns))
                input(Fore.MAGENTA + 'Next page')
                os.system("clear||cls")
                print(Fore.LIGHTYELLOW_EX + 'Список контактов:'.center(os.get_terminal_size().columns))

            elif number % 8 == 0 and (number // 8) == pages:
                print(Fore.LIGHTCYAN_EX + f"Страница {pages} из {pages}".center(os.get_terminal_size().columns))
                input(Fore.MAGENTA + 'Exit')
            elif number % 8 != 0 and (number // 8) + 1 == pages and line == contacts[-1]:
                print(Fore.LIGHTCYAN_EX + f"Страница {pages} из {pages}".center(os.get_terminal_size().columns))
                input(Fore.MAGENTA + 'Exit')
            number += 1
    os.system("clear||cls")
    telephone_book()


def add_contact() -> None:
    """
    Function to add a new contact to the phone book
    :return: None
    """
    os.system("clear||cls")
    contact: str = _create_contact_info()
    with open('telephone_book.txt', 'a+', encoding='utf-8') as file:
        file.write(contact)
    print(Fore.LIGHTRED_EX + separator)
    telephone_book()


def search_contact() -> None:
    """
    Function to search for an existing contact
    :return: None
    """
    os.system("clear||cls")
    while True:
        pattern: list = input(Fore.LIGHTGREEN_EX + 'Введите характеристики для поиска через пробел: ').split()
        if not pattern:
            os.system("clear||cls")
            print(Fore.LIGHTRED_EX + "Не предоставлено ни одной характеристики для поиска")
        else:
            break
    count: int = 0
    with open('telephone_book.txt', mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            characters = [i.lower() for i in line.split()]
            a = all([i in characters for i in pattern])
            if a:
                print(line.strip())
                count += 1
    if not count:
        print('К сожалению контакта, подходящего вашему описанию не найдено.')
    print(Fore.LIGHTCYAN_EX + separator)
    telephone_book()


def change_contact_information() -> None:
    """
    Function to change an existing contact
    :return: None
    """
    os.system("clear||cls")
    while True:
        pattern: list = input(Fore.LIGHTGREEN_EX + 'Введите характеристики для поиска через пробел: ').split()
        if not pattern:
            os.system("clear||cls")
            print(Fore.LIGHTRED_EX + "Не предоставлено ни одной характеристики для поиска")
        else:
            break
    count = 0
    with open('telephone_book.txt', mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            characters = [i.lower() for i in line.split()]
            a = all([i in characters for i in pattern])
            if a:
                count += 1
                while True:
                    answer = input(f"{line.strip()} -- изменить этот контакт? Да/Нет: ").lower()
                    if answer not in ['да', 'yes', 'y', 'n', 'no', 'нет']:
                        print("Непонятный ввод. Попробуйте еще раз.")
                    else:
                        break
                if answer in ['да', 'y', 'yes']:
                    old_data = line
                    new_data = _create_contact_info()
                    path = Path('telephone_book.txt')
                    path.write_text(path.read_text().replace(old_data, new_data))
                    break
    if not count:
        print('В списке контактов нет человека с такими данными.')
    print(Fore.LIGHTCYAN_EX + separator)
    telephone_book()


def telephone_book():
    """
    A function to process user input and send it to the appropriate function
    :return: None
    """
    print(Fore.GREEN + "Телефонный справочник".center(os.get_terminal_size().columns), end='\n\n')
    print(Fore.LIGHTCYAN_EX + f"{separator}\n{commands}\n{separator}\n\n")
    while True:
        try:
            action: int = int(input(Fore.CYAN + "####phone_book$$ "))
        except ValueError:
            print(Fore.LIGHTRED_EX + 'Неверные входные данные')
        else:
            match action:
                case 0:
                    sys.exit(print(Fore.LIGHTGREEN_EX + "Всего доброго!".center(os.get_terminal_size().columns)))
                case 1:
                    show_all_contacts()
                case 2:
                    add_contact()
                case 3:
                    change_contact_information()
                case 4:
                    search_contact()
                case _:
                    print(Fore.LIGHTRED_EX + 'Необходимо ввести целое число от 0 до 4')


if __name__ == "__main__":
    os.system("clear||cls")
    telephone_book()
