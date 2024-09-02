#getting colours
import colorama
from colorama import Fore, Back, Style

#making list
#l = [int(input('enter number to add to list ')) for x in range(int(input('how many numbers do you want to add to the list??? ')))]
l = [x for x in input('enter the numbers you want to add to the list with a space in between : ').split()]

for x in l:
    if x.isdigit() == False:
        l[l.index(x)] = input(f'{x} is not a number, enter a number: ')

comparison_count = 0
swap_count = 0

print(f'\noriginal list: {l}')
#bubble sort
for x in range(len(l)-1):
    print(f'\nPass {x+1}')
    for i in range(len(l)-1):
        
        comparison_count += 1
        
        #if a swap is needed
        if l[i]>l[i+1]:
            
            swap_count += 1
            #swapping around the variable values
            billy = l[i]
            l[i] = l[i+1]
            l[i+1] = billy
            #creating list that will be printed out to the user with colours indicating a swap
            n = [j for j in l]
            n[i] = Fore.GREEN + f'{l[i]}' + Style.RESET_ALL
            n[i+1] = Fore.GREEN + f'{l[i+1]}' + Style.RESET_ALL
        
        #if swap is not needed
        else:
            n = [j for j in l]
            n[i] = Fore.RED + f'{l[i]}' + Style.RESET_ALL
            n[i+1] = Fore.RED + f'{l[i+1]}' + Style.RESET_ALL
        print(*n)

print(f'\nsorted list: {l}')
print(f'{comparison_count} comparisons were made and {swap_count} swaps\nNote: green indicates the two items were swapped, red means they were compared but not swapped')

# Features of universal design used:
#     1. Tolerance for error :
#     the for loop at lines 10 - 12 allow the user to fix any mistakes 
#     made in case they incorrectly entered an alphabetic chracter
#     
#     2.Perciptable information
#     the colours showing the elements being compared and swapped (or not swapped),
#     each phase being printed as well as the orignal and sorted list being printed
#     makes it easy for the user to follow the sorting process as it happens in a simple
#     and understandable way
