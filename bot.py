#!/usr/bin/env python3

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def main():
    print("🤖 Факториал-бот запущен!")
    try:
        number = int(input("Введите число для вычисления факториала: "))
        if number < 0:
            print("❌ Факториал отрицательного числа не существует")
        else:
            result = calculate_factorial(number)
            print(f"✅ Факториал числа {number} равен: {result}")
    except ValueError:
        print("❌ Пожалуйста, введите целое число")

if __name__ == "__main__":
    main()