def program1(num1,num2,num3):
    if num1>num2 and num1>num3:
        resp = str(num1) +' is the greatest number'
    elif num2>num1 and num2>num3:
        resp = str(num2) +' is the greatest number'
    else:
        resp = str(num3) +' is the greatest number'
    return resp

def program2(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            resp = str(num1) +' is the greatest number'
        else:
            resp = str(num3) +' is the greatest number'
    else:
        if num2>num3:
            resp = str(num2) + ' is the greatest number'
        else:
            resp = str(num3) + ' is the greatest number'
    return resp

def program3(num1,num2,num3):
    max = num1
    if max<num2:
        max = num2
    if max<num3:
        max = num3
    resp = str(max) +' is the biggest number'
    return resp