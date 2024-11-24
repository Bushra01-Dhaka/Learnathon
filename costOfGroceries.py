

t = int(input("No of Test Cases: "))

# n = number of item
# x = min freshness
# a = array of nth items freshness
# b = array of nth items prices


while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Your code goes here
    matched_index_no = []
    cost_of_groceries = 0

    print("Freshness array: "+ str(a[0]) )

    for item in range(n):
        print("Item_index_no " + str(item))
        if a[item] >= x:
            matched_index_no.append(item)
            cost_of_groceries += b[item]
    print("Matched Items: " + str(matched_index_no))
    print("Total Cost of Groceries: " + str(cost_of_groceries))


    t -= 1
