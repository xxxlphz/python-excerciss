def dtobin(decimal):
    decimal = int(decimal)
    string = ''
    while decimal > 0:
        if decimal%2 == 1:
            string = string + '1'
        elif decimal%2 == 0:
            string = string + '0'
        decimal = decimal//2
    string = string[::-1]
    return string

def btodec(binary):
    binary = str(binary)
    binary = binary[::-1]
    ttl = 0
    p = 0
    for x in binary:
        if x =='1':
            ttl+= (2**p)
        p+=1
    return ttl

def utf(string):
    result = ''
    for character in string:
        dec = ord(character)
        binary = dtobin(dec)
        if len(binary) <= 7:
            for x in range(7 - len(binary)):
                binary = '0' + binary
            result = result + '0' + binary
        elif len(binary) <= 11:
            while len(binary) != 11:
                binary = '0' + binary
            result += '110' + binary[:5] + '10' + binary[5:]
        elif len(binary) <= 16:
            while len(binary) != 16:
                binary = '0' + binary
            result += '1110' + binary[:4] + '10' + binary[4:10] + '10' + binary[10:]
        elif len(binary) <= 21:
            while len(binary) != 21:
                binary = '0' + binary
            result += '11110' + binary[:3] + '10' + binary[3:9] + '10' + binary[9:15] + '10' + binary[15:]
    
    return result

def string(utf):
    r = ''
    rn = []
    list = [utf[x:x+8] for x in range(0,len(utf),8)]
    for v in list:
        if v[0] == '0':
            r += chr(btodec(v[1:]))

#     if utf[0] == '0':
#         new = utf[1:]
#         result += btodec[new]
        
    return r

while 1:
    menu = int(input('''
What do you want to do!?!?!?

1) string to UTF
2) UTF to string
        '''))
    if menu == 1:
        print(utf(input('enter a string to change into utf: ')))
    elif menu == 2:
        print(string(input('enter utf to change into a string: ')))
