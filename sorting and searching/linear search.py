#linear search
def linear_search(l,targ):
    if targ not in l:
        return 'target not in list'
    else:
        for i in range(len(l)):
            if l[i] == targ:
                return f'the index value of your target is {i}'

#entering list and target
print(linear_search([input('enter a value to add to list ') for x in range(int(input('how many items do you want to add to the list??? ')))],input('enter your search target ')))
