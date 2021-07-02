l=list(map(int,input().split()))
n=len(l)
adj=[[] for i in range(n)]
root=0
ans=[0]
for i in range(n):
	if l[i]!=-1:
		adj[i].append(l[i])
		adj[l[i]].append(i)
	else:
		root=i
		adj[i].append(i)
l[root]=0
def solve(i,ans):
	if len(adj[i])<=1:
		return 1
	m1,m2=0,0
	for j in range(len(adj[i])):
		t=0
		if adj[i][j]!=l[i]:
			t=solve(adj[i][j],ans)
		if t>m1:
			m2=m1
			m1=t
		elif t>m2:
			m2=t
	ans[0]=max(ans[0],m1+m2+1)
	return 1+m1
if len(l)==1:
	print(0)
else:
	solve(root,ans)
	print(ans[0]-1)




