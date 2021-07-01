//Scramble String using Memoization(Dynamic Programming)
//Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
//Below is one possible representation of A = great:
// great
//   /    \
//  gr    eat
// / \    /  \
//g   r  e   at
//           / \
//          a   t
//To scramble the string, we may choose any non-leaf node and swap its two children.

//For example, if we choose the node gr and swap its two children, it produces a scrambled string rgeat:

//    rgeat
//   /    \
//  rg    eat
// / \    /  \
//r   g  e   at
//          / \
//          a   t
//We say that rgeat is a scrambled string of great.

//Similarly, if we continue to swap the children of nodes eat and at, it produces a scrambled string rgtae

//    rgtae
//   /    \
//  rg    tae
// / \    /  \
//r   g  ta  e
//       / \
//      t   a
//We say that rgtae is a scrambled string of great.

import java.util.*;
public class scrambled_string{
	static HashMap<String, Integer> map; 
	public static int solve(String s1,String s2){
		if(map.getOrDefault(s1+" "+s2,-1)!=-1)
			return map.get(s1+" "+s2);
		int n1=s1.length();
		int n2=s2.length();
		if(n1==0 && n2==0)
			return 1;
		if(n1!=n2)
			return 0;
		if(s1.equals(s2)){
			map.put(s1+" "+s2,1);
			return 1;
		}
		int t=0;
		for(int i=1;i<n1;i++){
			int a=solve(s1.substring(0,i),s2.substring(0,i));
			int b=solve(s1.substring(i),s2.substring(i));
			int c=solve(s1.substring(0,i),s2.substring(n1-i));
			int d=solve(s1.substring(i),s2.substring(0,n1-i));
			if((a==1 && b==1) || (c==1 && d==1)){
				t=1;
				break;
			}
		}
		map.put(s1+" "+s2,t);
		return t;
	}

    public static int scramble(String s1,String s2) {
    	int n1=s1.length();
    	int n2=s2.length();
    	map=new HashMap<>();
    	if(n1!=n2 || n1==0 || n2==0)
    		return 0;
		return solve(s1,s2);
    }

    public static void main(String[] args){
    	Scanner sc=new Scanner(System.in);
    	String s1=sc.next();
    	String s2=sc.next();
		System.out.println(scramble(s1,s2));
    }
}
