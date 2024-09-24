package GeeksForGeeks;

public class Sum_palindrome {
		static long palindrome(long n) {
			
			for(int i=0;i<=5;i++) {
				long result=0,temp=n;
			
				while(n>0) {
				
				result=result*n%10;
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
		System.out.println(palindrome(23));

	}

}
