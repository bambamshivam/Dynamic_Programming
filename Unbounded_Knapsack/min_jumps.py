n=int(input())
l=list(map(int,input().split()))
s=int(input())
dp=[[True for i in range(s+1)] for i in range(n+1)]
for i in range(n+1):
	for j in range(s+1):
		if i==0:
			dp[i][j]=(False,0)

for i in range(n+1):
	for j in range(s+1):
		if j==0:
			dp[i][j]=(True,0)

for i in range(1,n+1):
	for j in range(1,s+1):
		if l[i-1]>j:
			dp[i][j]=dp[i-1][j]
		else:
			p=dp[i][j-l[i-1]]
			q=dp[i-1][j]
			if p[0]==True:
				if q[0]==True:
					dp[i][j]=(True,min(dp[i][j-l[i-1]][1]+1,dp[i-1][j][1]))
				else:
					dp[i][j]=(True,dp[i][j-l[i-1]][1]+1)
			else:
				if q[0]==True:
					dp[i][j]=(True,dp[i-1][j][1])
				else:
					dp[i][j]=(False,0)
print(dp[n][s][1])