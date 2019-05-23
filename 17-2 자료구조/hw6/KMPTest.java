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

public class KMPTest
{
    @Test
    public void testBasic()
    {
        KMP kmpTester = new KMP("m*rco");
        
        assertTrue("match is wrong (1)", kmpTester.match("marco"));
        assertTrue("match is wrong (2)", kmpTester.match("mbrco"));
        assertTrue("match is wrong (3)", kmpTester.match("mzrco"));
        assertTrue("match is wrong (4)", kmpTester.match("mxrco"));

        assertEquals("countMatchesInString is wrong (1)", 3, kmpTester.countMatchesInString("marcombrcoyonseimcrco"));

        System.out.println("all tests passed");
        System.out.println("you should add your own tests!");
    }
}
