
class 2_sum_of_digits{
    public static main (String []args){
        int n = 123,sum = 0;
        while (n!=0){
            sum = sum+n%10;
            n=n/10;

        }
        System.out.println(sum);
    }
}