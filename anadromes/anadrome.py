f = open('C:\\Users\\19AAbdallah.ACC\\Desktop\\New folder\\yurr.txt','r')
words = []
done = []
for x in f:
    if len(x) > 6:
        words.append(x.strip('\n'))

for x in words:
    y = x[::-1]
    if y in words and x not in done and y not in done and x != y:
        done.append(x)
        done.append(y)
        print(x,y)
