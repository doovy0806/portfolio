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

public class TreeTest
{
    @Test
    public void testBasic()
    {
        Tree<Integer> t = new Tree<Integer>(); //test binary tree
        t.insert(1);
        assertEquals("Root not set properly (1)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (1)", Integer.valueOf(1), t.getLast().getData());
        assertEquals("getDepth wrong (1)", 1, t.getDepth());
        t.insert(2);
        assertEquals("Root not set properly (2)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (2)", Integer.valueOf(2), t.getLast().getData());
        t.insert(3);
        assertEquals("Root not set properly (3)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (3)", Integer.valueOf(3), t.getLast().getData());
        t.insert(4);
        assertEquals("Root not set properly (4)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (4)", Integer.valueOf(4), t.getLast().getData());

        assertEquals("getDepth wrong (2)", 3, t.getDepth());

        t.remove();
        assertEquals("Root not set properly (5)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (5)", Integer.valueOf(3), t.getLast().getData());

        assertEquals("getDepth wrong (3)", 2, t.getDepth());
    }

    @Test
    public void testBasic2()
    {
        Tree<Integer> t = new Tree<Integer>(3); //test 3-ary tree

        t.insert(1);
        assertEquals("Root not set properly (1)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (1)", Integer.valueOf(1), t.getLast().getData());
        assertEquals("getDepth wrong (1)", 1, t.getDepth());
        t.insert(2);
        assertEquals("Root not set properly (2)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (2)", Integer.valueOf(2), t.getLast().getData());
        t.insert(3);
        assertEquals("Root not set properly (3)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (3)", Integer.valueOf(3), t.getLast().getData());
        t.insert(4);
        assertEquals("Root not set properly (4)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (4)", Integer.valueOf(4), t.getLast().getData());
        t.insert(5);
        assertEquals("Root not set properly (5)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (5)", Integer.valueOf(5), t.getLast().getData());

        assertEquals("getDepth wrong (2)", 3, t.getDepth());

        t.remove();
        assertEquals("getDepth wrong (3)", 2, t.getDepth());
        assertEquals("Root not set properly (6)", Integer.valueOf(1), t.getRoot().getData());
        assertEquals("Last not set properly (6)", Integer.valueOf(4), t.getLast().getData());
    }
}
