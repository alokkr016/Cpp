public class PrintKeypad {
    public static void printKeys(int n){
        printKeys(n,"");
        
    }
    public static void printKeys(int n,String output){
        if(n == 0){
            System.out.println(output);
            return;
        }
        String keys[] = helper(n%10);
        printKeys(n/10,keys[0] + output);
        printKeys(n/10,keys[1] + output);
        printKeys(n/10,keys[2] + output);
        if(keys.length == 4){
            printKeys(n/10,keys[3] + output);
        }
    }
    public static String[] helper(int n){
        String two[] = {"a","b","c"};
        String three[] = {"d","e","f"};
        String four[] = {"g","h","i"};
        String five[] = {"j","k","l"};
        String six[] = {"m","n","o"};
        String seven[] = {"p","q","r","s"};
        String eight[] = {"t","u","v"};
        String nine[] = {"w","x","y","z"};
        if(n== 2){
            return two;
        }
        else if(n == 3){
            return three;
        }
        else if(n == 4){
            return four;
        }
        else if(n == 5){
            return five;
        }
        else if(n == 6){
            return six;
        }
        else if(n == 7){
            return seven;
        }
        else if(n == 8){
            return eight;
        }
        else if(n == 9){
            return nine;
        }
        else {
            String str[] = {""};
            return str;
        }
    }
    public static void main(String[] args){
        PrintKeypad.printKeys(23);
    }
    
}
