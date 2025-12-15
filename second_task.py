n = -1
while n < 0:
    try:
        n = int(input("Введите количество чисел Фибоначчи: "))
    except ValueError:
        print("Некорректное значение")
    if n < 2:
        print("Некорректное значение")
fib = [1, 1]
for i in range(0, n):
    fib.append(fib[i] + fib[i + 1])

print("Первые", n, "чисел Фибоначчи:")
print(fib[:n])
