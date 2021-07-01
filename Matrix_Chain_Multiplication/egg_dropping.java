/**Egg Dropping using Memoization Optimization

Problem statement: You are given N floor and K eggs. You have to minimize the number of times you have to drop the eggs to find the critical floor where critical floor means the floor beyond which eggs start to break. Assumptions of the problem:

If egg breaks at ith floor then it also breaks at all greater floors.
If egg does not break at ith floor then it does not break at all lower floors.
Unbroken egg can be used again.
Note: You have to find minimum trials required to find the critical floor not the critical floor.

Example:
Input:
    4
    2
    
    Output:
    Number of trials when number of eggs is 2 and number of floors is 4: 3*/
import java.util.*;
public class egg_dropping{
	static int dp[][];
	public static int solve(int e,int f){
		if(dp[e][f]!=-1)
			return dp[e][f];
		if(e==1){
			dp[e][f]=f;
			return f;
		}
		if(f==0 || f==1){
			dp[e][f]=f;
			return f;
		}
		int min=f+1;
		for(int k=1;k<=f;k++){
			if(dp[e-1][k-1]==-1)
				dp[e-1][k-1]=solve(e-1,k-1);
			if(dp[e][f-k]==-1)
				dp[e][f-k]=solve(e,f-k);
			int temp=Math.max(dp[e-1][k-1],dp[e][f-k])+1;
			min=Math.min(min,temp);
		}
		dp[e][f]=min;
		return min;
	}

    public static int eggdrop(int e,int f){
    	if(e==1){
			return f;
		}
		if(f==0 || f==1){
			return f;
		}
    	dp=new int[e+1][f+1];
    	for(int i=0;i<e+1;i++){
    		for(int j=0;j<f+1;j++)
    			dp[i][j]=-1;
    	}
		return solve(e,f);
    }

    public static void main(String[] args){
    	Scanner sc=new Scanner(System.in);
    	int e=sc.nextInt();
    	int f=sc.nextInt();
    	System.out.println(eggdrop(e,f));
    }
}
