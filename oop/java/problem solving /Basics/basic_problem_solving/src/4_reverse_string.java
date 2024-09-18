
class Main{
    public static void main (String []args){
        String str ="hello",revstr="";
        for (int i=0;i<str.length();i++){
            revstr=str.chartAt(i)+revstr;
        }
        System.out.println(revstr);
    }
}