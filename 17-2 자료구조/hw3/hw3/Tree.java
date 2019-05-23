/*
 * Name: 구한모
 * Student ID:2014121136
 */


/*
 * You should NOT import anything else.
 * 
 * For a quick summary of ArrayLists, see https://www.tutorialspoint.com/java/util/java_util_arraylist.htm
 */

import java.lang.Math;
import java.util.ArrayList;


public class Tree<T>
{

    /*
     * Instance variables
     *
     * You may add new instance variables and methods, but you should not
     * modify the variables and methods that are already defined.
     * 
     * size holds the number of elements currently in the tree
     * 
     * k holds the number of children a node can have
     * 
     * root holds the root node of the tree
     */
    private int size, k;
    private Node<T> root;
    private ArrayList<Integer> routeToLast;
    private ArrayList<Node<T>> preorderAL;
    private ArrayList<Node<T>> postorderAL;
    private ArrayList<Node<T>> inorderAL;
    private ArrayList<Node<T>> convertToAL;
    private Node<T>[] convertArr;
    /*
     * Constructor for the tree
     *
     * Initialize the instance variables to their default values
     * 
     * The default value for k is 2, meaning it is a binary tree
     */
    public Tree()
    {
        this.k =2;
        this.size = 0;

        this.routeToLast = new ArrayList();
        this.postorderAL = new ArrayList<>();
        this.preorderAL = new ArrayList<>();
        this.inorderAL = new ArrayList<>();



    }

    /*
     * Constructor for the tree
     *
     * k - int; the number of children a node can have
     * 
     * Note: If k = 2, it is considered a binary tree
     * 
     * Note: k will always be an integer greater than or equal to 2.
     *       You do not have to consider edge cases where an invalid
     *       value for k is passed as an input.
     */
    public Tree(int k)
    {
        this.k = k;
        this.size = 0;

        this.routeToLast = new ArrayList();
        this.postorderAL = new ArrayList<>();
        this.preorderAL = new ArrayList<>();
        this.inorderAL = new ArrayList<>();

    }

    public void router(int treeSize){
        int adParent;
        int adTemp = treeSize-2;
        if(adTemp>=0) {
            routeToLast.clear();
            while (adTemp > -1) {
                int r = adTemp%k;
                this.routeToLast.add(0, r);
                this.routeToLast.toString();
                adParent = adTemp / k - 1;
                adTemp = adParent;
            }
        }
    }

    public Node<T> lastParentLocater(){
        Node<T> tempParent = this.root;
        for(int i=0; i<routeToLast.size()-1 ; i++){
            tempParent.getData();
            tempParent = tempParent.children.get(this.routeToLast.get(i));
            tempParent.getData();
        }
        return tempParent;
    }

    /*
     * insert
     *
     * Insert the data into the next available position
     *
     * data - T; the data to be inserted
     *
     * Note: The data should be inserted into the next available slot.
     *       Remember that the tree must always be complete, meaning
     *       each level must be full before starting on a new level and
     *       nodes are always added from left to right
     */
    public void insert(T data)
    {

        int adTemp = this.size;
        int adParent;
        //나머지가 0~k-1일때는 부모와의 관계에서 어디있는지,


        if(this.size==0){
            this.root = new Node<>(data, null, this.k);
            //            this.root.data = data;
            this.size=1;

        }else if(this.size > k) {
            //만약 this.routeToLast의 size에 맞는 원소가 있으면 새로 설정 - 넣어줘야함.
            this.router(this.size+1);

            this.lastParentLocater().addChild(data);
            this.size++;

        }else if(this.size <= k){
            this.root.addChild(data);
//            this.routeToLast.clear();
//            while(adTemp>-1){
//                this.routeToLast.add(0,adTemp%k);
//                adParent = (adTemp-1)/k -1;
//                adTemp = adParent;
//            }
            this.size++;
            router(this.size);
        }


    }


    /*
     * remove
     *
     * Remove the "last" node in the tree
     * 
     * Note: The tree must always be complete, so you this method should
     *       remove the right most node in the lowest level of the tree.
     */
    public void remove()
    {

        if(this.size==1){
            this.root=null;
            this.size=0;
        }else if( this.routeToLast.size()>1){
            lastParentLocater().removeChild();
            this.size--;
            this.router(this.size);
        }
    }

    /*
     * preorder
     *
     * Return an arraylist of the nodes in the tree in preorder traversal order
     * 
     * Note: This should be implemented for all values of k.
     * 
     * Note: If the tree is empty, return null.
     */
    public ArrayList<Node<T>> preorder() {
        if (this.size == 0) return null;
        else {
            preorderAL.clear();
            preorderVisit(this.root);

            return preorderAL;

        }
    }
    public void preorderVisit(Node<T> n) {
        preorderAL.add(n);

        for(int i =0; i<n.children.size() ; i++){
            preorderVisit(n.children.get(i));
        }

    }
    /*
     * postorder
     *
     * Return an arraylist of the nodes in the tree in postorder traversal order
     * 
     * Note: This should be implemented for all values of k.
     * 
     * Note: If the tree is empty, return null.
     */
    public ArrayList<Node<T>> postorder()
    {
        if(this.size == 0) return null;
        else {
            postorderAL.clear();
            postorderVisit(this.root);
            return postorderAL;
        }
    }
    public void postorderVisit(Node<T> n) {

        for(int i =0; i<n.children.size() ; i++){
            postorderVisit(n.children.get(i));
        }
        postorderAL.add(n);

    }
    /*
     * inorder
     *
     * Return an arraylist of the nodes in the tree in inorder traversal order
     * 
     * Note: This should be implemented only for binary trees. If the
     *       tree is not a binary tree, you should return null.
     * 
     * Note: If the tree is empty, return null.
     */
    public ArrayList<Node<T>> inorder()
    {
        if(k!=2 || this.size ==0)
        return null;
        else{
            inorderAL.clear();
            inorderVisit(this.root);
        }
        return inorderAL;
    }
    public void inorderVisit(Node<T> n){

        if (!n.getChildren().isEmpty()){
            n.children.get(0).getData();
            inorderVisit(n.children.get(0));
        }
        inorderAL.add(n);
        if(n.children.size()==2){
            inorderVisit(n.children.get(1));
        }

    }

