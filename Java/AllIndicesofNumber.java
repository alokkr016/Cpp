// import java.util.Scanner;

// public class AllIndicesofNumber {
//     public static int[] allIndexes(int input[], int x) {
    
//         return allIndexes(input,x,0);
//     }
//     public static int[] allIndexes(int []arr, int x, int startIndex){
//         if(startIndex == arr.length){
//             int []newArr = {};
//             return newArr;
//         }


//     }
    
// }

//  class Runner3 {
	
// 	static Scanner s = new Scanner(System.in);
	
// 	public static int[] takeInput(){
// 		int size = s.nextInt();
// 		int[] input = new int[size];
// 		for(int i = 0; i < size; i++){
// 			input[i] = s.nextInt();
// 		}
// 		return input;
// 	}
	
// 	public static void main(String[] args) {
// 		int[] input = {9, 8, 10, 8, 8};
// 		int x = s.nextInt();
// 		int output[] = AllIndicesofNumber.allIndexes(input, x);
// 		for(int i = 0; i < output.length; i++) {
// 			System.out.print(output[i] + " ");
// 		}
// 	}
// }