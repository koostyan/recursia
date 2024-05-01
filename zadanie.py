def test(*args, **kargs):  #функция с произвольным числом параметров разного типа
    print(args)
    for x, y in kargs.items():
        print(x, y)


test(1, 2, 3, 'ответ', на='поставленное', задание='.')

print()

def fact(n):        #расчёт факториала
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(int(input('Введите число:'))))
