package Basics;
//input : 5 output 0,1,1,2,3
public class Fibonacci_sequence {

	public static void main(String[] args) {
		int n=5,a=0,b=1,c;
		for(int i=0;i<n;i++) {
			System.out.print(a+" ");
			c=a+b;
			a=b;
			b=c;
			
		}
		
	}

}
