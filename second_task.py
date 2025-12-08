n = -1
while n < 2:
    try:
        n = int(input("Введите количество чисел Фибоначчи: "))
    except ValueError:
        print("Некорректное число, введите заново")
    if n < 2:
        print("Некорректное число, введите заново")
fib = [1, 1]
for i in range(0, n-2):
    fib.append(fib[i] + fib[i + 1])

print("Первые", n, "чисел Фибоначчи:")
print(fib)
