c0 = int(input("Введіть початкове число: "))

if c0 > 1:
    steps = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 //= 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
        print(c0)
    print("Кроки =", steps)
else:
    print("Число має бути більшим за 1.")