import math
 
#1
def un(sent):
    new_sent = 'un'+sent
    return new_sent

print(un(input('#1\nenter a word: ')))
 
#2
def s(sent):
    new_sent = sent + 's'
    return new_sent

print(s(input('#2\nenter a word: ')))
 
#3

def circle_area(d):
    r = d/2
    area = math.pi*(r**2)
    return '%.2f' %area

circle_area_result = (circle_area(float(input('#3\nenter your diameter: '))))
print(f'area = {circle_area_result}')
 
#4

def rectangle_area(h,w):
    return h*w
 
rectangle_area_result = rectangle_area(float(input('#4\nenter height of rectangle ')),float(input('enter width of rectangle ')))
print( f'area = {rectangle_area_result}')
 
#5

#uses #3 and #4
 
def perimiter_of_circle(r):
    return 2*maths.pi*r

def perimiter_of_rectangle(h,w):
    return 2*h + 2*w

choice = int(input('''#5
1. Area of Circle
2. Perimeter of circle
3. Area of rectangle
4. Perimeter of rectangle
    choose a menu number: '''))
 
if choice == 1:
    print(f'area of circle is',circle_area(float(input('enter your diameter: '))))
elif choice == 2:
    print(f'perimiter of circle is',circle_area(float(input('enter your radius: '))))
elif choice == 3:
    print(f'area of rectangle is',rectangle_area(float(input('enter height of rectangle ')),float(input('enter width of rectangle '))))
elif choice == 4:
    print(f'perimiter of rectangle is',perimiter_of_rectangle(float(input('enter height of rectangle ')),float(input('enter width of rectangle '))))
 
