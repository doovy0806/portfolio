/*
 * Name:±¸ÇÑ¸ð
 * Student ID: 201412136
 */

public class PostfixCalculator
{

   /*
    * Instance variables
    *
    * You should not add anything here or change the existing ones.
    *
    * You do not need to use all of these
    */
    Queue<String> sq;
    Queue<Integer> iq;
    Stack<String> ss;
    Stack<Integer> is;

    /*
     * Constructor for the StackSolver
     *
     * Initialize the instance variables to their default values
     * You do not have to initialize variables you will not use
     */
    public PostfixCalculator()
    {
       sq = new Queue<String>();
       iq = new Queue<Integer>();
       ss = new Stack<String>();
       is = new Stack<Integer>();

    }


    /*
     * evaluate
     *
     * Evaluate the expression and return the result
     *
     * exp - String; the string representation of the postfix expression
     *
     * Note: We guarantee exp will always be a valid postfix expression of
     *       length >= 1. Only operators +, -, and * will be used and only
     *       non-negative integers will be used as terms. Terms and operators
     *       will be separated by spaces, for example "5 3 x". At no point in
     *       the evaluation
      *      will an intermediate value be large enough to
     *       overflow the Java int type. However, it can go below 0.
     */
    public int evaluate(String exp)
    {
     String[] expAr= exp.split(" ");
     int expLength = expAr.length;
     for(int i=0; i< expLength;i++){
         try{
             is.push(Integer.parseInt(expAr[i]));
             is.toString();
         }catch(Exception e){
             if (expAr[i].equals("x")){
                 is.push(is.pop()*is.pop());
                 is.toString();
             }else if(expAr[i].equals("+")){
                 is.push(is.pop()+is.pop());
                 is.toString();
             }else if(expAr[i].equals("-")){
                 is.push(-(is.pop() - is.pop()));
             }
         }

        }
     return is.pop();
     }
}
