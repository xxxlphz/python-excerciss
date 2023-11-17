# # if loops ex 12
# 
# num1 = int(input("choose a number: "))
# num2 = int(input("choose another number: "))
# 
# if num1 > num2:
#     print(num2, num1)
# 
# else:
#     print(num1,num2)
# 
# 
# 
# 
# # if loop ex 13
# num1 = int(input("Enter a number below 20 (or dont): "))
# 
# if num1 < 20:
#     print("Thank you")
# 
# else:
#     print("Too high")
# 
# 
# 
# 
# 
# # if loops ex 14
# num = int(input("Enter a number from 10 till 20: "))
# 
# if num>=10 and num<=20:
#     print("Thank you")
# 
# else:
#     print("Incorrect answer")
# 
# 
# 
# 
# # if loops ex 15
# color = input("What your favorite colour? ")
# 
# if color == "red" or color == "Red" or color == "RED":
#     print("I like red too.")
# 
# else:
#     print ("i dont like", color+", I prefer red")
# 
# 
# 
# 
# # if loops ex 16
# rain = input("is it raining? ")
# rain = rain.lower()
# 
# if rain == "yes":
#     wind = input("Is it also windy? ")
#     wind = wind.lower()
#     if wind == "yes":
#         print("\nits too windy for an umbrella just stay inside.")
#     else:
#         print ("\ntake an umbrellla with you.")
# 
# else:
#     sunny = input("is it sunny then? ")
#     sunny = sunny.lower()
#     if sunny == "yes":
#         v_sunny = input("is it REALLY sunny?? ")
#         v_sunny = v_sunny.lower()
#         if v_sunny == "yes":
#             print("\nstay inside or you'll melt.")
#         else:
#             print("\n all good go out and chill lil bro")
# 
#     else:
#         print("\nhave a nice day.")
# 
# 
# 
# 
# # if loops ex 17
# age = int(input("What is your age? "))
# if age >= 18:
#     print("you can vote!")
#     
# elif age == 17:
#     print("you can drive")
#     
# elif age == 16:
#     print("you can buy a lottery ticket")
#     
# elif age < 16 and age>2:
#     print("you can go trick or treating xD ")
# 
# elif age <3:
#     print("cap.")
# 
# 
# 
# 
# # if loops ex 18
# 
# def func():
#     num = int(input("Enter a number: "))
# 
#     if num < 10:
#         print("\nToo low\n")
# 
#         print("Try again:")
# 
#         func()
# 
#     elif num <= 20 and num >= 10:
#         print("\nCorrect")
# 
#     else:
#         print("\nToo high\n")
# 
#         print("Try again:")
# 
#         func()
# 
# func()
# 
# 
# 
# 
# # if loops ex 19
# num = int(input("Choose either 1, 2 or 3: "))
# 
# if num == 1:
#     print("Thank you")
# 
# elif num == 2:
#     print("Well done")
# 
# elif num == 3:
#     print("Correct")
# 
# else:
#     print("Error message") 