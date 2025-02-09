ch1 = int(input("Введіть перше число: "))
ch2 = int(input("Введіть друге число: "))
ch3 = int(input("Введіть третє число: "))


def check(ch1, ch2, ch3):
    if ch1 % 5 == 0:
        if ch2 % 5 == 0:
            if ch3 % 5 == 0:
                sp = [ch1, ch2, ch3]
                sp.sort()
                print(sp)
            else:
                raise TypeError("Неправильне число! Третє число має ділитись на 5!")
        else:
            raise TypeError("Неправильне число! Друге число має ділитись на 5!")
    else:
        raise TypeError("Неправильне число! Перше число має ділитись на 5!")


try:
    check(ch1, ch2, ch3)
except TypeError:
    print("Введено некоректні числа!")
