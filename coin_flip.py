t=int(input())
while(t):
    g = int(input())
    while(g):
        initial_state,n_round,req_state=[int(i) for i in input().split()]
        if initial_state==1:
            if n_round%2==0:
                n_heads=n_round//2
                n_tails=n_round//2
            else:
                n_heads=n_round//2
                n_tails=(n_round//2)+1
        elif initial_state==2:
            if n_round%2==0:
                n_heads=n_round//2
                n_tails=n_round//2
            else:
                n_heads=(n_round//2)+1
                n_tails=(n_round//2)
        if req_state==1:
            print(n_heads)
        elif req_state==2:
            print(n_tails)
        
        
        g-=1
    
    
    t-=1