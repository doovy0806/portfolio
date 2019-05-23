/*
 * Feel free to add your own tests here.
 *
 * You can find a tutorial on junit at
 *     https://www.tutorialspoint.com/junit/index.htm
 */

import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.AfterClass;

public class LinkedListTest
{
    @Test
    public void testBasic()
    {
        LinkedList<String> ll = new LinkedList<String>();
        
        ll.insertAtHead("Data");
        ll.insertAtTail("Structures");
        ll.insert(2, "is the best class");

        assertTrue(ll.contains("Data"));
        assertFalse(ll.contains("is the worst class"));
    }
}
