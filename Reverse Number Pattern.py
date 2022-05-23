## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while i<=n:
    j = 1
    for j in range(i,0,-1):
        print(j,end='')
    print('')
    i+=1    