public class Returnsubsetofanarray{
    public static int[][] subArray(int[] array){
        return subArray(array,0);
    }
    public static int[][] subArray(int []array,int startIndex){
        if(startIndex == array.length){
            int[][] temp = new int[1][0];
            return temp;
        }
        int[][] substring = subArray(array,startIndex + 1);
        int[][] ans = new int[2*substring.length][];
        int k = 0;
        for(int i=0;i < substring.length;i++){
            ans[i] = new int[substring[i].length];
            for(int j = 0;j < substring[i].length;j++){
                ans[i][j] = substring[i][j];
            }
            k++;
        }
        for(int i = 0;i < substring.length;i++){
            ans[k + i] = new int[substring[i].length + 1];
            ans[k + i][0] = array[startIndex];
            for(int j = 1;j <= substring[i].length;j++){
                ans[i + k][j] = substring[i][j - 1];
            
            }
        }

        return ans;
    }
    public static void main(String[] args){
        int []num = {1,2,3};
        int[][] output = Returnsubsetofanarray.subArray(num);
        for(int i = 0; i < output.length; i++) {
			for(int j = 0; j < output[i].length; j++) {
				System.out.print(output[i][j] + " ");
			}
			System.out.println();
		}
    }
}