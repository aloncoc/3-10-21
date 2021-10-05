i=1
_sum=int(input('please enter a number:'))
while i<=9:
    x=int(input('enter number:'))
    if x==_sum:
        break
    _sum+=x
    i+=1
print('sum',_sum)
