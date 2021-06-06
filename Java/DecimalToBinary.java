import java.util.Scanner;

import static java.lang.Integer.parseInt;

public class DecimalToBinary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String bin = sc.next();
        int s = parseInt(bin);
        

        int temp = 0;
        
        
        long res = 0;
        long i = 0;
        while(s > 0){
            temp = s % 2;
            s = s / 2;

           res += (long)(temp * Math.pow(10, i));
            
            i++;
        }
        System.out.print(res);
    }

}