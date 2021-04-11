public class CommandLineInput {
    
        static int anyFunctin(int x,int y){
            try{
                int a = x/y;
                return a;
            }
            catch(ArithmeticException e){
                System.out.println("Division by zero");
               
            }
            return 0;
        }

        public static void main(String[] args){
            int a,b,result = 0;
            a = 0;
            b = 0;
            try{
                a = Integer.parseInt(args[0]);
                b = Integer.parseInt(args[1]);
            }
            catch(Exception e){
                System.out.println(e.getMessage());
            }
            result = anyFunctin(a, b);
            System.out.println(result);
            }
        }