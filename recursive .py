#RECURSION
 
# def factorial(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# 
# print(factorial(int(input(''))))
 
#1
def sumoflist(l):
    if len(l) == 1:
                    
        return l[0]
    else:
        return l[0] + sumoflist(l[1:])

list = []
while 1:
    n = (input('enter a number to add to list(enter nothing to stop) '))
    if n == '':
        break
    else:
        list.append(int(n))
        
print(sumoflist(list))
 
#2
def factorialsum(n):
    if n <= 0:
        return 1
    else:
        return n + factorial(n-1)

print(factorial(int(input(''))))

#3
def has_digit(s):
    if s[0].isdigit() == True:
        return True
    else:
        if len(s) <= 1:
            return False
        else:
            return has_digit(s[1:])
print(has_digit(input('enter a string ')))
