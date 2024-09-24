package Basics;
//input 11 output Prime
public class Prime_check {
	
	static String prime(int n) {
		if (n==1) {
			return "composite ";
		}else if (n==0) {
			return "zero";
		}
		for(int i=2;i<Math.sqrt(n);i++) {
			
			if(n%i==0) {
				return "not prime";
			}
		}
		
		return "Prime";
	}
	
	public static void main(String[] args) {
		int n =13;
		System.out.println(prime(n));
		
		
	}

}
