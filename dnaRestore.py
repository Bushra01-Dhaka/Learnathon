t = int(input())

#  00 - A
#  01 -T
#  10 - C
#  11 - G

while t > 0:
    n = int(input())
    s = input()
    result = ""

    # code here
    for i in range(0, n, 2):
        pair = s[i: i+2]

        if pair == "00":
            result += "A"
        elif pair == "01":
            result += "T"
        elif pair == "10":
            result += "C"
        elif pair == "11":
            result += "G"

    print(result)

    t -= 1