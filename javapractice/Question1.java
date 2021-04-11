import java.util.Scanner;
public class Question1{
	public static void main(String args[]){
        int sum = 0;
        Scanner n = new Scanner(System.in);
        int num = n.nextInt();
        for(int i = 2;i <= num*2;i += 2){
            if (i % 2 == 0){
                sum = sum +i;
            }

        }
        System.out.print(sum);


    }
}