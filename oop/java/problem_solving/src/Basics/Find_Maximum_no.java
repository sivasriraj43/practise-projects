package Basics;
//input 3,7,5 output 7
public class Find_Maximum_no {

	public static void main(String[] args) {
		int a=3,b=7,c=5;
		
		if(a>b && a>c) {
			System.out.print(a);
		}else
			if(a<b && b>c)
				System.out.println(b);
			else 
				System.out.print(c);
	}

}
