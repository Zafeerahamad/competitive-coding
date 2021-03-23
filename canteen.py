# t=int(input())
# while(t):
#     num_frnd,eggs,chocolate,o_price_1,c_milk_price_1,c_cake_price_1=[eval(i) for i in input().split()]
#     netcost=[]
#     if eggs>0:
#         omelate_net_cost=o_price_1*2/eggs
#         netcost.append(o_price_1*2/eggs)
#     else:
#         omelate_net_cost=10000
#     if chocolate>0:
#         c_milk_net_cost=c_milk_price_1*3/chocolate
#         netcost.append(c_milk_price_1*3/chocolate)
#     else:
#         c_milk_net_cost=10000
#     if chocolate>0 and eggs>0:
#         c_cake_net_cost=c_cake_price_1*((1/eggs)+(1/chocolate))
#         netcost.append(c_cake_price_1*((1/eggs)+(1/chocolate)))
#     else:
#         c_cake_net_cost=10000
    
    
    
#     netcost.sort()
    
#     money=0
#     frnd=0
#     for i in range(len(netcost)):
#         if netcost[i]==omelate_net_cost:
#             while num_frnd>frnd:
#                 if eggs>=2:
#                     eggs-=2
#                     frnd+=1
#                     money+=o_price_1
#                 else:
#                     break
#         if netcost[i]==c_milk_net_cost:
#             while num_frnd>frnd:
#                 if chocolate>=3:
#                     chocolate-=3
#                     frnd+=1
#                     money+=c_milk_price_1
#                 else:
#                     break
#         if netcost[i]==c_cake_net_cost:
#             while num_frnd>frnd:
#                 if eggs>=1 and chocolate>=1:
#                     eggs-=1
#                     chocolate-=1
#                     frnd+=1
#                     money+=c_cake_price_1
#                 else:
#                     break
#     if num_frnd==frnd:
#         print(money)
#     else:
#         print("-1")

#     t-=1# cook your dish here





def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
# Driver program to test above function 
val = [1,2,3] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n)) 