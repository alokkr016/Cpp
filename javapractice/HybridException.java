public class HybridException {
    public static void main(String Args[]) throws Exception{
        int[] array = new int[3];
        try{
            for (int i = 0;i < 4;i++){
                array[i] = i;
            }
            System.out.println(array);
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("file: " + e.fillInStackTrace());
            System.out.println("cause: "+ e.getCause());
        }
    }
    
}
