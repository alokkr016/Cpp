

public class ReturnSubstring {
    public static String[] substring(String str){
        if(str.length() == 0){
            String s[] = {""};
            return s;
        }
        String []smallans = substring(str.substring(1));
        String []finalArray = new String[smallans.length * 2];
        int k = 0;
        for(int i = 0;i < smallans.length;i++){
            finalArray[i] = smallans[i];
            k++;
        }
        for(int i = 0;i < smallans.length;i++){
            finalArray[k + i] = str.charAt(0) + smallans[i];
        }

        return finalArray;

    }
    public static void main(String []args){
        String []str = substring("abc");
        for(int i = 0;i < str.length;i++){
            System.out.println(str[i]);
        }
    }
}
