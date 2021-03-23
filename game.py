t=int(input())
while(t):
    n,a,b=list(map(int,input().split()))
    l=[int(i) for i in input().split()]
    i=0
    j=0
    A_=0
    B_=0
    while(i<n):
        if l[i]%a==0:
            A_+=1
        if l[j]%b==0:
            B_+=1
        i+=1
        j+=1
    if A_<=B_:
        print("Tokyo")
    else:
        print("Rio")

        



    t-=1