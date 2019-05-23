/* 
 * Name: 구한모
 * Student ID: 2014121136
 */

public class AVLTree
{

    /* 
     * Our instance variables.
     *
     * root - AVLTreeNode, root of our AVLTree
     * size - int, the number of elements in our AVLTree
     * 
     * You are NOT allowed to add your own instance variables
     */    
    
    private AVLTreeNode root;
    private int size;

    /*
    * Our constructor. 
    * Initialize the instance variables to their default values
    */
    public AVLTree()
    {
        root = null;
        //size?? 3? or1?
        this.size = 0;
    }

    /*
    * Constructs a new AVLTreeNode and inserts it into our AVLTree
    *
    * return the inserted AVLTreeNode or null if a node with the same data
    * already exists
    */
    public AVLTreeNode insert(int data)
    {
        AVLTreeNode temp =root;
        AVLTreeNode returnNode;
        AVLTreeNode prev;
        if(this.size==0 && this.root ==null){
            root = new AVLTreeNode(data);
            this.size++;
            return root;
        }else if(this.contains(data)) return null;
        else{
            do{
                if(temp.getData()>data){
                    if(temp.getLeft()!=null)temp = temp.getLeft();
                    else {
                        temp.setLeft(new AVLTreeNode(data));
                        returnNode = temp.getLeft();
                        temp = returnNode;
                        this.size++;
                        break;
                    }
                }else if(temp.getData() < data){
                    if(temp.getRight()!=null)temp = temp.getRight();
                    else{
                        temp.setRight(new AVLTreeNode(data));
                        returnNode = temp.getRight();
                        temp = returnNode;
                        this.size++;
                        break;
                    }
                }else return null;
            }while(true);


        }
        returnNode = temp;
        // reset height appropriately with new insertion
        this.resetHeight(returnNode);
        this.resetBF(returnNode);


        reRestructure(returnNode);
        return returnNode;

    }

    /*
    * returns the node in the tree containing the desired data
    *
    * return null if such a node does not exist
    */
    public AVLTreeNode retrieve(int data)
    {
        if(this.root==null) return null;
        AVLTreeNode temp = this.root;

        do{
            if(data<temp.getData()) temp = temp.getLeft();
            else if(temp.getData()<data) temp= temp.getRight();
            else return temp;
        }while(temp!=null);
        return null;
    }

    /*
    * return whether or not the tree contains a node with the desired data
    */
    public boolean contains(int data)
    {
        if(this.root==null) return false;
        AVLTreeNode temp = this.root;
        do{
            if(data<temp.getData()) temp = temp.getLeft();
            else if(temp.getData()<data) temp= temp.getRight();
            else return true;
        }while(temp!=null);

        return false;
    }

    /*
    * remove and return the AVLTreeNode with the desired data
    *
    * return null if the data is not in the AVLTree
    */
    public AVLTreeNode remove(int data)
    { // return 하기 전에 restructure 때리기
        if(this.root==null) return null;
        AVLTreeNode temp = this.root;
        AVLTreeNode prev;
        if(!this.contains(data)) return null;
        else if(this.root.getData()==data&&(this.root.getLeft()==null||this.root.getRight()==null)){
            //없애는 노드가 루트인데, leaf가 자식인 경우
            AVLTreeNode returnNode = new AVLTreeNode(data);
            AVLTreeNode next = root.getLeft()==null? root.getRight() : root.getLeft();
            this.root = next;
            this.size--;
            return returnNode;
        }
        else{ // temp 찾기 - temp가 루트가 아닌경우, prev는 temp의 parent인 아이.
            do{
                if(temp.getData()>data){
                    prev = temp;
                    temp = prev.getLeft();
                }else if(temp.getData() < data){
                    prev = temp;
                    temp = prev.getRight();
                }else{ // temp.getData()== data
                    prev = this.getParentNode(temp);
                    break;
                }
            }while(data!=temp.getData());

        }
        // 없애는 노드가 마지막 끝, leaf일 때
        if(temp.getLeft()==null){
            if(temp.equals(prev.getLeft())){
                prev.setLeft(temp.getRight());
            }else if(temp.equals(prev.getRight())){
                prev.setRight(temp.getRight());
            }
            this.size--;
            calculateHeight(prev);
            calculateBF(prev);
            this.reRestructure(prev);
            return temp;
        }else if(temp.getRight()==null){
            if(temp.equals(prev.getLeft())){
                prev.setLeft(temp.getLeft());
            }else if(temp.equals(prev.getRight())){
                prev.setRight(temp.getLeft());
            }
            this.size--;
            resetHeight(prev);
            resetBF(prev);
            this.reRestructure(prev);

            return temp;

        }else {
            //없애는 노드가 leaf가 없는 경우 - right의 leftmost grandgrandchild찾으면 됨.
            AVLTreeNode returnNode = new AVLTreeNode(data);
            AVLTreeNode next = this.inorderNext(temp);
            AVLTreeNode nextParent = this.getParentNode(next);
            boolean ifNextLeft = next.getData()<nextParent.getData()? true : false;
            if(next.getRight()!=null){
                temp.setData(next.getData());
                if(ifNextLeft) nextParent.setLeft(next.getRight());
                else nextParent.setRight(next.getRight());
            } else{
                temp.setData(next.getData());
                if(ifNextLeft)nextParent.setLeft(null);
                else nextParent.setRight(null);
            }
            this.size--;
            resetHeight(nextParent);
            resetBF(nextParent);
            this.reRestructure(nextParent);

            return returnNode;
        }

    }

