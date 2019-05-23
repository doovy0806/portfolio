/*
 * Name: 구한모
 * Student ID: 2014121136
 */
 
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.HashSet;
import java.util.Iterator;

/*
 * Do not import anything else
 */

public class Graph
{
    /*
     * Our instance variables
     *
     * numNodes - int - holds the number of nodes currently in the graph
     * numEdges - int - holds the number of edges currently in the graph
     * nodes - ArrayList<Node> - holds all the nodes indexed by their label
     *                           if node n has label i, it must be located in
     *                           nodes.get(i).
     * edges - ArrayList<Edge> - holds all of the nodes in the graph
     *                           these can be in any order
     * adjacencyList - HashMap<Node, HashMap<Node, Edge>> - the adjacency list for the graph
     *                                                      with this, you can get an edge
     *                                                      between node u and v (if it exists)
     *                                                      by calling Edge e = adjacencyList.get(u).get(v);
     * INFINITY - final int - you can use this value to represent infinity in dijkstra's algorithm
     *
     * You may add any other instance variables that you wish
     */

    private int numNodes, numEdges;
    private ArrayList<Node> nodes;
    private ArrayList<Edge> edges;
    private HashMap<Node, HashMap<Node, Edge>> adjacencyList;
    private final int INFINITY = Integer.MAX_VALUE;
    private HashSet<Node> connection = new HashSet<>();

    /*
    * Constructor for our Graph
    */
    public Graph()
    {
        this.numNodes = 0;
        this.numEdges =0;
        this.adjacencyList = new HashMap<Node,HashMap<Node, Edge>>();
        this.nodes = new ArrayList<>();
        this.edges = new ArrayList<>();
    }

    /*
    * Add a new node to the graph
    *
    * The nodes in the graph are labeled from 0 to numNodes-1
    * so the new node should have label numNodes (before incrementing)
    *
    * For example, if we have nodes 0,1,2 (so numNodes = 3) then addNode()
    * will make a new node with label 3 and then increment numNodes
    *
    * Make sure you place the new node in the correct position in nodes
    * and that you insert it into adjacencyList
    * 
    * Return the new node
    */
    public Node addNode()
    {
        Node newNode = new Node(this.numNodes);
        this.nodes.add(this.numNodes, newNode);
        this.numNodes++;
        this.adjacencyList.put(newNode, new HashMap<Node, Edge>());
        return newNode;
    }

    /*
    * Add an edge with the given endpoints and weight to the graph
    *
    * You do not have to worry about the case where u or v does not exist
    * If there is already an edge between u and v, you should update the
    * weight of that edge to the new weight and return that edge
    * Otherwise, you should create a new edge with the correct properties
    *
    * Be sure to insert it into edges and into adjacencyList in the appropriate places
    * Remember that this graph is undirected, so an edge between u and v is
    * also an edge between v and u.
    *
    * Return the new edge or the updated edge if it already existed
    *
    */        
    public Edge addEdge(Node u, Node v, int weight)
    {
        if(this.adjacencyList.get(u).containsKey(v)){
            Edge newEdge = this.adjacencyList.get(u).get(v);
            newEdge.setWeight(weight);
            return newEdge;
        }else{
            Edge newEdge = new Edge(u, v, weight);
            this.edges.add(newEdge);
            this.adjacencyList.get(u).put(v, newEdge);
            this.adjacencyList.get(v).put(u, newEdge);
            this.numEdges++;
            return newEdge;
        }

    }

