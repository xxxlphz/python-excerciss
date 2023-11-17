# #  for loops 35
# n= input("whats your name? ")
# 
# for i in range(3):
#     print(n)



# #  for loops 36
# n= input("whats your name? ")
# num = int(input("choose a number "))
# for i in range(num):
#     print(n)



# #  for loops 37
# name = str(input("what your name"))
# 
# for i in name:
#     print(i)



# #  for loops 38
# name = str(input("what your name "))
# num = int(input("choose a number "))
# 
# for i in range(num):
#     for i in name:
#         print(i)
        



# #  for loops 39
# num = int(input("choose a number between 1 and 12 "))
# 
# for i in range(12):
#     print(num * i)



# #  for loops 40
# num = int(input("choose a number below 50 "))
# 
# for i in range(num):
#     print(num - i)



# #  for loops 41
# name = str(input("what your name "))
# num = int(input("choose a number "))
# 
# if num <= 10:
#     for i in range(num):
#         print(name)
# 
# else:
#     for i in range(3):
#         print("Too high")



# #  for loops 42
# ttl = int(0)
# 
# for i in range(5):
#     num = int(input("choose a number "))
#     inc = input("do you wanna include this  number? ")
#     if inc == "yes":
#         ttl += num
# 
# print(ttl)



# #  for loops 43
# dir = input("do you want to count up or down? ")
# 
# if dir == "up":
#     n = int(input("choose your final number "))
#     for i in range(n):
#         print(i+1)
# 
# elif dir == "down":
#     n = int(input("choose a number below 20 "))
#     for i in range(n):
#         print(n-i)
# else:
#     print("i dont understand")



# #  for loops 44
# n = int(input("how many people do you want to invite to a party? "))
# list = []
# 
# for i in range(n):
#     name = input('who do you want to invite? ')
#     list.append(name)
#     print(name,"has been invited.")
# 
# print("you invited",n,"people")
# print('the people you invited are',*list) 