    /*
    * clear the AVLTree
    */
    public void clear()
    {
        this.root = null;
        this.size = 0;

    }

    /*
    * return whether or not the AVLTree is empty
    */
    public boolean isEmpty()
    {
        if(this.size ==0) return true;
        else return false;
    }

    /*
    * return the root of the AVLTree
    */
    public AVLTreeNode getRoot()
    {
        if(this.size==0 || this.root ==null)
        return null;
        else return this.root;
    }

    /*
    * return the height of the AVLTree
    */
    public int getHeight()
    {
        if(this.root!=null)
        return this.root.getHeight();
        else return 0;
    }

    public AVLTreeNode getParentNode(AVLTreeNode node){
        AVLTreeNode temp = this.root;
        AVLTreeNode tempParent = this.root;

        int nodeData = node.getData();
        if(nodeData == this.root.getData()) return null;
        else if(root!=null){
            do{
                if(nodeData<tempParent.getData()){
                   temp = tempParent.getLeft();
                   if(nodeData == temp.getData()){
                       return tempParent;
                   }else tempParent = temp;
                }else if(nodeData> tempParent.getData()){
                    temp = tempParent.getRight();
                    if(nodeData==temp.getData()) return tempParent;
                    else tempParent = temp;
                }
            }while(tempParent!=null&&temp.getData()!=nodeData);
        }
        return tempParent;
    }

