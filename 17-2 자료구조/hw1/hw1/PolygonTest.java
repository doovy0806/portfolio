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

public class PolygonTest
{
    @Test
    public void testBasic()
    {
        Polygon p = new Polygon();
        p.addPoint(new Point(0,0));
        p.addPoint(new Point(1,0));
        p.addPoint(new Point(1,1));
        p.addPoint(new Point(0,1));

        Point testPoint1 = new Point(.5,.5);
        Point testPoint2 = new Point(3,10);

        assertTrue(p.pointInPolygon(testPoint1));
        assertFalse(p.pointInPolygon(testPoint2));
    }
}
