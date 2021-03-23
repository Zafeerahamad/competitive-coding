test_cases=int(input())
while(test_cases):
    activities,origin=[ik for ik in input().split()]
    laddus=0
    activities=int(activities)
    for i in range(activities):
            act=[j for j in input().split()]
            if len(act)==2:
                if act[0]=="CONTEST_WON":
                    rank=int(act[1])
                    if rank<20:
                        laddus+=300+20-rank
                    else:
                        laddus+=300
                elif act[0]=="BUG_FOUND":
                    severity=int(act[1])
                    laddus+=severity
            elif len(act)==1:
                if act[0]=="TOP_CONTRIBUTOR":
                    laddus+=300
                elif act[0]=="CONTEST_HOSTED":
                    laddus+=50
    if origin=="INDIAN":
        redeem_month=laddus//200
        print(redeem_month)
    elif origin=="NON_INDIAN":
        print(laddus//400)
        
                
                    
                
    
    test_cases-=1
    