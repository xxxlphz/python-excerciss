#getting colours
import colorama
from colorama import Fore, Back, Style
#making list
l = [int(input('enter number to add to list ')) for x in range(int(input('how many numbers do you want to add to the list??? ')))]
 
 
#bubble sort
for x in range(len(l)-1):
    print(f'\nPass {x+1}')
    for i in range(len(l)-1):
        #if a swap is needed
        if l[i]>l[i+1]:

            billy = l[i]
 
            l[i] = l[i+1]
 
            l[i+1] = billy
            #creating a list that will be printed to the user with colours indicating the swap
            n = [j for j in l]
            n[i] = Fore.GREEN + f'{l[i]}' + Style.RESET_ALL
            n[i+1] = Fore.GREEN + f'{l[i+1]}' + Style.RESET_ALL
        # if a swap is not needed
        else:
            n = [j for j in l]
            n[i] = Fore.RED + f'{l[i]}' + Style.RESET_ALL
            n[i+1] = Fore.RED + f'{l[i+1]}' + Style.RESET_ALL
        print(*n)
