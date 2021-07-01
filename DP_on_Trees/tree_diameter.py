l=list(map(int,input().split()))
n=len(l)
adj=[[] for i in range(n)]
dp=[-1 for i in range(n)]
v=[0 for i in range(n)]
root=0
ans=[0]
for i in range(n):
	if l[i]!=-1:
		adj[i].append(l[i])
		adj[l[i]].append(i)
	else:
		root=i

def solve(i,ans):
	v[i]=1
	if len(adj[i])==1:
		dp[i]=1
		return 1
	if len(adj[i])==0:
		return 0
	m1,m2=0,0
	for j in range(len(adj[i])):
		if v[adj[i][j]]==0:
			if dp[adj[i][j]]==-1:
				dp[adj[i][j]]=solve(adj[i][j],ans)
			t=dp[adj[i][j]]
			if t>m1 and t>m2:
				m2=m1
				m1=t
			elif t>m2:
				m2=t
	ans[0]=max(ans[0],m1+m2+1)
	dp[i]=1+m1
	return dp[i]
solve(root,ans)
print(ans[0])




