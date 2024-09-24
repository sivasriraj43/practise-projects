package GeeksForGeeks;

public class Sum_of_prime {
	static int prime(int n) {
		int sum =0,temp=n,rem;
		while(n!=0) {
			rem=n%10;
			
			if(rem==2||rem==3||rem==5||rem==7) {
				 sum=sum+rem;
			}
			n=n/10;
		}
		
		return sum;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(prime(333));

	}

}
