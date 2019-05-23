/*
 * Name: 구한모
 * Student ID: 2014121136
 */

import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.Iterator;
import java.util.ArrayList;
/*
 * You should NOT import anything else.
 * 
 * For a quick summary of ArrayLists, see https://www.tutorialspoint.com/java/util/java_util_arraylist.htm
 * For a summary of HashMaps, Iterators, and HashSets please see the handout.
 */

public class Trie
{

    /*
    * Instance variables
    * You should not add any instance variables here
    *
    * root - TrieNode - holds the root of the trie
    * numWords - int - the number of words currently stored in the trie
    */
    private TrieNode root;
    private int numWords;


    /*
    * Constructor
    * Initalize the instance variables here
    *
    * root should always exist (and is not an output node by default)
    */
    public Trie()
    {
        this.root = new TrieNode(false);
        this.numWords = 0;

    }

    /*
    * insert
    *
    * Insert a string into the trie.
    * 
    * s - string - the string to be inserted
    */
    public void insert(String s)
    {
        char[] sChar = s.toCharArray();
        int sLength = s.length();
        TrieNode temp = this.root;
        for(int i=0; i<sLength; i++){
            if(!temp.children.containsKey(sChar[i])&&i<sLength-1){
                temp = temp.addTransition(sChar[i]);

            }else if(!temp.children.containsKey(sChar[i])&&i==sLength-1){
                temp = temp.children.put(sChar[i], new TrieNode(true));
            }else if(temp.children.containsKey(sChar[i])&&i==sLength-1){
                temp = temp.getTransition(sChar[i]);
                temp.setOutput(true);
            }else if(temp.children.containsKey(sChar[i])&&i<sLength-1){
                temp = temp.getTransition(sChar[i]);
            }
        }
        numWords++;
        //마지막 노드가 있는경우도 생각해야 -> output을 바꿔야 함!

    }

    /*
    * insertMany
    *
    * Insert all strings from a list into the trie.
    * 
    * strings - String[] - the strings to be inserted
    */
    public void insertMany(String[] strings)
    {
        for(int i=0; i<strings.length; i++){
            this.insert(strings[i]);
        }

    }

    /*
    * contains
    *
    * Return whether or not a given string is stored in the trie
    * 
    * s - string - the string to be checked
    */
    public boolean contains(String s)
    {
        char[] charArr = s.toCharArray();

        TrieNode temp = this.root;
        TrieNode current = null;
        for(int i=0; i<s.length(); i++){
            if(i<s.length()-1 &&temp.getTransition(charArr[i])!=null){
                temp = temp.getTransition(charArr[i]);
            }else if(i==s.length()-1 && temp.getTransition(charArr[i])!=null){
             // when the method reaches end of s,
                temp = temp.getTransition(charArr[i]);
                if(temp.getOutput()) return true;
                else return false;
            }else return false;
        }
        return true;
        //?
    }

    /*
    * remove
    *
    * Remove a given string from the trie (if it is contained in the trie)
    * 
    * s - string - the string to be removed
    */
    public void remove(String s)
    {
        // s의 길이를 받아서 char로 반환, 그 char경로따라 trienode 배열도 받아서 인덱스에 차례대로 넣음
        // 끝인덱스부터 children이 비어있으면 삭제(->null로 바꿈), 차례로 올라오다가 마지막 children이 없는 노드까지삭제
        // 만약 가장 끝 노드가 children이 있으면 output을 false로 - 근데 이미 output이 false면 그냥 리턴
        if(contains(s)) {

            char[] charArr = s.toCharArray();
            int sLength = s.length();
            TrieNode[] sNodeArr = new TrieNode[sLength];
            TrieNode temp = this.root;
            for (int i = 0; i < sLength; i++) {
                temp = temp.getTransition(charArr[i]);
                sNodeArr[i] = temp;
            }
            if(!sNodeArr[sLength-1].getChildren().isEmpty()){
                if(sNodeArr[sLength-1].getOutput()){
                    sNodeArr[sLength-1].setOutput(false);
                }else return; // 마지막 노드가 children이 있는데 output이 false인 경우 - 즉 존재하지않음
            }else {//마지막 노드가 children이 없는 경우 - children 있는 temp나올때까지 쭉 null로 삭제
                for (int i = 0; i < sLength; i++) {
                    if (i!=sLength-1&&sNodeArr[sLength-1-i].getChildren().isEmpty()){
                        //앞 인덱스의 children에서 key가 해당되는 trienode를 없애버린다
                        sNodeArr[sLength-2-i].children.remove(charArr[sLength-1-i]);
                    }else if(i!=sLength-1&&sNodeArr[sLength-1-i].getChildren().isEmpty()){
                        //다 children없고 root 의 children마저 children이 없게 된 경우
                        this.root.children.remove(charArr[0]);
                    }else{ // children이 있는 노드가 발견된 경우
                        return;
                    }
                }
            }
        }
    }

