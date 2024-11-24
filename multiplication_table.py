#
# def multiplication_table(number):
#     for i in range(1,11):
#         print(f"{number} X {i} = {number * i}")
#
# number = int(input("Enter the number to get it's multiplication table: "))
# multiplication_table(number)


#*********** CODECHEFF problem about Array ************************

# 1 no problem
# two_value = list(map(int, input().split()))
# array_len = two_value[0]
# search_value = two_value[1]
#
# print("Array Length: " + str(array_len) + " Search Element: " + str(search_value))
#
# array = list(map(int, input("Insert Array Element: ").split()))
#
# element_present = False
#
# for i in array:
#     if i == search_value:
#         element_present = True
#
# if element_present:
#     print("YES")
# else:
#     print("NO")


# 2 no: Find maximum in an Array

test_case = int(input("Number of Test Case: "))
all_test_case_max_value = []
max_value_of_allCase = 0

for test in range(test_case):
    array_len = int(input("Array Length: "))
    array = list(map(int, input("Insert value of the array: ").split()))
    max_value = array[0]

    for i in array:
        if i > max_value:
            max_value = i
    all_test_case_max_value.append(max_value)


print("All Max value: ", str(all_test_case_max_value))

max_value_of_allCase = max(all_test_case_max_value)
print("The maximum value: ", max_value_of_allCase)





