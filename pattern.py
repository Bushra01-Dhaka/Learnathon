num = int(input("Enter the number: "))

# ************************************************************
# *
# * *
# * * *
# * * * *
# * * * * *

print()
print()

for i in range(1, num+1):
    for j in range(1, i+1):
        print("*", end=' ')
    print()

#************************************************************
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print()
print()

for i in range(1,num+1):
    for j in range(1, i+1):
        print(j,end =' ')
    print()

#*******************************************************************
print()
print()

for i in range(num+1, 0, -1):
    for j in range(i, 0, -1 ):
        print(j, end=' ')
    print()


# *********************************************************************
# * * * * *
# * * * *
# * * *
# * *
# *
print()
print()

for i in range(num+1, 1, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# ********************************************************
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

for i in range(num):
    print(' ' * (num-i-1) + '* ' * (i+1))


# *************************************************************
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
print()
print()

for i in range(num):
    print(' '*i + '* ' *(num-i))


# **********************************************************

print()
print()

for i in range(num):
    print(" " * (num-i-1) + '* ' *(i+1))
for i in range(num):
    print(" " * i + "* " *(num - i))