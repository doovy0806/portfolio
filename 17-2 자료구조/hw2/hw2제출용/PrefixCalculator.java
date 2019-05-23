/*
 * Name:±¸ÇÑ¸ð
 * Student ID:2014121136
 */

public class PrefixCalculator
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
     * Constructor for the QueueSolver
     *
     * Initialize the instance variables to their default values
     * You do not have to initialize variables you will not use
     */
    public PrefixCalculator()
    {
        sq = new Queue<String>();
        iq = new Queue<Integer>();
        ss = new Stack<String>();
        is = new Stack<Integer>();

    }

    /*
     * solve
     *
     * Evaluate the expression and return the result
     *
     * exp - String; the string representation of the prefix expression
     *
     * Note: We guarantee exp will always be a valid prefix expression of
     *       length >= 1. Only operators +, -, and x will be used and only
     *       non-negative integers will be used as terms. Terms and operators
     *       will be separated by spaces, for example "+ 5 3". At no point in
     *       the evaluation will an intermediate value be large enough to
     *       overflow the Java int type. However, it can go below 0.
     */
    public int evaluate(String exp)
    {
        boolean beforeNum = false;
        String[] expAr= exp.split(" ");
        int expLength = expAr.length;
        for(int i=0; i< expLength;i++){
            try{
                is.push(Integer.parseInt(expAr[i]));

                if(is.getSize()>1&&beforeNum){

                    if(ss.peek().equals("x")){
                        ss.pop();
                        is.push(is.pop()*is.pop());
                        beforeNum=true;

                    }else if(ss.peek().equals("+")){
                        ss.pop();
                        is.push(is.pop()+is.pop());
                        beforeNum=true;

                    }else if(ss.peek().equals("-")){
                        ss.pop();
                        is.push(-(is.pop()-is.pop()));
                        beforeNum=true;

                    }

                }else beforeNum = true;
            }catch(Exception e){
                if (expAr[i].equals("x")){
                    ss.push(expAr[i]);
                    beforeNum = false;
                }else if(expAr[i].equals("+")){
                    ss.push(expAr[i]);
                    beforeNum = false;
                }else if(expAr[i].equals("-")){
                    ss.push(expAr[i]);
                    beforeNum = false;
                }
            }

        }
        while(!ss.isEmpty()) {
            if (ss.peek().equals("x")) {
                ss.pop();
                is.push(is.pop() * is.pop());
                beforeNum = true;

            } else if (ss.peek().equals("+")) {
                ss.pop();
                is.push(is.pop() + is.pop());
                beforeNum = true;

            } else if (ss.peek().equals("-")) {
                ss.pop();
                is.push(-(is.pop() - is.pop()));
                beforeNum = true;
            }
        }

        return is.pop();
    }
}