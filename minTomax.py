

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    # Your code goes here
    smallest_value = a[0]
    count = 0

    for item in a:
        if item < smallest_value:
            smallest_value = item


    for item in a:
        if item == smallest_value:
            count += 1

    total_operation_needed_to_made_M_Max = int(n - count)
    print(str(total_operation_needed_to_made_M_Max))



    # value = int(n - smallest_value)
    # print(str(value))


    t -= 1
