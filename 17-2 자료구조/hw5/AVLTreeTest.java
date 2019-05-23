import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.AfterClass;

public class AVLTreeTest
{
    AVLTree t;

    @Test(timeout=1000)
    public void testBasic()
    {
        t = new AVLTree();
        t.insert(3);
        t.insert(5);
        t.insert(10);
        assertTrue("contains is wrong (1)", t.contains(3));
        assertTrue("contains is wrong (2)", t.contains(5));
        t.remove(3);
        assertFalse("contains is wrong after removal (1)", t.contains(3));
        assertTrue("contains is wrong after removal (2)", t.contains(10));
        
        System.out.println("Tests passed");
    }

}