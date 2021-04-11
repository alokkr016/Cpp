import java.io.FileOutputStream;

class DemonstratinFileOutputstream{
    public static void main(String args[]){
        try{
            
            FileOutputStream fout = new FileOutputStream("A:/Vs Code workspace/MyWorkSpace/javapractice/My.txt");
            String s = "Welcome to Computer's World";
            byte[] b = s.getBytes();
            fout.write(b);
            fout.close();
            System.out.println("File Wrriting is over");

        }
        catch(Exception e){
            System.out.println(e);
        }

    }
}