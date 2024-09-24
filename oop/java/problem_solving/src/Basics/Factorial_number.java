package Basics;
//input 4 output 24
public class Factorial_number {

	public static void main(String[] args) {
		int n=4,fact=1;
		for(int i=1;i<=n;i++) {
			fact=fact*i;
		}
		System.out.println(fact);
	}

}
