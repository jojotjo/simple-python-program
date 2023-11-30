# #Write a Python Program to check whether a given number is even or odd.
# #method 1 by using if and else loop
# num = int(input())
# if (num % 2 == 0):
#   print(" num is even number ", num)
# else:
#   print(" num is odd number ", num )

# #method 2 by using bitwise operator
# num = int(input(" enter the number: "))
# if num & 1:
#   print(" num is odd ", num )
# else:
#   print(" num is even ", num)

# #Python Program to check whether a number is positive or negative.
# check_num = int(input(" enter the number: "))
# if check_num < 0:
#   print(" num is negative ",check_num)
# else:
#   print(" num is positive ",check_num)

# #Python Program to check whether a given number is a palindrome.
# num = int(input())
# temp = num
# rev = 0
# while (num > 0):
#   dig = num % 10
#   rev = rev*10 + dig
#   num = num // 10
# if (temp == rev):
#   print(" the number is a palidrome! ")
# else:
#   print(" the number isn't a palidrome! ")
