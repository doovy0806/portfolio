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

public class SorterTest
{
    @Test(timeout=100)
    public void testBasic()
    {
        Sorter s = new Sorter();
        int[] test = {2,3,1,4};
        int[] expectedAscending = {1,2,3,4};
        int[] expectedDescending = {4,3,2,1};
        test = s.ascending(test);
        assertArrayEquals(test, expectedAscending);
        test = s.descending(test);
        assertArrayEquals(test, expectedDescending);
    }
}
