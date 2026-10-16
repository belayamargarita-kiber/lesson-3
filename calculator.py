add_lambda = lambda x, y: x + y
subtract_lambda = lambda x, y: x - y
multiply_lambda = lambda x, y: x * y
divide_lambda = lambda x, y: x / y if y != 0 else "Ошибка. Деление на ноль"

while True:
    operation = input("Введите операцию (сложение, вычитание, умножение, деление) или 'выход' для завершения: ").strip().lower()
    if operation == 'выход':
        print ("До свидания")
        break

    if operation in ["сложение", "вычитание", "умножение", "деление"]:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        if operation == "сложение":
            result = add_lambda(a, b)
        elif operation == "вычитание":
            result = subtract_lambda(a, b)
        elif operation == "умножение":
            result = multiply_lambda(a, b)
        elif operation == "деление":
            result = divide_lambda(a, b)

        print(f"результат: {result}\n")
    else:
        print("Неизвестная операция. Попробуйте еще раз\n")