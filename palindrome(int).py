from unittest import result


num1 = 1221

num2 = 1232

#solution1
def pal1(x):
    return str(x)==str(x)[::-1]

#solution2

def pal2(x):
    num = x
    if x<0:
        return False
    result = 0    
    while num>0:
        result = result*10 + num%10
        num = num//10
        

    return result == x


print(pal1(num1))
print(pal2(num1))





