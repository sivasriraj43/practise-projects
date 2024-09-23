import java.util.HashSet;
import java.util.Iterator;

public class Hashset_eg {

	public static void main(String[] args) {
		
		HashSet<String> set = new HashSet<>();
		
		set.add("Apple");
		set.add("Banana");
		set.add("Orange")
;
		boolean added = set.add("Apple");
		
		System.out.println("HashSet: "+set);
		
		boolean containbanana = set.contains("Banana");
		
		set.remove("Orange");
		
		System.out.println("Afer romoval : "+set);
		System.out.println(containbanana);
		
		System.out.println("For each loop");
		for(String fruit : set ) {
			System.out.println(fruit);
	
		}
		System.out.println("Using iterator : ");
		Iterator<String> iterator = set.iterator();
		while(iterator.hasNext()) {
			System.out.println(iterator.next());
			
		System.out.println("size : "+set.size());
		System.out.println("empty or not "+set.isEmpty());
		//set.clear();
		System.out.println("after clear "+ set.isEmpty());
		
		String[] array = set.toArray(new String[0]);
		
		System.out.println("Array from HashSet : ");
		for(String fruits : array) {
			System.out.println(fruits);
		}
		
		HashSet<String> set2 = new HashSet<>();
		set2.add("Banana");
		set2.add("Grapes");
		set2.add("Mango");
		
//Union
		HashSet<String> union = new HashSet<>(set);
		union.addAll(set2);
		System.out.println();
		System.out.println("Union : " +union);
		
//Intersection 
		HashSet<String> intersection = new HashSet<>(set);
		intersection.retainAll(set2);
		System.out.println();
		System.out.println("Intersection : "+intersection);
		
//Difference
		HashSet<String> difference = new HashSet()
		
		
		
		
		}
		
	}

}
