# # lists 74
# list = ["green","blue","black","red","pink","purple","yellow","orange","marshmallow","white"]
# int1 = int(input("choose a number from 0 to 4: "))
# int2 = int(input("choose number from 5 to 9"))
# 
# print (*list[int1+1:int2])




# # lists 75
# list = [345, 234, 876, 900]
# 
# print (*list)
# 
# n = int(input("enter a three-digit number: "))
# 
# if (n) in (list):
#     print(list.index(n))




# # lists 76
# n1 = input("Name someone you wanna invite to a party: ")
# n2 = input("ANOTHER ONE (DJ KHALED!): ")
# n3 = input("A third person: ")
# 
# list = [n1, n2, n3 ]
# 
# ans = input("do you wanna invite someone else? " )
# 
# def func():
# 
# 
#     if ans == "yes" or "Yes":
#         n4 = input("whats their name: ")
#         ans2 = input("do you wanna invite another person? " )
#         list.append(n4)
#         if ans2 == "yes":
#             func()
# 
#         else:
#             print ( "\n\nyouve invited", len(list), "people to the party")
#             print("the people you invited are", *list)
# 
#     else:
#         print ( "\n\nyouve invited", len(list), "people to the party")
#         print("the people you invited are", *list)
# 
# func()




# # lists 77
# n1 = input("Name someone you wanna invite to a party: ")
# n2 = input("ANOTHER ONE (DJ KHALED!): ")
# n3 = input("A third person: ")
# list = [n1, n2, n3 ]
# 
# ans = input("do you wanna invite someone else? " )
# 
# def func():
# 
# 
#     if ans == "yes" or "Yes":
#         n4 = input("whats their name: ")
#         ans2 = input("do you wanna invite another person? " )
#         list.append(n4)
#         if ans2 == "yes":
#             func()
# 
#         else:
#             print ( "\n\nyouve invited", len(list), "people to the party")
#             print("the people you invited are", *list)
# 
#     else:
#         print ( "\n\nyouve invited", len(list), "people to the party")
#         print("the people you invited are", *list)
# 
# func()
