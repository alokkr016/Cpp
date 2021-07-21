import java.util.Scanner;
public class CountZeros {
    public static int countZerosRec(int n){
        if(n==0){
            return 1;
        }
        if(n< 10){
            return 0;
        }
        int remainder = n % 10;
        if(remainder==0){
            return 1 + countZerosRec(n / 10);
        }
        else{
        return countZerosRec (n/10);
    }
}
}



 class runner {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = 500150047;
		System.out.println(CountZeros.countZerosRec(n));
	}
}
