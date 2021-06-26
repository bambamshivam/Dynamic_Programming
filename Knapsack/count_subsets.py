n=int(input())
l=list(map(int,input().split()))
s=int(input())
dp=[[1 for i in range(s+1)] for i in range(n+1)]
for i in range(n+1):
	for j in range(s+1):
		if i==0:
			dp[i][j]=0

for i in range(n+1):
	for j in range(s+1):
		if j==0:
			dp[i][j]=1

for i in range(1,n+1):
	for j in range(1,s+1):
		if l[i-1]>j:
			dp[i][j]=dp[i-1][j]
		else:
			dp[i][j]=dp[i-1][j-l[i-1]] + dp[i-1][j]


	print()
print(dp[n][s])