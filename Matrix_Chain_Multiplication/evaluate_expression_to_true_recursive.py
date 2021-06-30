import math
s=input()
n=len(s)
def solve(s,i,j,isTrue):
	if i>j:
		return 0
	if i==j:
		if isTrue:
			return 1 if s[i]=='T' else 0
		else:
			return 1 if s[i]=='F' else 0
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
	return ans


print(solve(s,0,n-1,True))



