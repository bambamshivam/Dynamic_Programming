import math

def pal(s,i,j):
	while i<=j:
		if s[i]!=s[j]:
			return False
		i+=1
		j-=1
	return True

s=input()
n=len(s)
dp=[[-1 for i in range(n+1)] for i in range(n+1)]
def solve(s,i,j):
	if i>=j or pal(s,i,j):
		return 0
	m=math.inf
	for k in range(i,j):
		if dp[i][k]==-1:
			dp[i][k]=solve(s,i,k)
		if dp[k+1][j]==-1:
			dp[k+1][j]=solve(s,k+1,j)
		temp=dp[i][k]+dp[k+1][j]+1
		m=min(m,temp)
	dp[i][j]=m
	return m


print(solve(s,0,n-1))



