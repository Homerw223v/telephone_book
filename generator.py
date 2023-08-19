from faker import Faker
from random import randint

fake = Faker(locale='ru_RU')


def create_random_person(random: int) -> str:
    """
    Function to create a random person
    :return: str
    """
    last_name: str = fake.last_name_male() if random == 0 else fake.last_name_female()
    first_name: str = fake.first_name_male() if random == 0 else fake.first_name_female()
    middle_name: str = fake.middle_name_male() if random == 0 else fake.middle_name_female()
    organization: str = f'ИП-{str(fake.company()).split()[-1].replace("»", "").replace("«", "")}'
    phone_number_work: str = str(fake.phone_number()).replace(' ', '')
    phone_number_personal: str = str(fake.phone_number()).replace(' ', '')
    line: str = f"{last_name} {first_name} {middle_name} {organization} {phone_number_work} {phone_number_personal}\n"
    return line


def add_contact(number: int) -> None:
    """
    Function to add a new contact to the phone book
    :return: None
    """
    for i in range(number):
        contact: str = create_random_person(randint(0, 2))
        with open('telephone_book.txt', 'a+', encoding='utf-8') as file:
            file.write(contact)


if __name__ == "__main__":
    try:
        count: int = int(input('Сколько нужно фейковых данных?: '))
        add_contact(count)
    except ValueError:
        print("Введите целое число")
