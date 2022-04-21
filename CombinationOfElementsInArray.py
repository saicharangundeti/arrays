from posixpath import split


from itertools import combinations 
def comb(inarr,innum):
    c=combinations(inarr,4)
    count=0
    for i in list(c):
        if sum(i)==innum:
            count+=1





inarr=map(int,input().split(''))
innum=int(input())

