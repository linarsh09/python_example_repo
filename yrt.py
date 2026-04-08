def make_multiplier(n):
    # Внешняя функция принимает параметр n
    def multiplier(x):
        # Внутренняя функция запоминает n (замыкание)
        return x * n
    return multiplier # Возвращаем функцию, а не результат

# Создаем замыкания
times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10)) # Вывод: 30 (10 * 3)
print(times5(10)) # Вывод: 50 (10 * 5)