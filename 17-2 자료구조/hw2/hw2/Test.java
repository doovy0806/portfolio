public class Test
{
    public static void main(String[] args)
    {
        LinkedList<Integer> ll = new LinkedList<Integer>();
        ll.insert(0,0);
        System.out.println(ll);
        ll.insert(1,1);
        System.out.println(ll);
        ll.insert(5,100);
        System.out.println(ll);
        ll.insert(2,2);
        System.out.println(ll);
        ll.insert(0,-1);
        System.out.println(ll);
        ll.insert(4,4);
        System.out.println(ll);
        ll.insert(5,5);
        System.out.println(ll);
        ll.remove(5);
        System.out.println(ll);
        ll.remove(0);
        System.out.println(ll);
        ll.remove(190);
        System.out.println(ll);
        ll.remove(2);
        System.out.println(ll);
        ll.remove(1);
        System.out.println(ll);
        
    }
}