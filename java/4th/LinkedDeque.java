package assign4;


public class LinkedDeque<E> implements Dequeinterface<E> {
public class Node
{
	E element;
	Node next,prev;
	public Node(E element)
	{
		this.element=element;
	}
	public String toString()
	{
		//convert any object to string
		return element.toString();
	}
}
int size;
Node front,rear;
public LinkedDeque()
{
	front=null;
	rear=null;
	size=0;
}

@Override
public int size() {
	return size;
}
@Override
public boolean isEmpty() {
	return size<1;
}
public String toString()
{	
	String output;
	if(!isEmpty())
	{
	output=size()+"\t \t";
	Node n=front;
	while(n!=rear)
	{
		output+="  "+n.element.toString();
		n=n.next;
	}
	output+="  "+n.element.toString();
	return output;
	}
	else
	{
		return "0       ";
	}
	
}

@Override
public E getFirst() throws EmptyDequeException {
	// TODO Auto-generated method stub
	return front.element;
}
@Override
public E getLast() throws EmptyDequeException {
	// TODO Auto-generated method stub
	return rear.element;
}
@Override
public void addFirst(E element) {
	// TODO Auto-generated method stub
	Node n=new Node(element);
	n.next=front;
	if(front==null)
	{
		rear=n;
	}
	else
	{
		front.prev=n;
	}
	front=n;
	size++;

}
@Override
public void addLast(E element) {
	// TODO Auto-generated method stub
	Node n=new Node(element);
	n.prev=rear;
	if(rear==null)
	{
		front=n;
	}
	else
	{
		rear.next=n;
	}
	rear=n;
	size++;
}
	
@Override
public E removeFirst() throws EmptyDequeException {
	// TODO Auto-generated method stub
	if(front==null && rear==null)
	{
		throw new EmptyDequeException("cant remove from empty deque");
	}
	Node n=new Node(front.element);
	if(front==rear)
	{
		front=null;
		rear=null;
	}
	else
	{
	front.next.prev=null;
	front=front.next;
	n.next=null;
	}
	size--;
	return n.element;
}
@Override
public E removeLast() throws EmptyDequeException {
	// TODO Auto-generated method stub
	if(front==null && rear==null)
	{
		throw new EmptyDequeException("cant remove from empty deque");
	}
	Node n=new Node(rear.element);
	if(front==rear)
	{
		front=null;
		rear=null;
	}
	else
	{
	rear.prev.next=null;
	rear=rear.prev;
	n.prev=null;
	}
	size--;
	return n.element;

}
}


