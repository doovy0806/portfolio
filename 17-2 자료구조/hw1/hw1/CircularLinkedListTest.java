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

public class CircularLinkedListTest
{
    @Test
    public void testBasic()
    {
        CircularLinkedList<Integer> cll = new CircularLinkedList<Integer>();

        cll.insertAtHead(3);
        cll.insertAtTail(-1);
        cll.insert(2, 500);
        
        assertTrue(cll.contains(-1));
        assertFalse(cll.contains(0));
    }
}