    public AVLTreeNode restructure(AVLTreeNode a, int type){
        //pull the node that has balance problem to the top.
        AVLTreeNode b =null;
        AVLTreeNode c =null;
        AVLTreeNode aParent = null;
        boolean ifALeft = false;

        switch (type){
            case 1:
                //위에서부터 left-left 인 경우 나중에는 b가제일 위 2, 1, 0 / -2 -1 0
                if(!a.equals(root)) {
                    aParent = getParentNode(a);
                    ifALeft = a.getData()<aParent.getData() ? true :  false;
                    b = a.getLeft();
                    c = b.getLeft();
                    a.setLeft(b.getRight());
                    b.setRight(a);
                    if(ifALeft) aParent.setLeft(b);
                    else aParent.setRight(b);
                    calculateHeight(a);
                    calculateHeight(c);
                    resetHeight(b);
                    calculateBF(a);
                    calculateBF(c);
                    resetBF(b);
                }else{
                    b = a.getLeft();
                    c = b.getLeft();
                    a.setLeft(b.getRight());
                    b.setRight(a);
                    this.root=b;
                    calculateHeight(a);
                    calculateHeight(c);
                    resetHeight(b);
                    calculateBF(a);
                    calculateBF(c);
                    resetBF(b);
                }
                break;

            case 2:
                //위에서부터 right-left인 경우 c가제일위 -2 , 1, 0/ 2 -1 0
                if(!a.equals(this.root)) {
                    aParent = getParentNode(a);
                    ifALeft = a.getData() < aParent.getData() ? true: false;

                    b = a.getRight();
                    c = b.getLeft();
                    a.setRight(c.getLeft());
                    b.setLeft(c.getRight());
                    c.setLeft(a);
                    c.setRight(b);
                    if(ifALeft) aParent.setLeft(c);
                    else aParent.setRight(c);
                    calculateHeight(a);
                    calculateHeight(b);
                    calculateHeight(c);
                    calculateBF(a);
                    calculateBF(b);
                    calculateBF(c);
                }else{
                    b = a.getRight();
                    c = b.getLeft();
                    a.setRight(c.getLeft());
                    b.setLeft(c.getRight());
                    c.setLeft(a);
                    c.setRight(b);
                   this.root = c;
                    calculateHeight(a);
                    calculateHeight(b);
                    calculateHeight(c);
                    calculateBF(a);
                    calculateBF(b);
                    calculateBF(c);
                }

                break;
            case 3:
                //위에서부터 left-right인 경우 2, -1, 0 / -2 1 0
                if(!a.equals(this.root)) {
                    aParent = getParentNode(a);
                    ifALeft = a.getData() < aParent.getData() ? true : false;

                    b = a.getLeft();
                    c = b.getRight();
                    a.setLeft(c.getRight());
                    b.setRight(c.getLeft());
                    c.setRight(a);
                    c.setLeft(b);
                    if(ifALeft) aParent.setLeft(c);
                    else aParent.setRight(c);
                    calculateHeight(a);
                    calculateHeight(b);
                    calculateHeight(c);
                    calculateBF(a);
                    calculateBF(b);
                    calculateBF(c);
                }else{
                    b = a.getLeft();
                    c = b.getRight();
                    a.setLeft(c.getRight());
                    b.setRight(c.getLeft());
                    c.setRight(a);
                    c.setLeft(b);
                    this.root = c;
                    calculateHeight(a);
                    calculateHeight(b);
                    calculateHeight(c);
                    calculateBF(a);
                    calculateBF(b);
                    calculateBF(c);

                }
                break;

            case 4:
                //위에서부터 right-right인 경우 -2, -1, 0 / 2 1 0
                if(!a.equals(this.root)) {
                    aParent = getParentNode(a);
                    ifALeft = a.getData() < aParent.getData() ? true : false;
                    b = a.getRight();
                    c = b.getRight();
                    a.setRight(b.getLeft());
                    b.setLeft(a);
                    if(ifALeft) aParent.setLeft(b);
                    else aParent.setRight(b);
                    calculateHeight(a);
                    calculateHeight(c);
                    resetHeight(b);
                    calculateBF(a);
                    calculateBF(c);
                    resetBF(b);
                }else{
                    b = a.getRight();
                    c = b.getRight();
                    a.setRight(b.getLeft());
                    b.setLeft(a);
                    this.root = b;
                    calculateHeight(a);
                    calculateHeight(c);
                    resetHeight(b);
                    calculateBF(a);
                    calculateBF(c);
                    resetBF(b);
                }
                break;
            default:
                return null;
        }


        return a;
    }
    public int calculateBF (AVLTreeNode avl){
        int leftHeight = avl.getLeft()!=null ? (avl.getLeft().getHeight()) : -1;
        int rightHeight = avl.getRight()!=null ? (avl.getRight().getHeight()) :-1;
        avl.setBalanceFactor(rightHeight-leftHeight);
        return avl.getBalanceFactor();
    }
    public void calculateHeight(AVLTreeNode avl){

        if(avl==null) avl.setHeight(-1);
        else{
            int leftHeight = avl.getLeft()!=null?avl.getLeft().getHeight() : -1;
            int rightHeight = avl.getRight()!=null? avl.getRight().getHeight():-1;
            avl.setHeight(leftHeight>rightHeight?leftHeight+1:rightHeight+1);

        }
    }
    public void resetHeight(AVLTreeNode avl){

        if(avl.equals(this.root)) {calculateHeight(this.root); return;}
        do{
            this.calculateHeight(avl);

//            this.calculateBF(avl);

        if(!avl.equals(this.root)) {
            avl = this.getParentNode(avl);
        }else {
            this.calculateHeight(avl);
            break;
        }

        }while(true);
    }
    public void resetBF(AVLTreeNode avl){
        if(avl.equals(this.root)) calculateBF(this.root);
        else {
            do {
                this.calculateBF(avl);
                if (!avl.equals(this.root)) avl = this.getParentNode(avl);
                else{
                    calculateBF(avl);
                    break;
                }
            } while (true);
        }
    }

