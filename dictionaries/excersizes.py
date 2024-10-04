# #tables excercise
# #ex 96-99
# table = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# row = int(input('choose a row (1-4): '))
# print(table[row-1])
# column = int(input('choose column in that row (1-3): '))
# print(table[row-1][column-1])
# if input('do you want to change the value of the number? (y/n) ').lower() == 'y':
#     table[row-1][column-1] = int(input('enter the new value: '))
#     print(table[row-1])
 
# #100-101
# ntable = {'John':{'N':3056,'S':8463,'E':8441,'W':2694},
#             'Tom':{'N':4832,'S':3586,'E':4737,'W':3612},
#             'Anne':{'N':5239,'S':6437,'E':7652,'W':8731},
#             'Fiona':{'N':2048,'S':1693,'E':9647,'W':4213}}
#  
# # name = input('enter a name: John, Tom, Anne, Fiona (case sensetive) ')
# # r = input('enter a region (N,S,E,W) ').upper()
# # print(ntable[name][r])
# 
# for k,v in ntable.items():
#     print(k,*v.items())
# 
# name = input('enter the person whos sales you want to change ')
# print('\n'+name, ntable[name],'\n')
# 
# r = input('enter the region you want to change (N,S,E,W) ').upper()
# ntable[name][r] = int(input('enter the new value: '))
# 
# print('\n'+name, ntable[name],'\n')

#102
table = {}
for x in range(4):
    name = input(f'enter the name of person number {x+1}: ')
    age = int(input('enter their age '))
    shoe = input('enter their shoe size ')
    table[name] = {'age':age,'shoe size': shoe}
    
for k,v in table.items():
    print(k,*v.items())
