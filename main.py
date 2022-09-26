import math


def num_2():
    print("\n#2")
    N = 20
    sZnam = 0
    sItog = 0
    for x in range(1, N):
        sZnam += math.sin(x)
        sItog += 1 / sZnam
    print(sItog)


def num_3():
    print("\n#3")
    N = 20
    p = 1
    for x in range(1, N):
        p *= 2 * x / (2 * x + 1)
    print(p)


def num_4():
    print("\n#4")
    N = 10
    for x in range(N, N * 2):
        if x + 2 <= N * 2:
            print("1:", x, ", 2:", (x + 2))


def num_5():
    print("\n#5")
    n = 0
    k = 500
    prov = 0
    for i in range(1, k):
        buff = i
        while buff != 0:
            n += 1
            buff //= 10
        buff = i
        while buff != 0:
            prov += math.pow(buff % 10, n)
            buff //= 10
        if i == prov:
            print(i)
        prov = 0
        n = 0


num_2()
num_3()
num_4()
num_5()
