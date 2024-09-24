package GeeksForGeeks;

public class Check_for_power {
		static int pow(long x,long y) {
			for(int i=1;i<y;i++) {
			if(Math.pow(x,i)==y) {
				return 1;
			}
				}
			return 0;
		}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long v = pow(1,8);
		System.out.println(v);
	}

}
//
//Input:
//X = 2, Y = 8
//Output:
//1
//Explanation:
//23 is equal to 8.

//Input:
//X = 1, Y = 8
//Output:
//0
//Explanation:
//Any power of 1 is not 
//equal to 8.
