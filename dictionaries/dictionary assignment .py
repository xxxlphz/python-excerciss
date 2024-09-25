sent = input('enter a sentence literally any sentence to ever exist')
words = sent.split()

dic = {} # dictionary fro words
dic2 = {} # dictionary for letters

for x in sent: # adding to letters dictionary
    if x == ' ':
        pass
    elif x in dic2.keys():
        dic2[x] = dic2[x] + 1
    else:
        dic2[x] = 1

for x in words: # adding to word dictionary 
    if x.lower() in dic.keys():
        dic[x.lower()] = dic[x.lower()] + 1
    else:
        dic[x.lower()] = 1

choice = input('choose a number\n1) word frequency \n2) character frequency \n	')
while choice != '1' and choice != '2': #in case of an invalid input
    choice = input('choose one or two!!!! \n1) word frequency \n2) character frequency \n	')

if choice == '1': #printing word count
    print('\033[4mWORD -- COUNT\033[0m')
    for key,value in dic.items():
        print(f'{key} -- {value}')
if choice == '2': #printing character count
    print('\033[4mCHARACTER -- COUNT\033[0m')
    for key,value in dic2.items():
        print(f'{key} -- {value}')
