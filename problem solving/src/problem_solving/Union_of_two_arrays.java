package problem_solving;

import java.util.HashSet;

//input : arr1[] = [1,2,3,4,5], arr2[] = [1,2,3]  
//output : 5 


public class Union_of_two_arrays {
	
	static int union(int []arr1,int []arr2) {
		HashSet<Integer> set = new HashSet<>();
		for(int i: arr1) {
			set.add(i);
		}
		for(int i: arr2) {
			set.add(i);
		}
		
		return set.size();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
