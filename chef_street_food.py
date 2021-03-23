testcase=int(input())
while(testcase):
    n=int(input())
    people=[]
    prices=[]
    stores=[]
    for i in range(n):
        s,p,v=[int(i) for i in input().split()]
        people.append(p)
        stores.append(s)
        prices.append(v)
    maximum=0
    for i in range(n):
        if maximum<prices[i]*(people[i]//(stores[i]+1)):
            maximum=prices[i]*(people[i]//(stores[i]+1))
            print(maximum)
    print(maximum)




    testcase-=1