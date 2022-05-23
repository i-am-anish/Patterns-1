## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = n
while i>=1:
    j = i
    strC = chr(ord('A')+i-1)
    chrP = chr(ord('A')-j+1)
    while j<=n:
        chrP = chr(ord('A')+j-1)
        print(chrP,end='')
        j+=1
    print('')
    i-=1    