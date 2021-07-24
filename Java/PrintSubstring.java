public class PrintSubstring {
    public static void substring(String str){
        substring(str,"");

    }
    public static void substring(String str,String output){
        if(str.length() == 0){
            System.out.println(output);
            return;
        }
        substring(str.substring(1),output); 
        substring(str.substring(1), output + str.charAt(0));
    }
    public static void main(String[] args){
        PrintSubstring.substring("abc");
    }
}
