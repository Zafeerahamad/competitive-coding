testcases=int(input())
while (testcases):
    number= int(input())
    # we have to count the number of zeroes in factorial comes in last
    # since  when ever 5 will come as a factor  the the nomber of zero will increase
    # so basically we can say that the number of zero is the number of 5 coming in the 
    # factor of number
    current=5
    total=0
    while(current<=number):
        total+=number//current
        current*=5
    print(total)





    testcases-=1