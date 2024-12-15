def decorator_cache(cache_depth_max=100):
    # Для хранения значений функций в кэше
    # создаем словарь
    cache_dictionary  = {}  

    def decorator_self(function):
        def wrapper(*args, **kwargs):
            # определяем имя функции
            function_name = function.__name__
            # Ищем функцию в кэше (словаре)
            if function_name in cache_dictionary:
                # Для найденной функции ищем аргуменнты, с которыи вычислялась функция 
                if args in cache_dictionary[function_name]:
                     # возвращаем найденное значение
                    return cache_dictionary[function_name][args]

                # Значения функции для заданных агрументов не найдено
                # вычисляем значение значений кэша с заданными аргументами
                function_result = function(*args, **kwargs)

                # Проверяем есть ли место в кэши для данной функции
                if len(cache_dictionary[function_name]) >= cache_depth_max:
                    cache_dictionary[function_name].pop(next(iter(cache_dictionary[function_name])))

                # Добавляем вычисленное значение в кэш
                cache_dictionary[function_name][args] = function_result
                return function_result

            # Для функции кэша ещё нет, создаем его
            # вычисляем значение значений кэша с заданными аргументами
            function_result = function(*args, **kwargs)
            # Добавляем вычисленное значение в кэш
            cache_dictionary[function_name] = {args: function_result}
            return function_result

        return wrapper

    return decorator_self

@decorator_cache(5)
def square(x):
    print(f"вычисляем {x} в квадрате  ")
    return pow(x,2)

@decorator_cache(3)
def cube(x):
    print(f"вычисляем {x} в кубе ")
    return pow(x,3)

if __name__ == '__main__':
    # первоначальное вычисление функций
    # заполняем кэш
    print('\nПервоначальное вычисление функций\n')
    print('square(1): ', square(1))
    print('square(2): ', square(2))
    print('square(3): ', square(3))
    print('square(4): ', square(4))
    print('square(5): ', square(5))


    print()
    print('cube(1)', cube(1))
    print('cube(2)', cube(2))
    print('cube(3)', cube(3))
    print('cube(4)', cube(4))
    print('cube(5)', cube(5))
    
    # повторное вычисление функций
    # будет происходить считание с кэша
    # тех значений функций, которые сохранились
    print('\nПовторное вычисление функций')
    print('square(5): ', square(5))
    print('square(4): ', square(4))
    print('square(3): ', square(3))
    print('square(2): ', square(2))
    print('square(1): ', square(1))
    print("\n для функции square глубина кэша равна 5,  \n"
          " и все значения функции остались в кэши и не пересчитывались")

    print()
    print('cube(5)', cube(5))
    print('cube(4)', cube(4))
    print('cube(3)', cube(3))
    print('cube(2)', cube(2))
    print('cube(1)', cube(1))
    
    print("\n для функции cube глубина кэша равна 3,  \n"
          " в кэши сохранились значения для функций с аргументами 5,4,3, так как они вычислялись последними \n"
          " а значения для функций с аргументами 2,1 пересчитывались, \n так как кэш расчитан на хранение 3 значений для функции cube")