    /*
     * convertToArrayList
     *
     * Return an ArrayList representing the tree.
     * 
     * Note: See page 19 of Lecture 5 for information.
     * 
     * Note: This should be implemented for all values of k. For example,
     *       the children of a node at index i in a k-ary tree should
     *       be stored from index k*i+1 to index k*i+k. The root should be
     *       at index 0.
     * 
     * Note: If the tree is empty, return null.
     * 
     */
    public ArrayList<Node<T>> convertToArrayList()
    {
        convertToAL = new ArrayList<>(this.size);
        convertArr = new Node[this.size];
        int tempAddress = 0;
        converToVisit(this.root, 0);
        for(int i=0; i<this.size; i++){
            convertToAL.add(convertArr[i]);
        }
        return convertToAL;

    }
    public void converToVisit(Node<T> n,int tempAddress){
        //nIndex는 array식으로의 index
//        convertToAL.add(tempAddress, n);
        convertArr[tempAddress] = n;
        for(int i =0; i<n.children.size();i++){
            converToVisit(n.children.get(i), tempAddress*k+i+1);
        }
    }

    /*
     * getSize
     *
     * Return the number of elements in the tree
     */
    public int getSize()
    {
        return this.size;
    }

    /*
     * clear
`     *
     * Clear the tree
     */
    public void clear()
    {
        this.root.children.clear();
        this.size=0;
        this.root.data=null;
    }

    /*
     * contains
     * 
     * data - T; the data to be searched for
     *
     * Return true if there is a node in the tree with the specified data and
     * false otherwise.
     */
    public boolean contains(T data)
    {
        if (cont(this.root, data)) return true;
        else return false;
    }
    public boolean cont(Node<T> n, T data){

        boolean rebool = false;
        for(int i=0; i<n.children.size(); i++){
            if(n.getChildren().get(i).getData().equals(data)) rebool =true;
            else if(n.children.size()>0) {
               rebool = rebool || cont(n.children.get(i), data);
            }
        }

        return rebool;
    }

    /*
     * getDepth
     *
     * Return the number of levels in the tree.
     * 
     * Note: The root node counts as one level. The only tree with depth
     *       equal to 0 is the empty tree.
     */
    public int getDepth()
    {
//        double doubleSize = (double)this.size;
//        double depthClose;
//        int depth;
//        double value;
//        value = Math.log(doubleSize*((double)k-1)-k)/Math.log((double)k) +1;
//        depthClose = Math.floor(value);
//        depth = (int)depthClose;
        if(this.size == 0) return 0;
        else if(this.size ==1 )return 1;
        else {
            return routeToLast.size()+1;
        }
    }

    /*
     * isPerfect
     *
     * Return true if the tree is currently perfect and false otherwise.
     * 
     * Note: A perfect tree is a complete binary tree where all of the levels
     *       are full. In other words, inserting a node into this tree would
     *       force it to begin another level.
     * 
     * Note: The empty tree is perfect.
     */
    public boolean isPerfect()
    {
        int depth = this.getDepth();
        int completeSize =(int)( Math.round((Math.pow(k,depth)-1)/(k-1)));

        if (this.size == completeSize ) return true;
        else  return false;
    }

    /*
     * getLast
     *
     * Return the right most node in the lowest level of the tree
     * 
     * Note: If the tree is empty, return null.
     */   
    public Node<T> getLast()
    {


        if (this.size==0)return null;
        else if(this.size==1){
            return this.root;
        }
        else{Node<T> lastParent = lastParentLocater();
            return lastParent.children.get(lastParent.children.size()-1);

        }

    }

    /*
     * getRoot
     *
     * Return the root of the tree
     */   
    public Node<T> getRoot()
    {
        return this.root;
    }

    /*
    * You should NOT change anything below this line.
    * 
    * Pay close attention to what has been implemented already and
    * what you need to implement on your own (in the Tree class).
    */
    public class Node<T>
    {
        private T data;
        private Node<T> parent;
        private ArrayList<Node<T>> children;
        //This arraylist contains the children of the node in order from left to right

        public Node(T data, Node<T> parent, int k)
        {
            this.parent = parent;
            this.data = data;
            children = new ArrayList<Node<T>>(k);
        }

        public Node<T> getParent()
        {
            return this.parent;
        }

        public T getData()
        {
            return this.data;
        }

        public ArrayList<Node<T>> getChildren()
        {
            return children;
        }
        
        /*
         * This will append to the end of the children arraylist.
         * You need to perform the bounds checks yourself for when
         * the node has the maximum amount of children.
         */
        public void addChild(T data)
        {
            children.add(new Node<T>(data, this, k));
        }

        /*
         * This will remove the right most child of the current node,
         * if it exists.
         */
        public void removeChild()
        {
            if(children.size() > 0)
                children.remove(children.size()-1);
        }

        public void setParent(Node<T> n)
        {
            parent = n;
        }

        public void clearParent()
        {
            parent = null;
        }
    }
}