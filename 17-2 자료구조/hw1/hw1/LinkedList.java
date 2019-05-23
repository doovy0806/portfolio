/*
 * Name: ±¸ÇÑ¸ð
 * Student ID: 2014121136
 */

/*
 * You should not import anything or change/add any instance variables, methods,
 * or method signatures.
 */
public class LinkedList<T>
{

    private int size;
    private Node<T> head, tail;

    /*
     * Constructor for our Linked List
     *
     * Initialize the instance variables to their default values
     */
    public LinkedList()
    {
        this.head = new Node<>(null);
        this.tail = new Node<>(null);
        head.setNext(this.tail);
        this.size = 2;


    }

    /*
     * insert
     *
     * Insert a new node with the specified data into the specified index
     *
     * index - int; the location in which to insert the new node (indexed
     *              from 0)
     *
     * data - T; the data to be stored in the newly created node
     *
     * Note:  If the index is out of range ([0, size]), nothing should be
     *        inserted.
     */
    public void insert(int index, T data)
    {
        Node<T> newNode = new Node<>(data);
        Node<T> temp = new Node<>(null);
        Node<T> tempPrev = new Node<>(null);
        temp = this.head;
        if(index==0){
            newNode.setNext(this.head);
            this.head = newNode;
            this.size++;
        } else if(index<this.size && index>0) {
            for (int i = 0; i < index; i++) {
                tempPrev = temp;
                temp = temp.getNext();
            }
            newNode.setNext(temp);
            tempPrev.setNext(newNode);
            this.size++;
        }
    }

    /*
     * insertAtHead
     *
     * Insert a new node at the head with the specified data
     *
     * data - T; the data to be stored in the newly created node
     *
     * Note: This should insert even if the list is empty.
     */
    public void insertAtHead(T data)
    {
        Node<T> newNode = new Node<>(data);
        if(this.size == 0){
            this.head = newNode;
            //this. tail = newNode;
            this.size++;
        }else if (this.size>0){
            newNode.setNext(this.head);
            this.head = newNode;
            this.size++;
        }
    }

    /*
     * insertAtTail
     *
     * Insert a new node at the tail with the specified data
     *
     * data - T; the data to be stored in the newly created node
     *
     * Note: This should insert even if the list is empty.
     */
    public void insertAtTail(T data)
    {
        Node<T> temp = new Node<>(null);
        Node<T> newNode = new Node<>(data);
        if(this.size == 0){
            this.tail = newNode;
            this.head = newNode;
            this.size++;

        }else if(this.size>0){
            tail.setNext(newNode);
            this.tail = newNode;
            this.size++;
        }
    }

    /*
     * remove
     *
     * Remove the first node with the specified data, if it exists
     *
     * data - T; the data to find and remove from the list
     *
     * Note: You should use x.equals(y) to compare generic data
     */
    public void remove(T data)
    {
        Node<T> temp = new Node<>(null);
        Node<T> tempPrev = new Node<>(null);
        temp = this.head;
        int index =0;
        for( ; index < this.size ; index++){
            if(index == 0 && data.equals(temp.getData())){
                this.head = this.head.getNext();
                this.size--;
                break;
            }
            else if(data.equals(temp.getData())){
                tempPrev.setNext(temp.getNext());
                this.size--;
                break;
            }else{
                tempPrev = temp;
                temp = temp.getNext();

            }
        }

    }

    /*
     * removeIndex
     *
     * Remove the node at the specified index
     *
     * index - int; the index to remove from
     *
     * Note: If the index is out of range do nothing
     */
    public void removeIndex(int index)
    {
        Node<T> n = this.head;
        Node<T> nPrev = new Node<>(null);

        if( index < this.size && index >0){
            for(int i=0; i<index ; i++){
                nPrev = n;
                n = n.getNext();
            }
            nPrev.setNext(n.getNext());
            this.size--;

        }else if (index ==0 && this.size > 0){
            this.removeFromHead();
            this.size--;
        }

    }

    /*
     * removeFromHead
     *
     * Remove the head node of the list, if it exists
     */
    public void removeFromHead()
    {
        if(this.size >2) {
            this.head = this.head.getNext();
            this.size--;
        }
        else if(this.size==1){
            this.head = this.tail;
            this.size--;
        }


    }

