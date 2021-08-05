import java.util.Scanner;
/*
Given a 2D integer array with n rows and m columns. 
Print the 0th row from input n times, 1st row n-1 times…..(n-1)th row 
will be printed 1 time.
*/
public class Print2Darray {
    public static void print2DArray(int arr[][]){
        int rows = arr.length;
        int columns = arr[0].length;
        for(int i = 0;i < rows;i++){
            int j = 0;
           
            while(j < rows - i){
                for(int m = 0; m < arr[i].length;m++){
                    System.out.print(arr[i][m] + " ");
                }
                System.out.println();
                j++;
            }
            
        }
    
}
}


 class TwoDarray {
	static Scanner s = new Scanner(System.in);
	
	public static int[][] takeInput(){
		int numRows = s.nextInt();
		int numCols = s.nextInt();
		int[][] input = new int[numRows][numCols];
		for(int i = 0; i < numRows; i++){
			for(int j = 0; j < numCols; j++){
				input[i][j] = s.nextInt();
			}
		}
		return input;
	}

	public static void main(String[] args) {
		int[][] input = takeInput();
		Print2Darray.print2DArray(input);
	}
}