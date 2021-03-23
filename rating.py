anjali=[int(i) for i in input().split()]
maya=[int(j) for j in input().split()]
anjali_point=0
maya_point=0
for i in range(3):
    if anjali[i]>maya[i]:
        anjali_point+=1
    elif anjali[i]<maya[i]:
        maya_point+=1
print(anjali_point,maya_point)