    /*
     * removeFromTail
     *
     * Remove the tail node of the list, if it exists
     */
    public void removeFromTail() {
            int index = 0;
            Node<T> n = this.head;

        if (this.size > 2) {
            for (index = 1; index < this.size-1; index++){
                n = n.getNext();
            }
            n.setNext(null);
            this.tail = n;
            this.size--;

        }else if(this.size ==2){
            this.head.setNext(null);
            this.size--;
        }
    }

    /*
     * joinLists
     *
     * Append a second list to the current list
     *
     * ll - LinkedList<T>; the linked list to append to the current list
     *
     * Note: This should work even if one or both of the lists are empty
     */
    public void joinLists(LinkedList<T> ll) {
        if (this.size == 0 && ll.size > 0) {
            this.head = ll.head;
            this.tail = ll.tail;
            this.size = ll.size;
        } else if (this.size > 0 && ll.size > 0) {
            this.tail.setNext(ll.head);
            this.tail = ll.tail;
            this.size = this.size + ll.size;
        }
    }

    /*
     * contains
     *
     * Check to see if the list contains a node with the specified data
     *
     * data - T; the data to check for
     *
     * Note: You should use x.equals(y) to compare generic data
     */
    public boolean contains(T data)
    {
        Node<T> n = this.head;
        int index = 0;

            for(index = 0; index<this.size ; index++ ){
                if(data.equals(n.getData())){
                    return true;
                }else{
                    n = n.getNext();
                }
        }
        return false;
    }

    /*
     * getIndex
     *
     * Return the index of the first node in the list with the specified data
     * or -1 if it does not exist
     *
     * data - T; the data to check for
     *
     * Note: You should use x.equals(y) to compare generic data
     */
    public int getIndex(T data)
    {
        Node<T> n = this.head;
        int index = 0;

        for(index = 0; index<this.size ; index++ ){
            if(data.equals(n.getData())){
                return index;
            }else{
                n = n.getNext();
            }
        }
        return -1;
    }

    /*
     * getElementAtIndex
     *
     * Return the node at the specified index or null if it is out of range
     *
     * index - int; the desired index
     */
    public Node<T> getElementAtIndex(int index)
    {
        Node<T> n = this.head;
        int i = 0;

        for(i = 0; i<this.size ; i++ ){
            if(index == i ){
                return n;
            }else{
                n = n.getNext();
            }
        }
        return null;
    }

    /*
     * clear
     *
     * Clear the linked list
     */
    public void clear()
    {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    /*
     * isEmpty
     *
     * Return whether or not the list is empty
     */
    public boolean isEmpty()
    {
        if (this.size ==0){
            return true;
        }else {
        return false;}

    }

    /*
     * getHead
     *
     * Return the head node (possibly null)
     */
    public Node<T> getHead()
    {
        if(this.size>0){
            return this.head;
        }
        else {
        return null;
        }
    }

    /*
     * getTail
     *
     * Return the tail node (possibly null)
     */
    public Node<T> getTail()
    {
        if(this.size>0){
            return this.tail;
        }
        else{
            return null;
        }

    }

    /*
     * getSize
     *
     * Return the number of elements in the linked list
     */
    public int getSize()
    {
        return this.size;
    }

    /*
     * toString
     *
     * Return a string representation of the linked list
     *
     * Note: We will not be grading this, it is only for you to be able to
     *       easily display the contents of a linked list by using something
     *       like "System.out.println(ll);". Remember not to have any printed
     *       output in any of the other methods.
     */
    public String toString()
    {
        return "";
    }

    /*
     * Node<T> class
     *
     * This class describes a generic node object.
     *
     * You should not edit anything below this line but please note exactly what
     * is implemented so that you can use it in your linked list code
     */
    public class Node<T>
    {
        private Node<T> next;
        private T data;

        public Node(T data)
        {
            this.data = data;
        }

        public void setNext(Node<T> next)
        {
            this.next = next;
        }

        public void setData(T data)
        {
            this.data = data;
        }

        public Node<T> getNext()
        {
            return this.next;
        }

        public T getData()
        {
            return this.data;
        }

        public void clearNext()
        {
            this.next = null;
        }
    }
}
