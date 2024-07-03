# CAESEAR CYPHER
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#functions
def encode(prompt,key):
    ans = ''
    for x in prompt:
        x = x.lower
        if x == ' ':
            ans += ' '
        else:
            move = l.index(x) + key
            if move > 25:
                move -= 26
            ans += l[move]
    return ans

def decode(prompt,key):
    ans = ''
    for x in prompt:
        x = x.lower
        if x == ' ':
            ans += ' '
        else:
            move = l.index(x) - key
            if move < 0:
                move += 26
            ans += l[move]
    return ans

#body
typeshi = input('(d)ecode or (e)ncode? ')   
if typeshi == 'e':
    print(encode(input('enter sentence to code: '),int(input('enter key: '))))
elif typeshi == 'd':
    print(decode(input('enter sentence to decode: '),int(input('enter key: '))))

