package GeeksForGeeks;
import java.util.HashMap;

public class Count_characters {
	
	public static int count(String s,int n) {
		HashMap<Character,Integer> occur  =new HashMap<>();
		
		for(int i=0;i<s.length();i++) {
			char currentchar =s.charAt(i);
			
			if (i==0|| currentchar != s.charAt(i-1) ) {
				occur.put(currentchar, occur.getOrDefault(currentchar, 0)+1);
			}
		}
		
		int count =0;
		for(int occurence:occur.values() ) {
			if(occurence ==n) {
				count++;
			}
		}
		return count;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String S ="geeksforgeeks"
				;int n=2;
			System.out.println("output : "+count(S,n));

	}

}
