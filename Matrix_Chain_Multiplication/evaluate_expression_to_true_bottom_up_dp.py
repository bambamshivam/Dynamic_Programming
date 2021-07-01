import math
#Evaluate Expression To True-Boolean Parenthesization Memoized
#Given a boolean expression with following symbols.
#Symbols
#   'T' --- true 
#    'F' --- false 
#And following operators filled between symbols
#Operators
#    &   --- boolean AND
#    |   --- boolean OR
#    ^   --- boolean XOR 
#Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.
#Example:
#Input: symbol[]    = {T, F, T}
#       operator[]  = {^, &}
#Output: 2
#The given expression is "T ^ F & T", it evaluates true
#in two ways "((T ^ F) & T)" and "(T ^ (F & T))"
s=input()
n=len(s)
di={}
def solve(s,i,j,isTrue):
    if i>j:
        return 0
    if i==j:
        if isTrue:
            return 1 if s[i]=='T' else 0
        else:
            return 1 if s[i]=='F' else 0
    if di.get((i,j,isTrue),-1)!=-1:
        return di[(i,j,isTrue)]
    ans=0
    for k in range(i+1,j,2):
        lf=solve(s,i,k-1,False)
        lt=solve(s,i,k-1,True)
        rf=solve(s,k+1,j,False)
        rt=solve(s,k+1,j,True)
        if s[k]=='&':
            if isTrue:
                ans+=lt*rt
            else:
                ans+=lf*rf+lf*rt+lt*rf
        if s[k]=='|':
            if isTrue:
                ans+=lf*rt+lt*rf+lt*rt
            else:
                ans+=lf*rf
        if s[k]=='^':
            if isTrue:
                ans+=lf*rt+lt*rf
            else:
                ans+=lf*rf+lt*rt
    di[(i,j,isTrue)]=ans
    return ans


print(solve(s,0,n-1,True))



