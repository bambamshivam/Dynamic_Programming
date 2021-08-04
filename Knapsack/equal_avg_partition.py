class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def avgset(self, A):
        n=len(A)
        s=sum(A)
        A.sort()
        d={}
        def chec(A,ss,i,c,l):
            if d.get((ss,i,c),-1)!=-1:
                return d[(ss,i,c)]
            if c==0:
                return (ss==0)
            if i>=len(A):
                return False
            if A[i]<=ss:
                l.append(A[i])
                if d.get((ss-A[i],i+1,c-1),-1)==-1:
                    d[(ss-A[i],i+1,c-1)]=chec(A,ss-A[i],i+1,c-1,l)
                if d[(ss-A[i],i+1,c-1)]:
                    return True
                l.pop()
            if d.get((ss,i+1,c),-1)==-1:
                d[(ss,i+1,c)]=chec(A,ss,i+1,c,l)
            if d[(ss,i+1,c)]:
                return True
            d[(ss,i,c)]=False
            return False

        for i in range(1,n):
            if (i*s)%n==0:
                ss=(i*s)//n
                l=[]
                if chec(A,ss,0,i,l):
                    di={}
                    a=[]
                    for j in l:
                        di[j]=di.get(j,0)+1
                    for t in A:
                        if di.get(t,0)!=0:
                            di[t]-=1
                        else:
                            a.append(t)
                    l1=[]
                    l.sort()
                    a.sort()
                    if len(l)<len(a):
                        l1.append(l)
                        l1.append(a)
                    elif len(l)>len(a):
                        l1.append(a)
                        l1.append(l)
                    else:
                        l1.append(a)
                        l1.append(l)
                        l1.sort()
                    return l1
        return []


        

obj=Solution()
print(obj.avgset([ 47, 14, 30, 19, 30, 4, 32, 32, 15, 2, 6, 24 ]))