import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.AfterClass;

public class CuckooHashTest
{
    CuckooHash ch;

    @Test(timeout=1000)
    public void testBasic()
    {
        ch = new CuckooHash(5,5,.85);
        ch.insert(11);
        ch.insert(13);
        ch.insert(1);

        int[] array1 = ch.getArray1();
        int[] array2 = ch.getArray2();
        int a1 = ch.getA1();
        int b1 = ch.getB1();
        int a2 = ch.getA2();
        int b2 = ch.getB2();
        int n = ch.getN();

        assertTrue("hash table is not correct", (array1[hash(a1,b1,n,11)] == 11) ^ (array2[hash(a2,b2,n,11)] == 11));
        assertTrue("hash table is not correct", (array1[hash(a1,b1,n,13)] == 13) ^ (array2[hash(a2,b2,n,13)] == 13));
        assertTrue("hash table is not correct", (array1[hash(a1,b1,n,1)] == 1) ^ (array2[hash(a2,b2,n,1)] == 1));

        System.out.println("Tests passed");
    }

    public int hash(int a, int b, int n, int x)
    {
        return (a*x+b)%n;
    }

}
