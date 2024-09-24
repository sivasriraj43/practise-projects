package GeeksForGeeks;
import java.util.HashSet;
//Input: arr1[] = [1, 2, 3, 4, 5], arr2[] = [1, 2, 3]
//Output: 5

public class Union_of_two_arrays {
	 public static int Union(int a[],  int b[]) 
	    {
	        HashSet<Integer> Un=new HashSet<>();
	        for(int i:a){
	            Un.add(i);
	        }
	        for(int i:b){
	            Un.add(i);
	        }
	        return Un.size();
	    }
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a[]= {1, 2, 3, 4, 5};
		int b[]= {1, 2, 3};
		
		System.out.println(Union(a,b));
		
	}

}
