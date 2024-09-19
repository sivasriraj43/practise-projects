package Basics;
//input = hello output 2
public class Count_vowels {
		static int vow(String str) {
			int count=0;String vowels="aeiouAEIOU"; 
			for(int i=0;i<str.length();i++) {
				if(vowels.indexOf(str.charAt(i)) !=-1) {
					 count ++;
				}
			}
			
			return count;
		}
		
	public static void main(String[] args) {
		System.out.print(vow("helloohgne"));
		
	}

}
