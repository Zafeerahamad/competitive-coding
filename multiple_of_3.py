testcases=int(input())
while (testcases):
    k,d0,d1=[eval(i) for i in input().split()]      # here s=d0+d1 and  each element is the sum of the  all previous element
    s=d0+d1
    first_3_sum=s+s%10
    cycle=(k-3)//4
    sum_cycle= 2*s%10 +4*s%10 +8*s%10 + 6*s%10
    rest=k-cycle*4-3
    #print(rest,sum_cycle)
    sum_rest=0
    for j in range(rest):
        sum_rest+=((2**(j+1))* s)%10
    #print(sum_rest)

    total_digit_sum=first_3_sum + cycle * sum_cycle + sum_rest
    #print(total_digit_sum)
    if total_digit_sum%3==0:
        print("YES")
    else:
        print("NO")

    testcases-=1