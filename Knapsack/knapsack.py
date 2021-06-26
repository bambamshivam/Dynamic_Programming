n=int(input())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
w=int(input())
dp=[[0 for i in range(w+1)] for i in range(n+1)]
for i in range(1,n+1):
	for j in range(1,w+1):
		if wt[i-1]>j:
			dp[i][j]=dp[i-1][j]
		else:
			dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
print(dp[n][w])