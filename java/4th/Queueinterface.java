package assign4;

public interface Queueinterface<E> {
		public void enqueue(E a);
		public int size();
		public boolean isEmpty();
		public E front() throws EmptyQueueException;
		public E dequeue() throws EmptyQueueException;
		public String toString();
	
}
