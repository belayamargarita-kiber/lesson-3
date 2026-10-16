from calculator_modules.arithmetic import add, subtract, multiply, divide

def main():
    print("Добро пожаловать в калькулятор!")
    
    while True:
        operation = input("Введите операцию (сложение, вычитание, умножение, деление) или 'выход' для завершения: ").strip().lower()
        
        if operation == 'выход':
            print("До свидания")
            break
            
        if operation in ["сложение", "вычитание", "умножение", "деление"]:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            
            if operation == "сложение":
                result = add(a, b)
            elif operation == "вычитание":
                result = subtract(a, b)
            elif operation == "умножение":
                result = multiply(a, b)
            elif operation == "деление":
                result = divide(a, b)
                
            print(f"Результат: {result}\n")
        else:
            print("Неизвестная операция. Попробуйте еще раз\n")

if __name__ == "__main__":
    main()