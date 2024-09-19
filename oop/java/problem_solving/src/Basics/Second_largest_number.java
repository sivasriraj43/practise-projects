package Basics;

public class Second_largest_number {
	static int find(int []arr) {
		if (arr.length<2) {
            throw new IllegalArgumentException("Array must have at least two elements");
		}
		int largest = Integer.MIN_VALUE;
		int secondLargest= Integer.MIN_VALUE;
		
		for(int num:arr) {
			if(num>largest) {
				secondLargest =largest;
				largest = num;
			}else if (num>secondLargest && num != largest) {
				secondLargest = num;
			}
		}
		return secondLargest;
	}
	public static void main(String[] args) {
		int []arr = {1,5,2,7,3};
		int result = find(arr);
		System.out.println(result);
	}

}