    /*
    * Perform dijkstras algorithm on the graph, with source as the source node
    *
    * You do not have to consider the case of negative weights
    *
    * Return a hashmap with all of the nodes in the graph as the keys and
    * the value being the length of the shortest path from the source to
    * the node.
    */
    public HashMap<Node, Integer> dijkstra(Node source) {
        int[] dijkLables = new int[this.numNodes];
        HashMap<Node, Integer> cloud = new HashMap<>();
        Node tempNode = source;

        for (int i = 0; i < numNodes; i++) {
            if (this.adjacencyList.get(tempNode).containsKey(nodes.get(i))) {
                dijkLables[i] = this.adjacencyList.get(tempNode).get(nodes.get(i)).getWeight();
            }else if(i==source.getLabel()){
                dijkLables[i]=0;
            }else{
                dijkLables[i] = this.INFINITY;
            }
        }
        cloud.put(source, 0);
        while (true) {
            int dijindex = -1;
            int dijMin = this.INFINITY;
            for (int i = 0; i < numNodes; i++) {
                if (dijkLables[i] != 0 && dijMin > dijkLables[i]) {
                    dijindex = i; dijMin = dijkLables[i];
                }
                //djindex는 현재 클라우드에서 최소의 dijlable가지는 노드의 index
            }
            if (dijindex >= 0) cloud.put(nodes.get(dijindex), dijkLables[dijindex]);
            else break;
            tempNode = nodes.get(dijindex);
            HashMap<Node, Edge> tempHash = this.adjacencyList.get(tempNode);
            for (int i = 0; i < numNodes; i++) {
                if (tempHash.containsKey(nodes.get(i))) {
                    //만약 현재 추가된 노드가 연결된 노드들의 경우에 필요하면 dijlable을 업데이트 한다.
                    dijkLables[i] = Math.min(dijkLables[i], dijkLables[dijindex] + tempHash.get(nodes.get(i)).getWeight());
                }
            }
            dijkLables[dijindex] = 0;
        }
        return cloud;
    }


    /*
    * Return the length of the shortest path from source to target
    * If there is no such path, this should return INFINITY
    */
    public int shortestPathLength(Node source, Node target)
    {
        HashMap<Node, Integer> cloud = this.dijkstra(source);
        if(cloud.containsKey(target)){
            return cloud.get(target);
        }else{
            return this.INFINITY;
        }

    }

    /*
    * Return a list of all of the edges in a minimum spanning tree of
    * the graph. The order does not matter. If there are multiple valid
    * minimum spanning trees, you can return any of them.
    */
    public ArrayList<Edge> minSpanningTree() {

        ArrayList<Edge> mst = new ArrayList<>();
        HashSet<Node> cloud = new HashSet<>();
        PriorityQueue<Edge> pq = new PriorityQueue<>();

        Node tempNode = nodes.get(0);
        cloud.add(nodes.get(0));
        HashMap<Node, Edge> tempHash = this.adjacencyList.get(tempNode);
        for(int i=0; i<numNodes; i++){
            if(tempHash.containsKey(nodes.get(i))){
                pq.add(tempHash.get(nodes.get(i)));
            }
        }
        while(!pq.isEmpty()){
            Edge tempEdge = pq.remove();
            while(cloud.contains(tempEdge.getU())&&cloud.contains(tempEdge.getV())&&!pq.isEmpty()) {
                tempEdge = pq.remove();
            }
            if(cloud.contains(tempEdge.getU())){
                cloud.add(tempEdge.getV());
                mst.add(tempEdge);
                tempNode = tempEdge.getV();
            }else if(cloud.contains(tempEdge.getV())){
                cloud.add(tempEdge.getU());
                mst.add(tempEdge);
                tempNode = tempEdge.getU();
            }
            tempHash = this.adjacencyList.get(tempNode);
            for(int i=0; i<numNodes; i++){
                if(tempHash.containsKey(nodes.get(i))&&!cloud.contains(nodes.get(i))){
                    pq.add(tempHash.get(nodes.get(i)));
                }
            }

        }
        return mst;

    }

    /*
    * Return the total weight of the minimum spanning tree of the graph
    */
    public int minSpanningTreeWeight()
    {
        ArrayList<Edge> mst = this.minSpanningTree();
        int weight =0;
        for(int i=0; i<mst.size(); i++){
            weight += mst.get(i).getWeight();
        }
        return weight;
    }

    /*
    * Return true if there is any path between u and v and false otherwise
    */
    public boolean areUVConnected(Node u, Node v)
    {

        Node tempNode = u;
        connection.add(u);
        boolean ifConnect = false;
        HashMap<Node, Edge> tempHash = this.adjacencyList.get(tempNode);
        if(tempHash.containsKey(v)){
            connection.clear();
            return true;
        }

        for(int j=0; j<numNodes; j++){
            if(tempHash.containsKey(nodes.get(j))&&!connection.contains(nodes.get(j))) {
                tempNode = nodes.get(j);
                ifConnect = this.areUVConnected(tempNode, v)||ifConnect;
                if(ifConnect) return true;
            }
        }



        return ifConnect;
    }

