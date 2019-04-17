package assign4;



public class ArrayQueue<E> implements Queueinterface<E>
{
	int front=0,rear=0,qsize;
	E S[];
	ArrayQueue()
	{
		S=(E[])new Object[1000];
		qsize=1000;
	}
	ArrayQueue(int N)
	{
		S=(E[])new Object[N];
		qsize=N;
	}
	@Override
	public void enqueue(E o)
	{
		S[rear]=o;
		rear=(rear+1)%qsize;
	}
	@Override
	public int size() {
		return (qsize+rear-front)%qsize;
	}
	@Override
	public boolean isEmpty() {
		return (front==rear);
	}
	@Override
	public E front() throws EmptyQueueException {
		if(isEmpty())
		{
			throw new EmptyQueueException("Queue is empty no front element");
		}
		return S[front];
	}
	@Override
	public E dequeue() throws EmptyQueueException{
		if(isEmpty())
		{
		throw new EmptyQueueException("Queue is empty cant dequeue");
		}
		E e=S[front];
		S[front]=null;
		front=front+1;
		return e;
	}
	@Override
	public String toString()
	{
		//format queue elements 
		String output=size()+"\t \t";
		if(rear<front)
		{
			//go till end of array and start from beginning
			for(int i=front;i<=qsize;i++)
			{
				output+="  "+S[i];
			}
			for(int i=0;i<=rear;i++)
			{
				output+="  "+S[i];
			}
		}
		else
		{//front to rear since not looping
			for(int i=front;i<rear;i++)
			{
				output+="  "+S[i];
			}
		}
		return output;
	}
	

public static void main(String args[])
{
	//since visualization was not asked in questions. heres a simple test to see working of arrayqueue 
	//with random insertions deletions
ArrayQueue<Object> a=new ArrayQueue<Object>();
System.out.println("Size               front<--->Rear");
System.out.println(a);
a.enqueue(new Integer(20));
System.out.println(a);
a.enqueue(new Character('h'));
System.out.println(a);
a.dequeue();
System.out.println(a);
a.enqueue(new String("string.txt"));
System.out.println(a);
a.enqueue(new Float(35.456));
System.out.println(a);
a.dequeue();
System.out.println(a);
a.enqueue(new Integer(2340));
System.out.println(a);
}
}

