max = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        number = list(str(i * j))
        if number == list(reversed(number)):
            if i * j > max:
                max = i * j

print(max)