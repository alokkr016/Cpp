
public class MergeTwoSortedArrays {
    public static int[] merge(int arr1[], int arr2[]) {
        if(arr1.length == 0){
            return arr2;
        }
        if(arr2.length == 0){
            return arr1;
        }
        int j = 0;
        int k = 0;
        int i = 0;
        int []newArr = new int[arr1.length + arr2.length];
   
            while(j < arr1.length && k < arr2.length){
            if(arr1[j] < arr2[k]){
                newArr[i] = arr1[j];
                j++;
                i++;
            }
            else{
                newArr[i] = arr2[k];
                k++;
                i++;
            }
            
    }
    while(j < arr1.length){
        newArr[i] = arr1[j];
        i++;
        j++;
    }
    while(k < arr2.length){
        newArr[i] = arr2[k];
        i++;
        k++;
    }
        return newArr;
    }

}

class Main{
    public static void main(String []args){
        int []arr1 = {1,4,8,9,10,15,20};
        int []arr2 = {2,7,10};
        int []arr = MergeTwoSortedArrays.merge(arr1, arr2);
        for(int i = 0;i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
    }
}