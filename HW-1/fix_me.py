"""
Программа для расчета среднего арифметического
Версия 1.0
Автор: Павел
"""

def calculate_average(num):
    """
    Рассчитывает среднее значение списка чисел
    numbers(list): Список чисел
    """
    total = sum(num) # Суммируем все числа в списке
    count = len(num) # Находим длину списка
    average = total / count # Рассчитываем среднее значение
    return average # Возвращает среднее значение

# Использование функции
numbers = [10, 15, 20]
result = calculate_average(numbers)
print("The average is:", result)
