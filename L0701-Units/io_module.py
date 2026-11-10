def write(mess):
    """Выводит на консоль выражение mess без перевода строки."""
    print(mess, end='')

def writeLn(mess):
    """Выводит на консоль выражение mess с переводом курсора на новую строку."""
    print(mess)

def readStr(mess):
    """Ввод строки с консоли с комментарием mess."""
    return input(mess)

def readInt(mess):
    """Ввод целого числа с консоли с комментарием mess."""
    while True:
        try:
            return int(input(mess))
        except ValueError:
            print("Ошибка! Введите целое число.")

def readFloat(mess):
    """Ввод дробного числа с консоли с комментарием mess."""
    while True:
        try:
            # Заменяем запятую на точку для корректного парсинга в Python
            val = input(mess).replace(',', '.')
            return float(val)
        except ValueError:
            print("Ошибка! Введите дробное число.")