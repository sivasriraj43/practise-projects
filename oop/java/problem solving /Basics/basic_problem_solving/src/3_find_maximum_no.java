import java.util.Scanner;

class 3_find_maximum_no{
    System.out.println("a : ");
    Scanner obj = new Scanner(System.in);
    int a= obj.nextInt();
    System.out.println("b : ");
    int b = obj.nextInt();
    System.out.println("c : ");
    int c = obj.nextInt();
    System.out.println("Maximum : ");
    
    if (a>b||a>c){
        System.out.println(a);
    }
    else if (a<b||b>c){
        System.out.println(b);
    }else if (a<c||b<c){
        System.out.println(c);
    }else {
        System.out.println("equal");
    }

    }
    
