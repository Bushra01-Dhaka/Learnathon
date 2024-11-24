#*********************************** Coupon Code Problem: Take discount or Not ***********************

t = int(input("No of Test: "))
normal_sum = 0
with_discount_sum = 0
after_discount_a = []

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    for i in a:
        normal_sum += i
    print("Without Using Coupon: " + str(normal_sum))

    for i in a:
        if i <= y:
            i = 0
            after_discount_a.append(i)
        elif i > y and x > 0 :
            after_discount_a.append(i - y)
        else:
            after_discount_a.append(i)

    print("New Cost of Product after taking Coupon: " + str(after_discount_a))

    # for i in after_discount_a:
    #     with_discount_sum += i

    with_discount_sum = sum(after_discount_a)
    print("With Discount sum: " + str(with_discount_sum))

    print("Coupon: " + str(x))
    with_adding_coupon_prize_total = with_discount_sum + x
    print("Using Coupon: " + str(with_adding_coupon_prize_total))

    if with_adding_coupon_prize_total >= normal_sum:
        print("NO COUPON")
    else:
        print("COUPON")

    # Reset variables for the next test case
    normal_sum = 0
    with_discount_sum = 0
    after_discount_a.clear()



