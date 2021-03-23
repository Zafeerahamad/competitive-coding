test_case=int(input())
while(test_case):
    n=int(input())
    A=list(map(int,input().split()))
    A.sort()
    chance=0
    i=0
    while(i<n):
        if A[i]<=i+1:
            A[i]+=1
            if chance==0:
                chance=1
            else:
                chance=0
        else:
            i+=1
    if chance==0:
        print("second")
    else:
        print("first")


    test_case-=1