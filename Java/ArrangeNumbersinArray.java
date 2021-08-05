public class ArrangeNumbersinArray {
    public static void arrange(int n){
        int arr[]  = new int[n];
        if(n % 2 != 0){
            int i = 0;
            int j = 0;
            while(i < n/2){
                arr[i] = j + 1;
                arr[n - i - 1] = arr[i] + 1;
                j = arr[n -i -1];
                i++;
            }
            arr[n / 2] = n;
        }
        else {
            int i = 0;
            int j = 0;
            while(i < n/2){
                arr[i] = j + 1;
                arr[n - i - 1] = arr[i] + 1;
                j = arr[n -i -1];
                i++;
            }

        }

        for(int elements : arr){
            System.out.print( elements + " ");
        }
        System.out.println();
    }
    public static void arrange1(int n){
        int arr[]  = new int[n];
        int start = 0;
        int end = n - 1;
        int i = 0;
        while(start < end){
            arr[start] = i + 1;
            arr[end] = arr[start] + 1;
            i = arr[end];
            start++;
            end--;
        }
        if( n % 2 != 0){
            arr[start] = n;
        }
        for(int elements : arr){
            System.out.print( elements + " ");
        }
        System.out.println();
    }

    public static void main(String[] args){
        arrange(6);
        arrange(5);
        arrange1(6);
        arrange1(5);
    }
    
}
