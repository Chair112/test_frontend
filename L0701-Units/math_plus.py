import random

def Sum(X, Y):
    """Вычисляет сумму двух целых чисел."""
    return X + Y

def Pif(a, b):
    """Вычисляет квадрат гипотенузы: a^2 + b^2 = c^2."""
    return a**2 + b**2

def Garm(n):
    """Вычисляет сумму n слагаемых гармонического ряда: 1 + 1/2 + ... + 1/n."""
    if n <= 0:
        return 0
    return sum(1 / i for i in range(1, n + 1))

def Summ(M):
    """Сумма последовательности M целых чисел."""
    return sum(M)

def Average(M):
    """Среднее арифметическое последовательности M."""
    if not M:
        return 0
    return sum(M) / len(M)

def AverageG(M):
    """Среднее гармоническое последовательности M: n / (1/x1 + 1/x2 + ... + 1/xn)."""
    if not M:
        return 0
    # Исключаем нули, чтобы избежать деления на ноль
    inv_sum = sum(1 / x for x in M if x != 0)
    if inv_sum == 0:
        return 0
    return len(M) / inv_sum

def Digits(n):
    """Вычисляет сумму цифр целого числа n."""
    n = abs(int(n))
    return sum(int(digit) for digit in str(n))

def RND(N1, N2):
    """Создает псевдослучайное целое число из диапазона [N1; N2]."""
    return random.randint(N1, N2)

def Fib(n):
    """Вычисление n-го по счету числа Фибоначчи (F1=1, F2=1, F3=2...)."""
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b