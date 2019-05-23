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

public class StackTest
{
    @Test
    public void testBasic()
    {
        Stack<Integer> s = new Stack<Integer>();

        s.push(3);
        assertEquals("Didn't push correctly (1)", Integer.valueOf(3), s.peek());
        s.push(5);
        assertEquals("Didn't push correctly (2)", Integer.valueOf(5), s.peek());
        s.pop();
        assertEquals("Didn't pop correctly (3)", Integer.valueOf(3), s.peek());
    }
}
