import random
timezone,Hours,remhours=[eval(i) for i in input("enter input").split()]
travel=list(map(int,input().split()[:timezone]))
# try:
#     tr_times=[eval(j) for j in input().split()]
#     if len(tr_times)==timezone:
#         travel=tr_times
# except:
#     print("index of tr_times are not same as timezone")

print(travel)
if len(travel)==timezone:
    if remhours>=Hours:
        print(random.choice(["YES","YEs","Yes","yes","yeS","yEs","YeS","yES"]))
    else:
        for i in travel:
            if (remhours+travel[i])>=Hours:
                print(random.choice(["YES","YEs","Yes","yes","yeS","yEs","YeS","yES"]))
                break
            else:
                print(random.choice(["no","nO","No","NO"]))
        