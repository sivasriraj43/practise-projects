package GeeksForGeeks;

public class Sum_palindrome {
		static long palindrome(long n) {
			
			for(int i=0;i<=5;i++) {
				long result=0,temp=n,rem;
			
				while(n>0) {
				rem=n%10;
				result=result*rem;
				n=n/10;
				}
				
				if(temp==result) {
					return result;
				}else  {
					n=temp+result;
				}
				}
			
			
			return -1;
		}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long v=23;
		System.out.println(palindrome(v));

	}

}
//
//Input: n = 23
//Output: 55 
//Explanation: reverse(23) = 32,then 32+23 = 55 which is a palindrome. 
//Input: n = 73
//Output: 121
//Explanation: reverse(73) = 37,then 37+73 = 110 which is not a palindrome, again reverse(110)= 011, then 110+11 = 121 which is a palindrome.
