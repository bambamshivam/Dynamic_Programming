n=int(input())
coins=list(map(int,input().split()))
sum=int(input())
dp=[[0 for i in range(sum+1)] for i in range(n+1)]
for i in range(0,1):
	for j in range(sum+1):
		if i==0:
			dp[i][j]=10**9

for i in range(0,1):
	for j in range(sum+1):
		if j==0:
			dp[i][j]=0



for i in range(1,n+1):
	for j in range(1,sum+1):
		if l[i-1]>j:
			dp[i][j]=dp[i-1][j]
		else:
			dp[i][j]=dp[i][j-l[i-1]] + dp[i-1][j]

