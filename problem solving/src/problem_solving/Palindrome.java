package problem_solving;

public class Palindrome {
	public static String palindrome(int n) {
		String originalStr = Integer.toString(n);
		String reverseStr= new StringBuilder(originalStr).reverse().toString();
		
		if(originalStr.equals(reverseStr)) {
			return "Yes";
		}
		return "No";
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(palindrome(555));  // Output: Yes
        System.out.println(palindrome(11)); 

	}

}
