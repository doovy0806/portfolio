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
import java.util.ArrayList;

public class GraphTest
{
    @Test
    public void testBasic()
    {
        Graph g = new Graph();
        for(int i = 0; i < 5; i++)
        {
            g.addNode();
        }
        ArrayList<Node> nodes = g.getNodes();
        g.addEdge(nodes.get(0), nodes.get(1), 3);
        g.addEdge(nodes.get(1), nodes.get(2), 5);
        g.addEdge(nodes.get(3), nodes.get(4), 100);

        assertEquals("shortest path is wrong (1)", 8, g.shortestPathLength(nodes.get(0), nodes.get(2)));
        assertEquals("shortest path is wrong (2)", 100, g.shortestPathLength(nodes.get(3), nodes.get(4)));
        assertFalse("areUVConnected is wrong (1)", g.areUVConnected(nodes.get(0), nodes.get(4)));

        System.out.println("all tests passed");
        System.out.println("you should add your own tests!");
    }
}
