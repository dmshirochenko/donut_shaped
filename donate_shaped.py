import math
import time

A, B = 0, 0
z = [0] * 1760
b = [' '] * 1760

while True:
    for i in range(1760):
        b[i] = ' '

    for j in range(1760):
        z[j] = 0

    for j in range(0, 628, 7):  # 6.28 approximated as 628, loop increments by 0.07
        for i in range(0, 628, 2):  # loop increments by 0.02
            c = math.sin(i / 100)
            d = math.cos(j / 100)
            e = math.sin(A)
            f = math.sin(j / 100)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i / 100)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

            if 0 <= o < 1760 and 0 <= N < 12 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

    print("\x1b[H")
    for k in range(1760):
        print(b[k] if k % 80 else '\n', end='')
        A += 0.00004
        B += 0.00002
    time.sleep(0.03)
