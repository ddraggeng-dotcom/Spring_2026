def check_palindrome():
    user_input = input("Введите слово для проверки: ")
    
    if not user_input:
        print("Вы ничего не ввели!")
        return
    
    # Приводим слово в единый вид (Каждый символ в строчный)
    clean = ''.join(c.lower() for c in user_input)
    
    if clean == clean[::-1]: #срез строки с шагом -1 (аналог Reverse)
        print(f'"{user_input}" - Слово палиндром! ')
    else:
        print(f'"{user_input}" - Слово не является палиндромом! ')
check_palindrome()