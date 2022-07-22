# четные символы - справа, нечетные - слева. Поторить n раз. Запара с оптимизацией

def jumbled_string(s, n):
    s = list(s)
    start = s
    pov = 1

    for i in range(n):
        if start == s and i != 0:
            pov = i
            break
        s = s[::2] + s[1::2]

    for i in range(n % pov):
        s = s[::2] + s[1::2]

    return "".join(s)
