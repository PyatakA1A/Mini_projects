what_op = input("Что нужно сделать: шифровать или дешифровать? ").lower()
while what_op != "шифровать" and what_op != "дешифровать":
    what_op = input('Похоже, вы ввели что-то не то. Введите "шифровать" или "дешифровать": ').lower()

what_lang = input('Выберите язык: русский (ru) или английский (en): ').lower()
while what_lang != "ru" and what_lang != "en":
    what_lang = input('Похоже, вы ввели что-то не то. Введите "en" или "ru": ').lower()

what_step = input("Введите шаг сдвига: ")
while not what_step.isdigit():
    what_step = input('Проверьте, точно ли вы ввели число: ')

what_step = int(what_step)
text = input('Введите сообщение: ')

def program(op, language, step, text):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'   
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    result = ""

    for symbol in text:
        if language == "en":
            alph = 26
            lower_al = eng_lower_alphabet
            upper_al = eng_upper_alphabet
        elif language == 'ru':
            alph = 32
            lower_al = rus_lower_alphabet
            upper_al = rus_upper_alphabet   

        if symbol.isalpha():
            if symbol.islower():
                place = lower_al.index(symbol)
                if op == "дешифровать":
                    index = (place - step) % alph
                elif op == 'шифровать':
                    index = (place + step) % alph
                result += lower_al[index]
            elif symbol.isupper():
                place = upper_al.index(symbol)
                if op == "дешифровать":
                    index = (place - step) % alph
                elif op == 'шифровать':
                    index = (place + step) % alph
                result += upper_al[index]
        else:
            result += symbol

    return result

# Вывод результата
output_text = program(what_op, what_lang, what_step, text)
print("Результат:", output_text)
text = 'Hawnj pk swhg xabkna ukq nqj.'
for k in range(25):
    print(program(text))
            
                    
                