    /*
    * Return true if there is only one connected component in the graph and false otherwise
    */
    public boolean isConnected()
    {
        if(this.numConnectedComponents()==1 ) return true;
        else return false;
    }

    /*
    * Return the number of connected components in the graph
    */
    public int numConnectedComponents()
    {
        HashSet<Node> cluster = new HashSet<>();
        ArrayList<HashSet<Node>> clusters = new ArrayList<>();
        //use kruskal's algorithm
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        for(int i=0; i<edges.size(); i++){
            pq.add(edges.get(i));
        }
        while(!pq.isEmpty()){
            Edge tempEdge = pq.remove();
            HashSet<Node> Ucluster =null;
            HashSet<Node> Vcluster =null;
            for(int i=0; i<clusters.size(); i++){
                if(clusters.get(i).contains(tempEdge.getU())){
                    Ucluster = clusters.get(i);
                }
                if(clusters.get(i).contains(tempEdge.getV())){
                    Vcluster = clusters.get(i);
                }
            }
            if(Ucluster==null && Vcluster==null){
                Ucluster = new HashSet<>();
                Ucluster.add(tempEdge.getU());
                Ucluster.add(tempEdge.getV());
                clusters.add(Ucluster);
            }else if(Ucluster==null){
                Vcluster.add(tempEdge.getU());
            }else if(Vcluster==null){
                Ucluster.add(tempEdge.getV());
            }else{
                Ucluster.addAll(Vcluster);
                clusters.remove(Vcluster);
            }
        }
        int isolated = 0;
        int clustersTotal =0;
        for(int i=0; i<clusters.size();i++){
            clustersTotal+=clusters.get(i).size();
        }
        isolated = numNodes - clustersTotal;
        int ncc = clusters.size() + isolated;

        return ncc;
    }

    /*
    * Return the number of nodes in the graph
    */
    public int getNumNodes()
    {
        return this.numNodes;
    }

    /*
    * Return the number of edges in the graph
    */
    public int getNumEdges()
    {
        return this.numEdges;
    }

    /*
    * Return the nodes in the graph
    */
    public ArrayList<Node> getNodes()
    {
        return this.nodes;
    }

    /*
    * Return the edges in the graph
    */
    public ArrayList<Edge> getEdges()
    {
        return this.edges;
    }

    /*
    * Return a hashmap with all of the nodes in the graph as the keys
    *     and the values being a list of all the edges that have the node
    *     as an endpoint
    */
    public HashMap<Node, HashMap<Node, Edge>> getAdjacencyList()
    {
         return this.adjacencyList;
    }

    /*
    * Return the adjacency matrix representing the graph
    * The value at [i][j] should be the weight between the nodes with
    * labels i and j (or 0 if there is no edge between them)
    */
    public int[][] getAdjacencyMatrix()
    {
        int[][] matrix = new int[numNodes][numNodes];
        for(int i=0; i<numNodes; i++){
            for(int j=0; j<numNodes; j++){
                Node nodeU = nodes.get(i);
                Node nodeV = nodes.get(j);
                if(this.adjacencyList.get(nodeU).containsKey(nodeV)){
                    matrix[i][j] = this.adjacencyList.get(nodeU).get(nodeV).getWeight();
                }else{
                    matrix[i][j] =0;
                }
            }
        }
        return matrix;
    }
}

/*
 *  ================================
 *  Do not modify anything below this comment
 *  ================================
 */

class Node
{
    private int label;

    public Node(int label)
    {
        this.label = label;
    }

    public void setLabel(int label)
    {
        this.label = label;
    }

    public int getLabel()
    {
        return label;
    }
}

class Edge implements Comparable<Edge>
{
    private Node u,v;
    private int weight;

    public Edge(Node u, Node v, int weight)
    {
        this.u = u;
        this.v = v;
        this.weight = weight;
    }

    public void setU(Node u)
    {
        this.u = u;
    }

    public void setV(Node v)
    {
        this.v = v;
    }

    public void setWeight(int weight)
    {
        this.weight = weight;
    }

    public Node getU()
    {
        return u;
    }

    public Node getV()
    {
        return v;
    }

    public int getWeight()
    {
        return weight;
    }

    public int compareTo(Edge e)
    {
        return Integer.compare(this.weight, e.getWeight());
    }
}
