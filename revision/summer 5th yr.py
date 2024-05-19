# #q1
# list = [int(input(f'enter {5-x} more number(s): ')) for x in range(5)]
# print(*list)
# newlist = [x+1 for x in list]
# print(*newlist)
# check = 0
# for x in range(len(list)):
#     if list[x]+1 == newlist[x]:
#         check += 1
# if check == 5:
#     print('yes')

# #q2
# hours = [12,7,9,9,6,8,2]
# total = 0
# for x in range(7):
#     for x in hours:
#         total += (1.35*0.5)
# print('%.2f' %total)

# #q3
# days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
# tot = []
# ttl = 0
# for x in range(7):
#     r = float(input(f'enter the rainfall for {days[x]} in cm: '))
#     tot.append(r)
#     ttl += r
# print(f'\ntotal rainfall: {ttl}cm cubed \naverage rainfall: %.1f cm \n' %(ttl/7))
# for x in range(7):
#     if x > 3.5:
#         print('rainfall exceeded 3.5cm on',days[x],f'by {tot[x]-3.5}cm')

# #q4
# names = []
# value = []
#   
# while True:
#      opt = (input('''*** Welcome ***
#  Please choose an option below:
#  1. Enter sales data
#  2. View total sales to date
#  3. View maximum sale value of any staff member
#  4. View minimum sale of any staff member
#  5. View average sale value of any staff member
#  
#      '''))
#      
#      if opt == '1':
#          names.append(input('enter the name of the sales person: '))
#          value.append(int(input('enter the value of their sale: ')))
#      elif opt == '2':
#          totsales = 0
#          for x in value:
#              totsales += x
#          print(f'value of total sales made to date: {totsales}')
#      elif opt == '3':
#          valofname = []
#          values = []
#          while 1:
#              currentname = input('enter name of salesperson: ')
#              if currentname in names:
#                  break
#              else:
#                  print('inavlid name try again')
#          for x in range(len(names)):
#              if names[x] == currentname:
#                  values.append(value[x])
#          max = 0
#          for x in values:
#              if x > max:
#                  max = x
#          print(f'{currentname}\'s largest sale value to date is {max}')
#      
#      elif opt == '4':
#          valofname = []
#          values = []
#          while 1:
#              currentname = input('enter name of salesperson: ')
#              if currentname in names:
#                  break
#              else:
#                  print('inavlid name try again')
#          for x in range(len(names)):
#              if names[x] == currentname:
#                  values.append(value[x])
#          min = values[0]
#          for x in values:
#              if x < min:
#                  min = x
#          
#          print(f'{currentname}\'s smallest sale value to date is {min}')
#      
#      elif opt == '5':
#          valofname = []
#          values = []
#          while 1:
#              currentname = input('enter name of salesperson: ')
#              if currentname in names:
#                  break
#              else:
#                  print('inavlid name try again')
#          for x in range(len(names)):
#              if names[x] == currentname:
#                  values.append(value[x])
#          total = 0
#          for x in values:
#              total += x
#              
#          avg = total/len(values)
#          print(f'{currentname}\'s average sale value {avg}')
#      else:
#          print('invalid,try again')
#      print('\n')
