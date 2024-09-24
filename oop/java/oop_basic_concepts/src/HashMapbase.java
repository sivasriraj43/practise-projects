import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;


public class HashMapbase {
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		HashMap<Integer,String> map =new HashMap<>();
//adding element	
		map.put(1, "Apple");
		map.put(2,"Bannana");
		map.put(3, "Orange");
		
		System.out.println("HashMap : "+map);

//accessing value 
		System.out.println("access : "+ map.get(2));
		
//modifying the value
		map.put(2, "watermelon");
		System.out.println("HashMap : "+map);
		
//Removing the value
		map.remove(3);
		System.out.println("HashMap : "+map);
		
//Checking key
		System.out.println(map.containsKey(2));

//Checking value
		System.out.println(map.containsValue("Apple"));

// Iterating over keys
        System.out.println("Iterating over keys:");
        for (int key : map.keySet()) {
            System.out.print(key);
        }
        System.out.println();
        
// Iterating over values
        System.out.println("Iterating over values:");
        for (String value : map.values()) {
            System.out.print(value);
        }
        
// Iterating over key-value pairs
        System.out.println("Iterating over Key-value pairs: ");
        for(Entry<Integer, String> entry : map.entrySet()) {
        	System.out.println(entry.getKey() +": " +entry.getValue());
        }
        
        System.out.println("size : "+map.size());
        
// Clearing the HashMap
        map.clear();
        System.out.println("Hashmap after clear : "+map);
        

	}

}
