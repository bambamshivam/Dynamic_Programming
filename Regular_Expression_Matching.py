#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

#'.' Matches any single character.​​​​
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        m=len(p)
        di={}
        def solve(i,j):
            if di.get((i,j),-1)!=-1:
                return di[(i,j)]
            if i>=n and j>=m:
                return True
            if j>=m:
                return False
            match=i<n and (s[i]==p[j] or p[j]=='.')
            if j+1<m and p[j+1]=='*':
                di[(i,j)]=(match and solve(i+1,j)) or solve(i,j+2)
                return di[(i,j)]
            if match:
                di[(i,j)]=solve(i+1,j+1)
                return di[(i,j)]
            di[(i,j)]=False
            return False
        return solve(0,0)
            