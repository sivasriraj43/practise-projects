package GeeksForGeeks;
//Input:
//A = AXY 
//B = YADXCP
//Output: 0 

//Input:
//A = gksrek
//B = geeksforgeeks
//Output: 1
//Explanation: A is a subsequence of B.
public class Check_for_subsequence {
	static boolean sequence(String A,String B) {
		
		int Aindex =0,Bindex=0;
		while(Aindex<A.length() && Bindex<B.length()) {
			if(A.charAt(Aindex)==B.charAt(Bindex)) {
				Aindex++;
			}
		Bindex++;
		}
		if(Aindex==A.length()) {
			return true;
		}else {
			return false;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(sequence("AXY", "YADXCP"));
		System.out.println(sequence("gksrek", "geeksforgeeks"));

		

	}

}
