import java.util.*;
public class palindrome_partitioning{
	static int dp[][];
	public static boolean ispal(String s,int i,int j){
		while(i<=j){
			if(s.charAt(i)!=s.charAt(j))
				return false;
			i++;
			j--;
		}
		return true;
	}

	public static int solve(String s,int i,int j){
		if(dp[i][j]!=-1)
			return dp[i][j];
		if(i>=j){
			dp[i][j]=0;
			return 0;
		}
		if(ispal(s,i,j)){
			dp[i][j]=0;
			return 0;
		}
		int min=s.length()+1;
		for(int k=i;k<j;k++){
			if(dp[i][k]==-1)
				dp[i][k]=solve(s,i,k);
			if(dp[k+1][j]==-1)
				dp[k+1][j]=solve(s,k+1,j);
			int temp=dp[i][k]+dp[k+1][j]+1;
			if(temp<min)
				min=temp;
		}
		dp[i][j]=min;
		return min;
	}

    public static int minCut(String A) {
    	int n=A.length();
    	dp=new int[n+1][n+1];
    	for(int i=0;i<n+1;i++){
    		for(int j=0;j<n+1;j++)
    			dp[i][j]=-1;
    	}
    	if(n==0 || n==1)
    		return 0;
		return solve(A,0,n-1);
    }

    public static void main(String[] args){
    	Scanner sc=new Scanner(System.in);
    	String str=sc.next();
    	System.out.println(minCut(str));
    }
}
