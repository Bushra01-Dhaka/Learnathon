t = int(input())

# n = number of days
# a = array of distance that alice ran
# b = array of distance that Bob ran

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    both_happy_count = 0

    for day in range(n):
        if a[day] > b[day]:
            # alice_per_distance = int(a[day] - b[day])
            if a[day]<= 2 * b[day] :
                both_happy_count += 1
        else:
            # bob_per_distance = int(b[day] - a[day])
            if b[day] <= 2 * a[day]:
                both_happy_count +=1

    print("Both Happy Count: ", str(both_happy_count))

