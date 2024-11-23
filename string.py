# Reverse a String

string = str(input("Write a string: "))
reverse_string = ""
for char in string:
    reverse_string = char + reverse_string

print("Reverse String: " + str(reverse_string))

#################################################################

#Check the string is palindrome or not
if string.lower() == reverse_string.lower():
    print(string + " is a Palindrome")
else:
    print(string + " is not a Palindrome")

#########################################################################

# Check How many vowel and consonant the string have
vowelCount = 0
consonantCount = 0

for char in string.lower():
    if char in "aeiou":
        vowelCount = vowelCount + 1
    elif char.isalpha():
        consonantCount = consonantCount + 1


print("Total Vowel: " + str(vowelCount))
print("Total Consonant: " + str(consonantCount))

