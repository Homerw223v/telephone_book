import os
from pathlib import Path
import sys

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
    last_name: str = input('Введите фамилию: ').capitalize()
    first_name: str = input('Введите имя: ')
    middle_name: str = input('Введите отчество: ')
    organization: str = input('Введите название организации: ')
    phone_number_work: str = input('Введите рабочий номер телефона: ')
    phone_number_personal: str = input('Введите личный номер телефона: ')
    line: str = f"{last_name} {first_name} {middle_name} {organization} {phone_number_work} {phone_number_personal}\n"
    return line


def show_all_contacts() -> None:
    """
    Function to display all available contacts
    :return: None
    """
    with open('telephone_book.txt', mode='r', encoding='utf-8') as file:
        os.system("clear||cls")
        number: int = 1
        contacts = file.readlines()
        pages = len(contacts) // 8 if len(contacts) % 8 == 0 else (len(contacts) // 8) + 1
        print('Список контактов:'.center(os.get_terminal_size().columns))
        for line in contacts:
            print(f"{number}: {line.strip()}")
            if number % 8 == 0 and (number // 8) < pages:
                print(f"Страница {(number // 8)} из {pages}".center(os.get_terminal_size().columns))
                input('Next page')
                os.system("clear||cls")
                print('Список контактов:'.center(os.get_terminal_size().columns))

            elif number % 8 == 0 and (number // 8) == pages:
                print(f"Страница {pages} из {pages}".center(os.get_terminal_size().columns))
                input('Exit')
            elif number % 8 != 0 and (number // 8) + 1 == pages and line == contacts[-1]:
                print(f"Страница {pages} из {pages}".center(os.get_terminal_size().columns))
                input('Exit')
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
    print(separator)
    telephone_book()


def search_contact() -> None:
    """
    Function to search for an existing contact
    :return: None
    """
    os.system("clear||cls")
    while True:
        pattern: list = input('Введите характеристики для поиска через пробел: ').split()
        if not pattern:
            os.system("clear||cls")
            print("Не предоставлено ни одной характеристики для поиска")
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
    print(separator)
    telephone_book()


def change_contact_information() -> None:
    """
    Function to change an existing contact
    :return: None
    """
    os.system("clear||cls")
    while True:
        pattern: list = input('Введите характеристики для поиска через пробел: ').split()
        if not pattern:
            os.system("clear||cls")
            print("Не предоставлено ни одной характеристики для поиска")
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
    print(separator)
    telephone_book()


def telephone_book():
    """
    A function to process user input and send it to the appropriate function
    :return: None
    """
    print(f"{separator}\n{commands}\n{separator}\n\n")
    while True:
        try:
            action: int = int(input("####phone_book$$ "))
            print()
        except ValueError:
            print('Неверные входные данные')
        else:
            match action:
                case 0:
                    sys.exit(print("Всего доброго!".center(os.get_terminal_size().columns)))
                case 1:
                    show_all_contacts()
                case 2:
                    add_contact()
                case 3:
                    change_contact_information()
                case 4:
                    search_contact()
                case _:
                    print('Неверные входные данные.')


if __name__ == "__main__":
    os.system("clear||cls")
    print("Добро пожаловать в телефонный справочник.".center(os.get_terminal_size().columns), end='\n\n')
    telephone_book()
