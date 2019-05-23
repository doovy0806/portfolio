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

public class TrieTest
{
    @Test
    public void testBasic()
    {
        Trie t = new Trie();
        
        t.insert("yonsei");
        t.insert("data");
        t.insert("structures");
        t.insert("yon");

        assertTrue("contains is wrong (1)", t.contains("yonsei"));
        assertTrue("contains is wrong (2)", t.contains("yon"));
        assertFalse("contains is wrong (3)", t.contains("korea"));

        System.out.println("all tests passed");
        System.out.println("you should add your own tests!");
    }
}
