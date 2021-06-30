s1=input()
n=len(s1)
s2=s1[::-1]
m=n
dp=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(1,n+1):
	for j in range(1,m+1):
		if s1[i-1]==s2[j-1]:
			dp[i][j]=1+dp[i-1][j-1]
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])
