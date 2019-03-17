package assignment3;
public interface stackinterface <E> {
	public void push(E a) throws FullStackException;
	public int size();
	public boolean isEmpty();
	public E top();
	public E pop() throws EmptyStackException;
	public String toString();
}

