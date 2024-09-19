package Basics;
//input 123 output = 6
public class Sum_of_digits {

	public static void main(String[] args) {
		
		int n =123,sum=0;
		while(n!=0) {
			sum = sum+n%10;
			n = n/10;
		}
		System.out.println(sum);
			
	}

}
