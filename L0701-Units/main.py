import math_plus
import io_module as IO

def main():
    IO.writeLn("=" * 50)
    IO.writeLn("  ДЕМОНСТРАЦИЯ РАБОТЫ МОДУЛЕЙ MathPlus и IO")
    IO.writeLn("=" * 50)

    # --- Демонстрация модуля IO ---
    IO.writeLn("\n[1] Демонстрация модуля ввода-вывода (IO):")
    name = IO.readStr("Введите ваше имя: ")
    age = IO.readInt("Введите ваш возраст: ")
    height = IO.readFloat("Введите ваш рост (в метрах): ")
    
    IO.write("Привет, ")
    IO.writeLn(f"{name}! Тебе {age} лет, и твой рост {height} м.")

    # --- Демонстрация базовых функций MathPlus ---
    IO.writeLn("\n[2] Демонстрация базовых функций MathPlus:")
    x, y = 15, 27
    IO.writeLn(f"Sum({x}, {y}) = {math_plus.Sum(x, y)}")
    
    a, b = 3, 4
    IO.writeLn(f"Pif({a}, {b}) (квадрат гипотенузы c^2) = {math_plus.Pif(a, b)}")
    
    num = -12345
    IO.writeLn(f"Digits({num}) (сумма цифр) = {math_plus.Digits(num)}")
    
    n1, n2 = 1, 100
    IO.writeLn(f"RND({n1}, {n2}) = {math_plus.RND(n1, n2)}")

    # --- Демонстрация функций для последовательностей ---
    IO.writeLn("\n[3] Демонстрация функций для последовательностей:")
    IO.writeLn("(Для теста введите числа через пробел, например: 2 4 5 10)")
    seq_str = IO.readStr("Введите последовательность целых чисел: ")
    
    try:
        M = [int(i) for i in seq_str.split()]
    except ValueError:
        IO.writeLn("Неверный формат. Используется тестовая последовательность: [2, 4, 5, 10]")
        M = [2, 4, 5, 10]

    IO.writeLn(f"Последовательность M: {M}")
    IO.writeLn(f"Summ(M) = {math_plus.Summ(M)}")
    IO.writeLn(f"Average(M) (среднее арифм.) = {math_plus.Average(M):.4f}")
    IO.writeLn(f"AverageG(M) (среднее гарм.) = {math_plus.AverageG(M):.4f}")

    # --- Табуляция 10 значений ---
    IO.writeLn("\n[4] Табуляция 10 значений функций Garm(n) и Fib(n):")
    # Формируем заголовок таблицы
    header = f"{'n':<5} | {'Garm(n) (Гарм. ряд)':<22} | {'Fib(n) (Фибоначчи)':<18}"
    IO.writeLn(header)
    IO.writeLn("-" * len(header))
    
    # Табулируем 10 значений (от 1 до 10)
    for n in range(1, 11):
        garm_val = math_plus.Garm(n)
        fib_val = math_plus.Fib(n)
        # Форматированный вывод строки таблицы
        row = f"{n:<5} | {garm_val:<22.6f} | {fib_val:<18}"
        IO.writeLn(row)
        
    IO.writeLn("=" * 50)
    IO.writeLn("Демонстрация завершена.")

if __name__ == "__main__":
    main()