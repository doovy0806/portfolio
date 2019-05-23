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

public class QueueTest
{
    @Test
    public void testBasic()
    {
        Queue<Integer> q = new Queue<Integer>();

        q.enqueue(3);
        assertEquals("Didn't enqueue correctly (1)", Integer.valueOf(3), q.peek());
        q.enqueue(5);
        assertEquals("Didn't enqueue correctly (2)", Integer.valueOf(3), q.peek());
        q.dequeue();
        assertEquals("Didn't dequeue correctly (3)", Integer.valueOf(5), q.peek());
    }

    @Test
    public void testCapacity()
    {
        Queue<String> q = new Queue<String>(2);

        q.enqueue("a");
        assertEquals("Didn't enqueue correctly (1)", String.valueOf("a"), q.peek());
        q.enqueue("b");
        assertEquals("Didn't enqueue correctly (2)", String.valueOf("a"), q.peek());
        q.enqueue("c");
        assertEquals("Didn't enqueue correctly (3)", String.valueOf("b"), q.peek());
        q.dequeue();
        assertEquals("Didn't enqueue correctly (4)", String.valueOf("c"), q.peek());
        q.enqueue("d");
        assertEquals("Didn't enqueue correctly (5)", String.valueOf("c"), q.peek());
    }
}
