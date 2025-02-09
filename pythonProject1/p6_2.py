ch1 = float(input("Введіть перше число: "))
ch2 = float(input("Введіть друге число: "))

try:
    result = ch1/ch2
    print(result)
except:
    print(f"Ви намагалались поділити {ch1} на {ch2} і отримали помилку!")
    if ch2 == 0:
        print("На 0 ділити не можна!")
else:
    print("Розрахунки завершено")
