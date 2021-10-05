into=0
against=0
avoid=0
veto=0
i=1
while i<5:
    vot=int(input('enter into numbers:'))
    into+=vot
    vot2=int(input('enter against numbers:'))
    against+=vot2
    vot3=int(input('enter avoid numbers:'))
    avoid+=vot3
    vot4=int(input('enter veto numbers:'))
    veto+=1
    i+=1
    if vot4 > 0:
        print(veto)
        break
    if i<5 :
        continue
    print('the into voted are:',into,'the againsted voted are:',against,'the avoid number is',avoid)
