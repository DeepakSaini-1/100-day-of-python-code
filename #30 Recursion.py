# If any function call itself is called recoursion

def fac(n):
    if(n<=1):
        return 1
    return n*fac(n-1)

print(fac(-5))

def fabonic(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    return fabonic(n-1)+fabonic(n-2)

print(fabonic(6))