i=1
f=int(input('enter num:'))
while i<=9:
    s=int(input('enter num:'))
    if s<f:
        print('not sorted')
        break
    f=s
    i+=1
    if i==9:
        print('sorted')
