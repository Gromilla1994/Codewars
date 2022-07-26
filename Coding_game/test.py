import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

a -= b
for i in range(c):
    a = a-d-i

print(a)
