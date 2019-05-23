/*
 * Name: ±¸ÇÑ¸ð
 * Student ID: 2014121136
 */


public class Queue<T>
{

    /*
     * Instance variables
     *
     * You should not add anything here or change the existing ones.
     *
     * Capacity holds the value for the maximum number of elements
     * allowed in the queue at any time. If capacity is -1, the queue
     * can hold an unlimited amount of elements. Capacity will always be
     * either -1 or a positive integer (never 0).
     */
    private LinkedList<T> ll;
    private int capacity;

    /*
     * Constructor for the Queue
     *
     * Initialize the instance variables to their default values
     *
     * The default value for capacity is -1
     */
    public Queue()
    {
        this.capacity = -1;
        ll = new LinkedList<>();
    }

    /*
     * Constructor for the Queue
     *
     * Initialize the instance variables
     *
     * Note: Capacity will always be either -1 or a positive integer (not 0)
     * You do not have to worry about incorrect capacity values being passed
     */
    public Queue(int capacity)
    {
        this.capacity = capacity;
        ll = new LinkedList<>();
    }

    /*
     * peek
     *
     * return the value at the front of the queue
     *
     * Note: Return null if the queue is empty. This should not
     *       remove the element from the front of the queue.
     */
    public T peek()
    {
        if(ll.getSize()>0){
            int llSize = ll.getSize();
            return ll.getData(0);

        }else return null;
    }

    /*
     * dequeue
     *
     * return and remove the value at the front of the queue
     *
     * Note: Return null if the queue is empty.
     */
    public T dequeue()
    {
        T t;
        if(ll.getSize()>0){
            int llSize = ll.getSize();
            t = ll.getData(0);
            ll.remove(0);

            return t;

        }else return null;
    }

    /*
     * enqueue
     *
     * enqueue data to the back of the queue
     *
     * data - T; The data to be added to the queue
     *
     * Note: If the queue is full, you should remove the element at the front
     * of the queue before adding the new data
     */
    public void enqueue(T data)
    {
        if (ll.getSize() < this.capacity || this.capacity==-1){
            ll.insert(ll.getSize(),data);
        }else {
            ll.remove(0);

            ll.insert(ll.getSize(),data);
        }

    }

    /*
     * clear
     *
     * empty the queue
     */
    public void clear()
    {
        int llSize = ll.getSize();
        for(int i =0; i<llSize;i++){
            ll.remove(0);
        }
    }

    /*
     * isEmpty
     *
     * return true if there are no elements in the queue and false otherwise
     */
    public boolean isEmpty()
    {

        return (ll.getSize()==0)? true:false;
    }

    /*
     * isFull
     *
     * return true if the queue is at maximum capacity and false otherwise
     */
    public boolean isFull()
    {
        return (ll.getSize()==this.capacity)?true : false;
    }

    /*
     * getSize
     *
     * return the number of elements in the queue
     */
    public int getSize()
    {
        return ll.getSize();
    }

    /*
     * toString
     *
     * You do not have to implement this method, it is just to help you debug.
     * When you submit your assignment, your code should never print anything
     * meaning it should not have any System.out.println.
     * If it does you will get an automatic 0 as this breaks the autograder.
     */
    public String toString()
    {
        return ll.toString();
    }
}