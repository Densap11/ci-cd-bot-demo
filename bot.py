

def calculate_factorial(number):
    
    if number == 0:
        return 1
    return number * calculate_factorial(number - 1)

def get_user_input():
   
    while True:
        try:
            user_input = int(input("Введите число для вычисления факториала: "))
            if user_input < 0:
                print(" Факториал отрицательного числа не существует")
                continue
            return user_input
        except ValueError:
            print(" Пожалуйста, введите целое число")

def main():
    """Основная функция бота."""
    print("🤖 Факториал-бот запущен!")
    number = get_user_input()
    result = calculate_factorial(number)
    print(f"✅ Факториал числа {number} равен: {result}")

if __name__ == "__main__":
    main()