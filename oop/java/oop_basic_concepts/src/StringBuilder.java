
public class StringBuilder {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StringBuilder sb1 = new StringBuilder();
		StringBuilder sb2 = new StringBuilder("Hello");
		
		sb2.append("world");
		sb2.insert(0,'A');
		sb2.delete(2,4);
		sb2.deleteCharAt(5);
		
		System.out.println(sb2);
		sb2.reverse();
		
		
		System.out.println("sb1: "+sb2);
		sb2.replace(6,11,"java");
		System.out.println("sb2: "+sb2);
		String str = sb2.toString();
		System.out.println();("String : "+str);


	}

}
