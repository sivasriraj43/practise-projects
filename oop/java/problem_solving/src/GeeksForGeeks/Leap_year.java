package GeeksForGeeks;

public class Leap_year {
	static int leapYear(int n) {
		if(n%100!=0 && n%4==0) {
			return 1;
		}else if(n%400==0) {
			return 1;
		}
		return 0;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(leapYear(2020));
	}

}
