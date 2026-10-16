while True:
    operation = input("Введите операцию (сложение, вычитание, умножение, деление) или 'выход' для завершения: ").strip().lower()
    
    if operation == 'выход':
        print("До свидания!")
        break
        
    if operation in ["сложение", "вычитание", "умножение", "деление"]:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        if operation == "сложение":
            result = a + b
        elif operation == "вычитание":
            result = a - b
        elif operation == "умножение":
            result = a * b
        elif operation == "деление":
            if b != 0:
                result = a / b
            else:
                result = "Ошибка: деление на ноль!"
                
        print(f"Результат: {result}\n")
    else:
        print("Неизвестная операция. Попробуйте еще раз.\n")