import re


if __name__ == '__main__':
    password = input("Введите пароль для анализа")
    strength = 0
    if len(password) < 8:
        strength = 0
        print('Длина пароля менее 8 символов.')
    elif len(password) >= 8:
        strength = 1
        print('Длина пароля равна или более 8-ми символов.')
    tmp_str = ''
    for i, ch in enumerate(password):
        if ch != password[i - 1]:
            tmp_str += ch
    if len(tmp_str) >= 8:
        strength += 1
    if re.search(r'[A-ZА-Я]', password) and re.search(r'[a-zа-я]', password):
        print('В пароле есть и строчные и заглавные буквы.')
        strength += 2
    if re.search(r'[a-zA-Zа-яА-Я]', password) and re.search('[0-9]+', password):
        strength += 2
        print('В пароле есть и буквы и цифры.')
    if re.search(r'\W+', password) and re.search(r'[a-zA-Zа-яА-Я]', password):
        print("В пароле есть и буквы и специальные символы.")
        strength += 2
    if re.search(r'\W+', password) and re.search(r'[0-9]+', password):
        print('В пароле есть и цифры и специальные символы.')
        strength += 2
    print('Итоговая оценка сложности введенного пароля по 10-ти бальной шкале: %d' % strength)
