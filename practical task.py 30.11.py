def generate_password(n):
    password = ""
    for i in range(1, n):  # Первая часть пары
        for j in range(i + 1, n + 1):  # Вторая часть пары
            pair_sum = i + j
            if n % pair_sum == 0:  # Проверяем кратность
                password += str(i) + str(j)
    return password
for n in range(3, 21):
    print(f"{n} - {generate_password(n)}")
