# #extra functions excercise 6
# def case(string):
#     upper = 0
#     lower = 0
#     space = 0
#     for x in range(len(string)):
#         newstring = ''
#         newstring = newstring + string[x]
#         if newstring == ' ':
#             space += 1
#         elif newstring.isupper():
#             upper += 1
#         elif newstring.islower:
#             lower += 1
#         
#     resp = (f'No. of Upper case characters: {upper} \nNo. of Lower case characters: {lower} (the number of spaces is {space} btw)')
#     return resp
#             
# print(case(str(input('write sumn '))))




# #extra functions excercise 7
# sample = [1,2,3,3,3,3,4,5]
# def distinct(list):
#     unique =  []
#     for x in list:
#         if x not in unique:
#             unique.append(x)
#     return unique
# 
# print(distinct(sample))




# #extra functions excercise 8
# def prime(num):
#     check = 0
#     for x in range(num-2):
#         x += 2
#         if num/x != num//x:
#             check += 1
#     
#     if check+2 == num or num==1:
#         ans = 'WOOOOO this number IS prime'
#     else:
#         ans = 'BOOHOO this number IS NOT prime'
#     return ans
#             
# print(prime(int(input('enter a number to check if its prime '))))



# #extra functions excercise 9
# sample = [1,2,3,4,5,6,7,8,9]
# 
# def evencheck(list):
#     even  = []
#     for x in list:
#        if x%2 == 0:
#            even.append(x)
#     return even
#         
# print(evencheck(sample))


























