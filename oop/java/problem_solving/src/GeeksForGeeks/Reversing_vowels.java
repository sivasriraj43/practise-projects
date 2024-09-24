package GeeksForGeeks;
//Input: 
//S = "practice"
//Output: prectica
//Explanation: The vowels are a, i, e
//Reverse of these is e, i, a.

public class Reversing_vowels {
	static String reversevow(String s) {
		//s.toLowerCase();
		char[] ch =s.toCharArray();
		
		int left =0,right = ch.length-1;
		
		while(left<right) {
				if(!isVowel(ch[left])) {
					
				
				left++;
				}
				
				else

				if(!isVowel(ch[right])) {

				right--;
			}
				else
			if(left<right) {
				char temp =ch[left];
				ch[left]=ch[right];
				ch[right]=temp;
				left++;right--;
			}
		}
		return new String(ch).toLowerCase();
	}
	
	
	private static boolean isVowel(char c) {
		return "AEIOUaeiou".indexOf(c) != -1;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(reversevow("Aeroplane"));

	}

}
