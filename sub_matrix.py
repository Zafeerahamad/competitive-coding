def get_all_sub_mat(mat):
    rows = len(mat)
    cols = len(mat[0])
    def ContinSubSeq(lst):
        size=len(lst)
        for start in range(size):
            for end in range(start+1,size+1):
                yield (start,end)
    for start_row,end_row in ContinSubSeq(list(range(rows))):
        for start_col,end_col in ContinSubSeq(list(range(cols))):
            yield [i[start_col:end_col] for i in mat[start_row:end_row] ]

def Solve(M,N,P,Matrix):
    count=0
    for i in get_all_sub_mat(Matrix):
        sum1=0
        for j in i:
            sum1+=sum(j)
        if sum1%P==0:
            count+=1
    print(count)
            
        

M,N,P = map(int,input().split())

Matrix = []

for _ in range(M):
    Matrix.append(list(map(int,input().split())))

Solve(M,N,P,Matrix)
