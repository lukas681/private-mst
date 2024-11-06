def lmis(A, n):
    r = []
    for i in range(n):
        r+= [1]
        for j in range(i):
            if(A[j] < A[i]):
                r[i] = r[j] + 1
    print(r)
    return r

I = [9,8,7,6,5,4,1,2,3,2]
print(max(lmis(I, len(I))))
#%%
