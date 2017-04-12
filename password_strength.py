import re
import os


def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file_handler:
            return file_handler.read()


def get_password_strength(password):
    pass


if __name__ == '__main__':
    password = 'ЕННЛОтьюбьо!!ьжд'
    strength = 0
    if len(password) < 8:
        strength = 0
    elif len(password) >= 8:
        strength = 1
    tmp_str = ''
    for i, ch in enumerate(password):
        if ch != password[i - 1]:
            tmp_str += ch
    if len(tmp_str) >= 8:
        strength += 1
    if re.search(r'[A-ZА-Я]', password) and re.search(r'[a-zа-я]', password):
        print('есть и строчные и заглавные буквы')
        strength += 2
    if re.search(r'[a-zA-Zа-яА-Я]', password) and re.search('[0-9]+', password):
        strength += 2
        print('есть и буквы и цифры')
    if re.search(r'\W+', password) and re.search(r'[a-zA-Zа-яА-Я]', password):
        print("есть и буквы и спецсимволы")
        strength += 2
    if re.search(r'\W+', password) and re.search(r'[0-9]+', password):
        print('есть и цифры и спецсимволы')
        strength += 2
    print(strength)
    text = load_data(
        'https://github.com/danielmiessler/SecLists/blob/master/Passwords/10_million_password_list_top_100000.txt')
    print(len(text))
