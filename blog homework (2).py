_sum=0
count=0
while True:
    a=int(input('enter a number:'))
    if a>77:
        _sum=a
        count+=1
        print(_sum,count)
    elif a==0:
        break
