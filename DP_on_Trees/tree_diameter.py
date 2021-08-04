pairs=["b-e","b-c","c-d","a-b","e-f"]

adj=[[] for i in range(26)]
for i in range(len(pairs)):
	adj[ord(pairs[i][0])-97].append(ord(pairs[i][2])-97)
	adj[ord(pairs[i][2])-97].append(ord(pairs[i][0])-97)
print(adj)
def dep(i,di):
    m = 0
    di[i]=1
    for j in range(len(adj[i])):
    	if di.get(adj[i][j],-1)==-1:
        	m = max(m , dep(adj[i][j],di))
    return m + 1

def solve(i,di):
	di[i]=1
	m1,m2=0,0
	for j in range(len(adj[i])):
		h=dep(adj[i][j],{})
		if h>m1:
			m2,m1=m1,h
		elif h>m2:
			m2=h

	m=0
	for j in range(len(adj[i])):
		if di.get(adj[i][j],-1)==-1:
			m=max(m,solve(adj[i][j],di))
	return max(m,m1+m2+1)

print(solve(0,{}))




