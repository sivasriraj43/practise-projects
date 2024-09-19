package Basics;
//input madam output palindrome
public class Palindrome {

	public static void main(String[] args) {
		String str = "madam" ,revstr="";
		for(int i=0;i<str.length();i++) {
			revstr=str.charAt(i)+revstr;
			
		}
		if(str.equals(revstr)) {
			System.out.println("Palindrome");
		}else {
			System.out.println("not Palindrome");
		}
			
	}

}
