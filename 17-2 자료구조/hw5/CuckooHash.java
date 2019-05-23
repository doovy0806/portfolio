/* 
 * Name: ±¸ÇÑ¸ğ
 * Student ID: 2014121136
 */

import java.util.Random;

/* 
 * java.util.Random is so you can generate your own hash functions
 * You should not import anything else
 */

public class CuckooHash
{
    /* 
    * The instance variables.
    *
    * a1 - int, a in the first hash function
    * b1 - int, b in the first hash function
    * a2 - int, a in the second hash function
    * b2 - int, b in the second hash function
    * n - int, the initial size of each array
    * numElements - int, the number of elements currently in the Cuckoo Hash
    * chainLength - int, the length of the allowed chain before we resize
    * threshold - double, the point at which the arrays are too full and we resize
    * array1 - int[], the first hash table
    * array2 - int[], the second hash table
    * resized - boolean, set to true if the previous insertion caused a resize
    *           and false otherwise
    */
    private int a1, b1, a2, b2, n, numElements, chainLength;
    private double threshold;
    private int[] array1, array2;
    private boolean resized;

    /*
    * The constructor. Initialize the instance variables to their default
    * value or the value passed as a parameter.
    *
    * array1, array2 should initially be filled with 0's
    */
    public CuckooHash(int n, int chainLength, double threshold)
    {
        array1 = new int[n];
        array2 = new int[n];
        this.n = n;
        this.numElements = 0;
        this.chainLength = chainLength;
        this.threshold = threshold;
        Random rand = new Random();
        do{a1 = rand.nextInt(n-1)+1;} while(a1%n==0);
        do{a2 = rand.nextInt(n-1)+1;} while(a2%n==0);
        b1 = rand.nextInt(n);
        b2 = rand.nextInt(n);




    }

    /*
    * insert data into the CuckooHash if it is not already contained
    * be sure to update resized if necessary
    */
    public void insert(int data)
    {
        if(!this.contains(data)) {
            resized = false;
            if (((double) numElements + 1) / (2 * n) >= threshold) resize();

            boolean ifInserted = false;
            int tempChain = 0;
            int temp = 0;
            int index1 = 0;
            int index2 = 0;
            do {
                if (tempChain >= chainLength) resize();
                index1 = hash1(data);
                if (array1[index1] == 0) {
                    array1[index1] = data;
                    ifInserted = true;
                } else {
                    //bump out from hash 1
                    temp = array1[index1];
                    array1[index1] = data;
                    data = temp;
                    index2 = hash2(data);
                    tempChain++;
                    if (tempChain >= chainLength) resize();
                    if (array2[index2] == 0) {
                        array2[index2] = data;
                        ifInserted = true;
                    } else {
                        //bump out from hash 2
                        temp = array2[index2];
                        array2[index2] = data;
                        data = temp;
                        tempChain++;
                        if (tempChain >= chainLength) resize();
                    }
                }

            } while (!ifInserted);
            numElements++;
        }
    }

    /*
    * remove data from the CuckooHash
    */
    public void remove(int data)
    {
        if(array1[hash1(data)]==data) array1[hash1(data)] = 0;
        else if(array2[hash2(data)]==data) array2[hash2(data)]=0;
    }

    /*
    * checks containment
    *
    * return true if data is in the CuckooHash
    */
    public boolean contains(int data)
    {
        if(array1[hash1(data)]==data) return true;
        else if(array2[hash2(data)]==data) return true;
        else
        return false;
    }

    /*
    * The first hash function
    * Remember, hashes are defined as (a,b,N) = ax+b (mod N)
    *
    * return the value computed by the first hash function
    */
    public int hash1(int x)
    {
        return (a1*x+b1)%n;
    }

    /*
    * The second hash function
    * Remember, hashes are defined as (a,b,N) = ax+b (mod N)
    *
    * return the value computed by the second hash function
    */
    public int hash2(int x)
    {
        return (a2*x+b2)%n;
    }

    /*
    * resize the CuckooHash and make new hash functions
    */
    public void resize()
    {
        int newN =2*n;
        int oldN = n;
        n= newN;
        Random rand = new Random();
        do{a1 = rand.nextInt(n-1)+1;} while(a1%n==0);
        do{a2 = rand.nextInt(n-1)+1;} while(a2%n==0);
        b1 = rand.nextInt(n);
        b2 = rand.nextInt(n);

        int[] newArray1 = new int[newN];
        int[] newArray2 = new int[newN];
        for(int i=0; i<2*oldN; i++ ){
            int index;
            int data;
            if(i<oldN) {
                index = i;
                data = array1[index];
                if(data!=0){
                    boolean ifInserted = false;
                    int tempChain =0;
                    int temp = 0;
                    int index1 = 0;
                    int index2 = 0;
                    do{
                        if(tempChain>=chainLength) resize();
                        index1 = hash1(data);
                        if(newArray1[index1] == 0){
                            newArray1[index1]=data; ifInserted=true;
                        }else{
                            //bump out from hash 1
                            temp = newArray1[index1]; newArray1[index1] = data; data = temp;
                            index2 = hash2(data);
                            tempChain++;if(tempChain>=chainLength) resize();
                            if(newArray2[index2] == 0){
                                newArray2[index2] = data; ifInserted =true;
                            }else{
                                //bump out from hash 2
                                temp = newArray2[index2]; newArray2[index2] = data; data = temp;
                                tempChain++;if(tempChain>=chainLength) resize();
                            }
                        }

                    } while(!ifInserted);
                }


            }else {
                index = i % oldN;
                data = array2[index];
                if(data!=0){
                    boolean ifInserted = false;
                    int tempChain =0;
                    int temp = 0;
                    int index1 = 0;
                    int index2 = 0;
                    do{
                        if(tempChain>=chainLength) resize();
                        index1 = hash1(data);
                        if(newArray1[index1] == 0){
                            newArray1[index1]=data; ifInserted=true;
                        }else{
                            //bump out from hash 1
                            temp = newArray1[index1]; newArray1[index1] = data; data = temp;
                            index2 = hash2(data);
                            tempChain++;if(tempChain>=chainLength) resize();
                            if(newArray2[index2] == 0){
                                newArray2[index2] = data; ifInserted =true;
                            }else{
                                //bump out from hash 2
                                temp = newArray2[index2]; newArray2[index2] = data; data = temp;
                                tempChain++;if(tempChain>=chainLength) resize();
                            }
                        }

                    } while(!ifInserted);
                }

            }
        }

        this.array1 = newArray1;
        this.array2 = newArray2;
        resized = true;
    }

    /*
    * return a1
    */
    public int getA1()
    {
        return this.a1;
    }

    /*
    * return b1
    */
    public int getB1()
    {
        return this.b1;
    }

    /*
    * return a2
    */
    public int getA2()
    {
        return this.a2;
    }

    /*
    * return b2
    */
    public int getB2()
    {
        return this.b2;
    }

    /*
    * return n
    */
    public int getN()
    {
        return this.n;
    }

    /*
    * return threshold
    */
    public double getThreshold()
    {
        return this.threshold;
    }

    /*
    * return chainLength
    */
    public int getChainLength()
    {  
        return this.chainLength;
    }

    /*
    * return array1
    */
    public int[] getArray1()
    {
        return this.array1;
    }

    /*
    * return array2
    */
    public int[] getArray2()
    {
        return this.array2;
    }

    /*
    * return the number of elements in the Cuckoo Hash
    */
    public int getNumElements()
    {
        return this.numElements;
    }

    /*
    * return the resized variable
    */
    public boolean getResized()
    {
        return this.resized;
    }
}
