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

public class PrefixCalculatorTest
{
    @Test
    public void testBasic()
    {
        PrefixCalculator calc = new PrefixCalculator();

        String exp = "+ 5 x 10 4";
        assertEquals("Did not evaluate correctly", 45, calc.evaluate(exp));
    }
}
