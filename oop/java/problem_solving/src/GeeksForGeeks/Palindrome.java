package GeeksForGeeks;

public class Palindrome {
	 public static String palindrome(int n)
	    {
	        // Code here
	        String originalStr=Integer.toString(n);
	        String reverseStr=new  StringBuilder(originalStr).reverse().toString();
	        
	        if(originalStr.equals(reverseStr)){
	            return "Yes";
	        }
	        return "No";
	    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(palindrome(22));
	}

}
