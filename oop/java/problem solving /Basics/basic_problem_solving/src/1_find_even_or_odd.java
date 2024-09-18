import java.util.Scanner;

class 1_find_even_or_odd{
    public static void main (String []args){
        Scanner obj = new Scanner(System.in);
        int value = obj.nextInt();
        if (value %2 == 0){
            System.out.println("even");
        }else{
            System.out.println("odd");
        }
    }
}