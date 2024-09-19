package Basics;

public class Reversing_String {

	public static void main(String[] args) {
		String str="hello",revstr="";
		for(int i=0;i<str.length();i++) {
			revstr=str.charAt(i)+revstr;
		}
		System.out.print(revstr);
	} 
		

}
