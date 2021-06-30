import math
l=list(map(int,input().split()))
n=len(l)
dp=[[-1 for i in range(n+1)] for i in range(n+1)]
def solve(l,i,j):
	if i>=j:
		dp[i][j]=0
		return 0
	m=math.inf
	for k in range(i,j):
		if dp[i][k]==-1:
			dp[i][k]=solve(l,i,k)
		if dp[k+1][j]==-1:
			dp[k+1][j]=solve(l,k+1,j)
		temp=dp[i][k]+dp[k+1][j]+l[i-1]*l[k]*l[j]
		m=min(m,temp)
	dp[i][j]=m
	return m


print(solve(l,1,n-1))



