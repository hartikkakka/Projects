import datetime
import math
import calendar

# https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 3
# current = datetime.datetime.utcnow()
# print(current)

# 4
# def area_of_circle(r):
#     area = math.pi * (r**r)
#     return print(f"area of circle is {area} ")
#
#
# radius = float(input("enter the radius of circle : "))
# area_of_circle(radius)

# 5
# user_first_name = input("enter your first name: ").title()
# user_last_name = input("enter your last name : ").title()
#
# print(user_last_name, user_first_name)

# 6
# numbers = input("enter your number : ").split(",")
# print(list(numbers))

# 7
# file_name = input("enter the file name with extension:").split(".")
# print(file_name[-1])

# 8
# color_list = ["Red", "Green", "White", "Black"]
# print(color_list[0], color_list[-1])
#
# # 9
# exam_st_date = (11, 12, 2014)
# print("examination starts from : %i/%i/%i" % exam_st_date)

#  10
# n = int(input("enter you nth value :"))
# n3 = int(f"{n}{n}{n}")
# n2 = int(f"{n}{n}")
# print(n + n3 + n2)

# 12
# month = int(input("entre the month: "))
# year = int(input("entre the year: "))
# print(calendar.month(year, month))

# 14
# first_dates = datetime.date(2014, 7, 2)
# second_date = datetime.date(2014, 7, 11)
# print(second_date-first_dates)

# 15
# def volume_of_sphere(r):
#     volume = (4 / 3) * math.pi * (r ** r * r)
#     return print(f"volume of sphere is {volume} ")
#
#
# volume_of_sphere(6)

# 16
# number = int(input("enter your number: "))
# if number > 17:
#     x = number - 17
#     print(x * 2)
# else:
#     print(17 - number)

# 17
# def number_within(number):
#     if number < 100:
#         print(f"{number} is small than 100")
#     elif 101 < number < 1000:
#         print(f"{number} is bigger than 101 but smaller than 1000")
#     elif 1001 < number < 2000:
#         print(f"{number} is bigger than 1001 but smaller than 2000")
#
#
# number_within(999)

# 18
# def sum_and_multiple_of_number(n1, n2, n3):
#     if n1 == n2 == n3 == n1:
#         print((n1+n2+n3) * 3)
#     else:
#         print(n1+n2+n3)
#
#
# sum_and_multiple_of_number(88, 88, 88)

# 19
# def new_sting(text):
#     if len(text) >= 2 and text[:2] == "is":
#         return print(text)
#     return print("is " + text)
#
#
# new_sting("your dog okay ?")

# 20
# def copy_string(text, n):
#     return print(text * n)
#
#
# copy_string("copt ", 6)

# 21
# def odd_or_even(n):
#     if n % 2 == 0:
#         print(f"{n} is an even number")
#     else:
#         print(f"{n} is an odd number")
#
#
# number = int(input("enter your number: "))
# odd_or_even(number)


# 22
# num4 = [4, 5, 6, 4, 7, 4]
# x = num4.count(4)
# print(x)

# 23
# def first_2_string(n):
#     x = "how is your dog?"
#     if len(x) > 2:
#         print(x[:2] * n)
#     else:
#         print(x)
#
# first_2_string(2)


# 24

