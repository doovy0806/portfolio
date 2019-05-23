public class LinkedList<T>
{
    private Node<T> head, tail;
    private int size;

    public LinkedList()
    {
        size = 0;
        head = null;
        tail = null;
    }

    public void insert(int index, T data)
    {
        if(index < 0 || index > size)
            return;
        
        Node<T> temp = new Node<T>(data);

        if(size == 0)
        {
            head = temp;
            tail = temp;
        }

        else
        {
            if(index == 0)
            {
                temp.setNext(head);
                head = temp;
            }

            else if(index == size)
            {
                tail.setNext(temp);
                tail = temp;
            }

            else
            {
                Node<T> cur = head;
                
                for(int i = 1; i < index; i++)
                {
                    cur = cur.getNext();
                }
                
                temp.setNext(cur.getNext());
                cur.setNext(temp);
            }
        }
        size++;
    }

    public void remove(int index)
    {
        if(index < 0 || index >= size)
            return;
        
        if(size == 1)
        {
            head = null;
            tail = null;
        }

        else
        {
            if(index == 0)
            {
                head = head.getNext();
            }

            else
            {
                Node<T> cur = head;
                for(int i = 1; i < index; i++)
                {
                    cur = cur.getNext();
                }

                cur.setNext(cur.getNext().getNext());

                if(index == size-1)
                    tail = cur;
            }
        }
        size--;
    }

    public void clear()
    {
        head = null;
        tail = null;
        size = 0;
    }

    public T getData(int index)
    {
        if(index < 0 || index >= size)
            return null;
        
        Node<T> cur = head;

        for(int i = 0; i < index; i++)
        {
            cur = cur.getNext();
        }

        return cur.getData();
    }

    public int getSize()
    {
        return size;
    }

    public String toString()
    {
        String out = "";
        Node<T> cur = head;
        for(int i = 0; i < size; i++)
        {
            out += cur.toString();
            if(i != size-1)
                out += " -> ";
            cur = cur.getNext();
        }
        return out;
    }
    
    private class Node<T>
    {
        private Node<T> next;
        private T data;

        public Node(T data)
        {
            this.data = data;
        }

        public void setNext(Node<T> next)
        {
            this.next = next;
        }

        public void clearNext()
        {
            next = null;
        }

        public Node<T> getNext()
        {
            return next;
        }

        public T getData()
        {
            return data;
        }

        public String toString()
        {
            return data.toString();
        }
    }
}