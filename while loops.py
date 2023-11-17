# #  while 45
# total = 0
# 
# while total <= 49:
#     n = int(input('Enter a number '))
# 
#     total += n
#     print('The total is',total)
# 
# 
# 
# 
# # while 46
# num = 0
# while num < 5:
#       n = int(input('Enter a number '))
#       num = n
# 
# print (f'The last number you entered is {num}')
# 
# 
# 
# 
# # while 47
# n1 = int(input('Enter a number '))
# n2 = int(input('Enter another number '))
# nsum = n1 + n2
# yn = str(input('do you wanna add another number? (y or n) '))
# while yn == 'y':
#     n3 = int(input('Enter another number '))
#     nsum += n3
#     yn = str(input('do you wanna add another number? (y or n) '))
# print (nsum)
# 
# 
# 
# # while 48
# n = 0
# 
# p1 = input('Who do you wanna invite ')
# print(f'{p1} has been invited')
# n += 1
# 
# yn = input('do you want to invite somome else? ')
# 
# while yn == 'yes':
#     p1 = input('Who do you wanna invite ')
#     print(f'{p1} has been invited')
#     yn = input('do you want to invite somome else? ')
# 
# print(f'\nyou have invited {n} people')
# 
# 
# 
# # while 49
# compnum = 50
# a = 0
# n = int(input('Guess a number '))
# a += 1
# while n != 50:
#     if n > 50:
#         print('Too high')
#         n = int(input('Try again '))
#         a += 1
#     elif n < 50:
#         print('Too low')
#         n = int(input('Try again '))
#         a += 1
# 
# if n == 50:
#     print(f'Well done, you took {a} attempts')
# 
# 
# 
# # while 50
# import time
# n = int(input('Guess a number '))
# 
# while n < 10 or n > 20: 
#     while n > 20:
#         print('whoa thats too high')
#         time.sleep(0.50)
#         n = int(input('try again '))
#     while n < 10:
#         print('damn thats too low')
#         time.sleep(0.50)
#         n = int(input('try again '))
# 
# 
# 
# print('Thank you cuh')
# 
# 
# 
# # while 51
# bottles = 10
# 
# while bottles != 0:
#     print(f'\"There are {bottles} green bottles hanging on the wall, {bottles} green bottles hanging on the wall, and if 1 green bottle should accidentally fall\"')
#     bottles -= 1
#     que = int(input('how many green bottles will be hanging on the wall? '))
#     while que != bottles:
#         print("wrong try again")
#         que = int(input('how many green bottles will be hanging on the wall? '))
#             
# print('WOOOOOOOOOOOOOOOOHOOOOOOOOO')