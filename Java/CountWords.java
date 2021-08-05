public class CountWords {
    public static int countWords(String str){
        if(str.length() != 0){
            int count = 1;
            for(int i = 0;i < str.length();i++){
                if(str.charAt(i) == ' '){
                    count++;
                }
            }
            return count;
        }
        return 0;
    }
    public static void main(String []args){
        int count = countWords("om namah shivay");
        System.out.print(count);
    }
    
}
