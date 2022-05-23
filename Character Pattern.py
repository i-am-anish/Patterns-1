## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while i<=n:
    j = 1
    strC = chr(ord('A')+i-1)
    while j<=i:
        chrP = chr(ord(strC)+j-1)
        print(chrP,end='')
        j+=1
    print('')
    i+=1    