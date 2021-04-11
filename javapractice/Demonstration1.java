import javax.xml.catalog.Catalog;

public class Demonstration1 {
    public static void main(String args[]){
        try{
            int i = args.length;
        
        String myString[] = new String[i];
        myString[0] = args[0];
        
        if(args[0].equals("Java")){
            System.out.println("First word is java");
        }
    
        System.out.println("Number of argument is " + i);
        int x = 12/i;
        int y[] = {555,9991,86};
        y[i] = x;
}
    catch(Exception e){
        System.out.println("division by zero " + e.getMessage());
    }
    
    }
}
