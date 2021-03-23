testcases=int(input())
while(testcases!=0):
    counting=['0']
    string=input()
    j=0
    for i in string:
        if i==counting[j]:
            continue
        else:
            counting.append(i)
            j+=1
    print(counting.count("1"))


