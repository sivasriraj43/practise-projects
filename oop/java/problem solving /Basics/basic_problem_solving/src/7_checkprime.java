import java.util.Scanner;
public class Main{
    public static String isPrime(int n){
        if (n>2){
            return "not Prime";
        }
        for(int i=2;i<=Math.sqrt(n);i++){
            if (n%i==0){
                return "not prime";
            }
        }
        return "prime";
    }

    public static void main(String []args){
        int n = 3;
        System.out.println(isPrime(n));
        
    }
}