    public AVLTreeNode inorderNext(AVLTreeNode avl){
        AVLTreeNode temp = avl;
        if(temp.getRight()!=null) {
            temp = temp.getRight();

            while (temp.getLeft() != null) {
                temp = temp.getLeft();
            }
        }else if(temp.equals(this.getParentNode(temp).getLeft())) {
            //temp의 right은 null이고 temp가 부모의 left인 경우
            temp = getParentNode(temp);
            while (temp.getRight() != null) temp = temp.getRight();
        }else if(temp.equals(this.getParentNode(temp).getRight())){
            //temp의 right은 null이고 temp가 부모의 right인 경우
            while(temp.equals(getParentNode(temp).getRight())){
                temp = getParentNode(temp);
                if(temp.equals(this.root)){
                    if(temp.getRight()==null) return root;
                    else temp = temp.getRight();
                    while(temp.getLeft()!=null) temp = temp.getLeft();
                    return  temp;
                }

            }

        }

        return temp;
    }

    public void reRestructure(AVLTreeNode w){
        AVLTreeNode z, y, x;
        z = w;
            while(true){
                if(z.getBalanceFactor()>1){
                    y = (nodeHeight(z.getLeft()) > nodeHeight(z.getRight()) ? z.getLeft() : z.getRight());
                    x = (nodeHeight(y.getLeft()) > nodeHeight(y.getRight()) ? y.getLeft() : y.getRight());
                    if(y.getBalanceFactor()>0) restructure(z, 4);
                    else restructure(z, 2);
                    return;
                }else if(z.getBalanceFactor()<-1){
                    y = (nodeHeight(z.getLeft())>nodeHeight(z.getRight())? z.getLeft() : z.getRight());
                    x = (nodeHeight(y.getLeft())>nodeHeight(y.getRight())? y.getLeft() : y.getRight());
                    if(y.getBalanceFactor()>0) restructure(z, 3);
                    else restructure(z,1);
                    return;
                }else if(!z.equals(this.root)) z = this.getParentNode(z);
                else return;
            }


    }

    public int nodeHeight(AVLTreeNode avl){
        if (avl==null) return -1;
        else return avl.getHeight();
    }

}

class AVLTreeNode
{

    /* 
     * Our instance variables.
     *
     * data - int, the data the AVLTreeNode will hold
     * height - int, the height of the AVLTreeNode
     * balanceFactor - int, the balance factor of the node
     * left - AVLTreeNode, the left child of the node
     * right - AVLTreeNode, the right child of the node
     */

    private int data, height, balanceFactor;
    private AVLTreeNode left, right;

    /*
    * Our constructor. 
    * Initialize the instance variables to their default values or the
    * values passed as paramters
    */
    public AVLTreeNode(int data)
    {
        this.data = data;
        this.height =0;
        this.left =null;
        this.right = null;
        this.balanceFactor = 0;
        //rest are initialized automatically I guess?
    }

    /*
    * Set the value stored in data
    */
    public void setData(int data)
    {
        this.data = data;
    }

    /*
    * Set the value stored in height
    */
    public void setHeight(int height)
    {
        this.height = height;

    }

    /*
    * Set the value stored in balanceFactor
    */
    public void setBalanceFactor(int balanceFactor)
    {
        this.balanceFactor = balanceFactor;

    }

    /*
    * Set the left child
    */
    public void setLeft(AVLTreeNode left)
    {
        this.left = left;

    }


    /*
    * Set the right child
    */
    public void setRight(AVLTreeNode right)
    {
        this.right = right;

    }

    /*
    * clear the left child
    */
    public void clearLeft()
    {
        this.left = null;
        //?
    }

    /*
    * clear the right child
    */
    public void clearRight()
    {
        this.right = null;
        //?

    }

    /*
    * get the data stored in the AVLTreeNode
    */
    public int getData()
    {
        return this.data;
    }

    /*
    * get the height of the AVLTreeNode
    */
    public int getHeight()
    {
        return this.height;
    }

    /*
    * get the balanceFactor of the AVLTreeNode
    */
    public int getBalanceFactor()
    {
        return this.balanceFactor;
    }

    /*
    * get the left child
    */
    public AVLTreeNode getLeft()
    {
        return this.left;
    }

    /*
    * get the right child
    */
    public AVLTreeNode getRight()
    {
        return this.right;
    }
}