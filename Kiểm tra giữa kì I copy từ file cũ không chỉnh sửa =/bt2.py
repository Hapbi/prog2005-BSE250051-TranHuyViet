def kt(n):
    d=0
    for i in range(1,n+1):
        if n%i==0:
            d=d+1
    if d==2:
        return True
    else:
        return False
for i in range (111,16,-2):
    print(i,end=' ')
print(' ')
for i in range(17,112):
    if kt(i):
        print(i,end=' ')