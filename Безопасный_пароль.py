from random import choice, sample

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

def installation():
    num_pass = int(input('Введите количество паролей для генерации: '))
    lenn = int(input('Насколько длинный пароль вам нужен? '))
    digit = input('Должен ли включать цифры 0123456789? (да/нет) ').strip().lower()
    upper_letters = input('Должен ли включать прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет) ').strip().lower()
    lower_letters = input('Должен ли включать строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет) ').strip().lower()
    any_chars = input('Должен ли включать символы !#$%&*+-=?@^_? (да/нет) ').strip().lower()
    exclusion = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет) ').strip().lower()

    chars = ''

    if digit == 'да':
        chars += digits
    if upper_letters == "да":
        chars += uppercase_letters
    if lower_letters == "да":
        chars += lowercase_letters
    if any_chars == 'да':
        chars += punctuation

    if exclusion == 'да':
        for ch in 'il1Lo0O':
            chars = chars.replace(ch, '')

    if len(chars) == 0:
        print("Ошибка: Не выбрано ни одного типа символов для генерации пароля.")
        return

    def generate_password():
        for i in range(num_pass):
            password = ''.join(sample(chars, lenn))
            print(password)

    generate_password()

installation()
