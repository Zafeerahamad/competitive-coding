testcase=int(input())
while (testcase):
    n=int(input())
    s=input()
    goal_A=0
    goal_B=0
    for i,el in enumerate(s):
        if i%2==0 and int(el)==1:
            goal_A=goal_A+1
        elif i%2!=0 and int(el)==1:
                goal_B+=1
        rest=n-(i+1)//2
        if rest+min(goal_A,goal_B)<max(goal_A,goal_B):
            break
        else:
            continue
    print(i+1)




            


    testcase-=1