    /*
    * getMatchesInString
    *
    * Return an arraylist containing all indices of the input string where a substring
    * contained in the trie ends
    * 
    * input - string - the string to be tested
    */
    public ArrayList<Integer> getMatchesInString(String input)

    {
        //아직 음 중간에 동시에 다른 단어를 같이 체킹하는 것 까지는 구현하지 않고 하나씩만..
        ArrayList<Integer> returnList = new ArrayList<>();
        ArrayList<TrieNode> nodeList = new ArrayList<>();
        int iLength = input.length();

        char[] inputChar = input.toCharArray();
        TrieNode[] matchArr = new TrieNode[iLength];
        for(int i=0; i<iLength; i++){
            if(this.root.children.containsKey(inputChar[i])){
                matchArr[i] = this.root.getTransition(inputChar[i]);
                if(matchArr[i].output){
                    if(!returnList.contains(i)){
                        returnList.add(i);
                    }
                }
            }else{
                matchArr[i] = null;
            }
            for(int j=0; j<i; j++){
                if(matchArr[j]!=null){
                    if(matchArr[j].children.containsKey(inputChar[i])){
                        matchArr[j] = matchArr[j].getTransition(inputChar[i]);
                        if(matchArr[j].output){
                            if(!returnList.contains(i)){
                                returnList.add(i);
                            }
                        }
                    }else{
                        matchArr[j] =null;
                    }
                }
            }
        }

        return returnList;
    }

    /*
    * countMatchesInString
    *
    * Return the number of substrings in the input string that are contained in the trie
    * 
    * input - string - the string to be tested
    */
    public int countMatchesInString(String input)
    {
        int totalCounts = 0;
        int iLength = input.length();
        char[] inputChar = input.toCharArray();
        TrieNode[] matchArr = new TrieNode[iLength];
        for(int i=0; i<iLength; i++){
            if(this.root.children.containsKey(inputChar[i])){
                matchArr[i] = this.root.getTransition(inputChar[i]);
                if(matchArr[i].output){
                    totalCounts++;
                }
            }else{
                matchArr[i] = null;
            }
            for(int j=0; j<i; j++){
                if(matchArr[j]!=null){
                    if(matchArr[j].children.containsKey(inputChar[i])){
                        matchArr[j] = matchArr[j].getTransition(inputChar[i]);
                        if(matchArr[j].output){
                            totalCounts++;
                        }
                    }else{
                        matchArr[j] =null;
                    }
                }
            }
        }



        return totalCounts;
    }


    /*
    * getRoot
    *
    * Return the root of the trie
    */
    public TrieNode getRoot()
    {
        return this.root;
    }

    class TrieNode
    {
        /*
        * TrieNode instance variables. You should not add any instance variables.
        *
        * children - HashMap<Character, TrieNode> - the outgoing transitions (mapped by character) of the node
        * output - boolean - whether or not the node is an output node
        */
        public HashMap<Character, TrieNode> children;
        public boolean output;

        /*
        * TrieNode constructor
        *
        * output - boolean - whether or not the node is an output node
        */
        public TrieNode(boolean output)
        {
            this.output = output;
            this.children = new HashMap<>();

        }

        /*
        * getOutput
        *
        * return the output instance variable
        */
        public boolean getOutput()
        {
            return this.output;
        }

        /*
        * getChildren
        *
        * return the children instance variable
        */
        public HashMap<Character, TrieNode> getChildren()
        {
            return children;
        }

        /*
        * setOutput
        *
        * set the output variable
        */
        public void setOutput(boolean output)
        {
            this.output = output;

        }

        /*
        * addTransition
        *
        * construct a new TrieNode and add a transition to it from the current node
        *
        * if the transition label already exists in children, you should just return null
        * without changing anything
        *
        * c - char - the transition label to add
        */
        public TrieNode addTransition(char c)
        {
            if(!children.containsKey(c)){
                children.put(c, new TrieNode(false));
                return children.get(c);
            }

            else return null;
        }

        /*
        * getTransition
        *
        * Return the TrieNode in children mapped to by c (or null if it does not exist).
        */
        public TrieNode getTransition(char c)
        {
            if(children.containsKey(c)){
                return children.get(c);
            }else return null;
        }
    }
}