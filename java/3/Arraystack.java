package assignment3;

public class Arraystack<E> implements stackinterface<E>
{
int top=0,stsize;
E S[];
Arraystack()
{
	S=(E[])new Object[1000];
	stsize=1000;
}
Arraystack(int N)
{
	S=(E[])new Object[N];
	stsize=N;
}
public void push(E o)throws FullStackException
{
	if(size()==stsize)
	{
		throw new FullStackException("Stack full");
	}
	top=top+1;
	S[top]=o;
	
}
@Override
public int size() {
	return top;
}
@Override
public boolean isEmpty() {
	return top<1;
}
@Override
public E top() {
	return S[top];
}
@Override
public E pop() throws EmptyStackException{
	if(isEmpty())
	{
	throw new EmptyStackException("Stack is empty cant pop");
	}
	E e=S[top];
	S[top]=null;
	top=top-1;
	return e;
}
@Override
public String toString()
{
	//format stack elements 
	String output=size()+"\t \t";
	for(int i=size();i>0;i--)
	{
	output+="  "+S[i];
	}
	return output;
}


}
