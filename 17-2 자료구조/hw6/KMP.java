/*
 * Name: ±¸ÇÑ¸ð
 * Student ID: 2014121136
 */

import java.util.ArrayList;
/*
 * You should NOT import anything else.
 * 
 * For a quick summary of ArrayLists, see https://www.tutorialspoint.com/java/util/java_util_arraylist.htm
 */
public class KMP
{
    /*
    * Instance variables
    * You should not add any instance variables here
    *
    * failure - int[] - holds the failure function for the KMP algorithm
    */
    private int[] failure;
    private String pattern;

    /*
    * Constructor
    *
    * Initalize the instance variables here
    */
    public KMP(String pattern)
    {
        this.pattern = pattern;
        setFailure(pattern);

    }

    /*
    * getFailure
    *
    * return the failure function array
    */
    public int[] getFailure()
    {
        return this.failure;
    }

    /*
    * getPattern
    *
    * return the current pattern
    */
    public String getPattern()
    {
	return this.pattern;
    }

    /*
    * setFailure
    *
    * Make a new failure function for the new pattern
    *
    * pattern - string - the new pattern for the KMP algorithm
    */
    public void setFailure(String pattern)
    {
        int plength = pattern.length();
        failure = new int[plength];
        char[] pChar = pattern.toCharArray();

        failure[0] =0;
        int i =1;
        int j=0;

        while(i<plength){
            boolean iBigLetter = (pChar[i]<='Z')&&(pChar[i]-pChar[j]!='A'-'a');
            boolean jBigLetter = (pChar[j]<='Z')&&(pChar[j]-pChar[i]!='A'-'a');
            if(pChar[i]==pChar[j] || pChar[i] =='*' || pChar[j] == '*'  ||iBigLetter || jBigLetter){
                failure[i] = j+1;
                i = i+1;
                j = j+1;
            }else if(j>0){
                j = failure[j-1];
            }else {
                failure[i] = 0;
                i = i+1;
            }
        }

    }

    /*
    * match
    *
    * output whether or not the input string matches the pattern exactly
    *
    * input - string - the string to test
    */
    public boolean match(String input)
    {
        int i =0;
        int j = 0;
        char[] inputChar = input.toCharArray();
        char[] patternChar = pattern.toCharArray();
        int pLength = pattern.length();
        int iLength = input.length();
        while(i<iLength){
            boolean iBigLetter = (inputChar[i]<='Z')&&(inputChar[i]-patternChar[j]!='A'-'a');
            boolean jBigLetter = (patternChar[j]<='Z')&&(patternChar[j]-inputChar[i]!='A'-'a');
            if(inputChar[i]==patternChar[j] || inputChar[i] =='*' || patternChar[j] == '*'
                    ||iBigLetter || jBigLetter){
                if(j==pLength-1) return true;
                else{
                    i++; j++;
                }
            }else{
                if(j>0) j=failure[j-1];
                else i++;
            }
        }
        return false;
    }

    /*
    * getMatchesInString
    *
    * return an arraylist of all indices in input where a substring
    * that matches our pattern ends
    *
    * input - string - the string to test
    */
    public ArrayList<Integer> getMatchesInString(String input)
    {
        ArrayList<Integer> returnList = new ArrayList<>();

        int i =0;
        int j = 0;
        char[] inputChar = input.toCharArray();
        char[] patternChar = pattern.toCharArray();
        int pLength = pattern.length();
        int iLength = input.length();
        while(i<iLength){
            boolean iBigLetter = (inputChar[i]<='Z')&&(inputChar[i]-patternChar[j]!='A'-'a');
            boolean jBigLetter = (patternChar[j]<='Z')&&(patternChar[j]-inputChar[i]!='A'-'a');
            if(inputChar[i]==patternChar[j] || inputChar[i] =='*' || patternChar[j] == '*'
                    ||iBigLetter || jBigLetter){
                if(j==pLength-1) {
                    returnList.add(i);
                    j=failure[j-1];

                }
                else{
                    i++; j++;
                }
            }else{
                if(j>0) j=failure[j-1];
                else i++;
            }
        }
        return returnList;
    }

    /*
    *  countMatchesInString
    *
    * return the number of substrings of the input string that match
    * our pattern
    *
    * input - string - the string to test
    */
    public int countMatchesInString(String input)
    {
        int i =0;
        int j = 0;
        int count = 0;
        char[] inputChar = input.toCharArray();
        char[] patternChar = pattern.toCharArray();
        int pLength = pattern.length();
        int iLength = input.length();
        while(i<iLength){
            boolean iBigLetter = (inputChar[i]<='Z')&&(inputChar[i]-patternChar[j]!='A'-'a');
            boolean jBigLetter = (patternChar[j]<='Z')&&(patternChar[j]-inputChar[i]!='A'-'a');
            if(inputChar[i]==patternChar[j] || inputChar[i] =='*' || patternChar[j] == '*'
                    ||iBigLetter || jBigLetter){
                if(j==pLength-1){
                    j=failure[j-1]; count++;
                }
                else{
                    i++; j++;
                }
            }else{
                if(j>0) j=failure[j-1];
                else i++;
            }
        }
        return count;

    }
}
