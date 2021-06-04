import java.io.FileInputStream;

public class DemonstrationFileInputStream {
    public static void main(String args[])
    {
        try{

        FileInputStream fin = new FileInputStream("A:/Vs Code workspace/MyWorkSpace/javapractice/My.txt");
        int i = 0;
        while((i = fin.read()) != -1){
            System.out.print((char)i);
        }
        fin.close();

        }
        catch(Exception e){ 
            System.out.print(e);
        }
    }
    
}
