package assignment3;

public class LinkedStack<E> implements stackinterface<E> {
public class Node
{
	E element;
	Node next;
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
Node top;
public LinkedStack()
{
	top=null;
	size=0;
}
@Override
public void push(E a) throws FullStackException {
	Node node=new Node(a);
	node.next=top;
	top=node;
	size++;
	}
@Override
public int size() {
	return size;
}
@Override
public boolean isEmpty() {
	return size<1;
}
@Override
public E top() {
	return top.element;
}
@Override
public E pop() throws EmptyStackException {
	if(isEmpty())
	{
		throw new EmptyStackException("Cant pop stack empty");
	}
	E elem=top.element;
	top=top.next;
	size--;
	return elem;	
}
public String toString()
{
	String output=size()+"\t \t";
	Node n=top;
	while(n!=null)
	{
	output+="  "+n.element.toString();
	n=n.next;
	}
	return output;
}
}
