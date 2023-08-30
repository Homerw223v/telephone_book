import os
from colorama import Fore
import constants

LEXICON = {'list_of_contacts': Fore.LIGHTYELLOW_EX + 'Список контактов:'.center(os.get_terminal_size().columns),
           'exit': Fore.MAGENTA + 'Exit',
           'next_page': Fore.MAGENTA + 'Next page',
           'input': Fore.CYAN + "####phone_book$$ ",
           'hello': Fore.GREEN + "Телефонный справочник".center(
               os.get_terminal_size().columns) + '\n\n' + Fore.LIGHTCYAN_EX + f"{constants.separator}\n"
                                                                              f"{constants.commands}\n"
                                                                              f"{constants.separator}\n\n",
           'feature': Fore.LIGHTGREEN_EX + 'Введите характеристики для поиска через пробел: ',
           'no_feature': Fore.LIGHTRED_EX + "Не предоставлено ни одной характеристики для поиска",
           'no_contact': 'К сожалению контакта, подходящего вашему описанию не найдено.',
           'goodbye': Fore.LIGHTGREEN_EX + "Всего доброго!".center(os.get_terminal_size().columns),
           'commands': ("---Чтобы вывести все контакты из справочник введите: 1\n"
                        "---Чтобы добавить новую запись в справочник введите: 2\n"
                        "---Чтобы отредактировать уже имеющуюся запись введите: 3\n"
                        "---Чтобы найти запись по характеристикам введите: 4\n"
                        "---Чтобы выйти из справочника введите: 0"),
           'wrong_input': Fore.LIGHTRED_EX + 'Неверные входные данные',
           'not_number': Fore.LIGHTRED_EX + 'Необходимо ввести целое число от 0 до 4',
           'not_yes_no': "Непонятный ввод. Попробуйте еще раз."}
