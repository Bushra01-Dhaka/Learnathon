def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
          print("YES")
        else:
          print("NO")
    else:
        if (x2 - x1) % (v1 - v2) == 0  and (x2 - x1) / (v1 - v2) >=0:
            print("YES")
        else:
            print("NO")

jump = list(map(int, input().split()))

x1, v1, x2, v2 = jump[0], jump[1], jump[2], jump[3]
kangaroo(x1, v1, x2, v2)
