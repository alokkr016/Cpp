public class MyexceptionThrows {
    public static void main(String args[]) throws Exception{
        int[] array = new int[3];
        try{
            for(int i = 0;i <4;i++ ){
                array[i] = i;

            }
            System.out.println(array);
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("fillin" + e.fillInStackTrace());
            System.out.println("Clauese" + e.getCause());


            throw(Exception) new Exception().initCause(e);
        }
        finally{
            System.out.println(array);
        }
    }
    
}
