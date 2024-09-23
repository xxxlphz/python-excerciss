sent = input('enter a sentence literally any sentence to ever exist').lower()
words = sent.split()
print(words)
dic = {}
dic2 = {}
for x in sent:
    if x == ' ':
        pass
    elif x in dic2.keys():
        dic2[x] = dic2[x] + 1
    else:
        dic2[x] = 1
for x in words:
    if x in dic.keys():
        dic[x] = dic[x] + 1
    else:
        dic[x] = 1

choice = int(input('choose a number\n1) word frequency \n2) character frequency \n	'))
while choice != 1 and choice != 2:
    choice = int(input('choose one or two!!!! \n1) word frequency \n2) character frequency \n	'))
if choice == 1:
    print('\033[4mWORD -- COUNT\033[0m')
    for key,value in dic.items():
        print(f'{key} -- {value}')
if choice == 2:
    print('\033[4mCHARACTER -- COUNT\033[0m')
    for key,value in dic2.items():
        print(f'{key} -- {value}')
