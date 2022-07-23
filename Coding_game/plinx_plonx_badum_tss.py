guitar = ["plinx", "plonx"]
drums = ["badum", "tss"]

g_count = 0
instrument = []

n = int(input())
for i in range(n):
    instrument.append(input())
for i in range(n):
    if instrument[i] == "guitar":
        print(guitar[g_count])
        g_count = (g_count + 1) % 2
    elif instrument[i] == "drums" and i+1 != n:
        print(drums[0])
    else:
        print(drums[1])
