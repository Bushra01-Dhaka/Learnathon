
t = int(input())

# h = Hidden word
#  g = Guess Word

while t > 0:

    h = input()
    g = input()
    length = len(h)
    output = []
    match_result = ""

    for i in range(length):
        hidden = h.upper()
        guess = g.upper()
        if hidden[i] == guess[i]:
            output.append("G")
        else:
            output.append("B")


    for item in output:
        match_result += item

    print(str(match_result))

    t -= 1