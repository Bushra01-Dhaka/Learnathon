s = "silaS sevol aryamuH"

reverse_string = ""

for char in s:
    reverse_string = char + reverse_string

print("The reverse of given string is: " + reverse_string)


# Prime number or not

def is_prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** .5)+ 1):
        if n % i == 0:
            return False

    return True

num = int(input("Enter the number: "))
if is_prime_num(num):
    print(num, "is a Prime Number")
else:
    print(num, "isn't a Prime number")



# FizzBuzz Game

print("Welcome to FizzBuzz Game!!!!!")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)




# Loop
import math

# Input: Integer N
N = int(input("Insert the value: "))

# Initialize variable to track the maximum sum of a1 + a2
max_sum = 0

# Loop through potential divisors up to sqrt(N)
for a1 in range(1, int(math.sqrt(N)) + 1):
    if N % a1 == 0:  # If a1 is a divisor
        a2 = N // a1  # Calculate a2
        max_sum = max(max_sum, a1 + a2)  # Update the maximum sum

# Output the maximum sum
print(max_sum)