def orgate(a,b):
    if a  == 0 and b == 0:
        return 0
    else:
        return 1
 
def andgate(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0
 
def notgate(a):
    if a == 1:
        return 0
    else:
        return 1
def xorgate(a,b):
    if a == b:
        return 0
    else:
        return 1
 
def nandgate(a,b):
    return notgate(andgate(a,b))
 
def norgate(a,b):
    return notgate(orgate(a,b))
 
def xnorgate(a,b):
    return notgate(xorgate(a,b))

def halfadder(a,b):
    a = int(a)
    b = int(b)
    s = xorgate(a,b)
    c = andgate(a,b)
    list = [str(s),str(c)]
    return list

def fulladder(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    s = xorgate(c,xorgate(a,b))
    c = orgate(andgate(c,xorgate(a,b)),andgate(a,b))
    list = [str(s),str(c)]
    return list

thea = str(input('enter two 8-bit numbers:\n'))
theb = str(input(''))
thea = thea[::-1]
theb = theb[::-1]
ans = ''
l = halfadder(thea[0],theb[0])
ans += l[0]
c = l[1]

for x in range(7):
    x +=1
    l = fulladder(thea[x],theb[x],c)
    ans += l[0]
    c = l[1]
ans = ans[::-1]


if len(thea) != 8 or len(theb) != 8:
    print('number(s) out of range')
elif c == '0':
    print(ans)
else:
    print('overflow error !!!!!!!!!!!!!!!')
