package GeeksForGeeks;

import java.util.HashSet;

public class Remove_Character {
	static String remove(String String1,String String2) {
		HashSet<Character> set = new HashSet<>();
		
		StringBuilder str = new StringBuilder();
		for(char i :String2.toCharArray()) {
			set.add(i);
		}
		for(char i: String1.toCharArray()) {
			if(!set.contains(i)){
				str.append(i);
			}
		}
		return str.toString();
		
	}

	public static void main(String[] args) {
		System.out.println(remove("computer","cat"));

	}

}
