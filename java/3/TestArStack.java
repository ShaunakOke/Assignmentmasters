package assignment3;

public class TestArStack {

	public static void main(String args[])
	{
		{//block to reuse and delete st object
		Arraystack<Object> st=new Arraystack<Object>(7);
		System.out.println("Array Implementation :\n");
		System.out.println("Size            Contents");
		st.push(new Integer(5));
		st.push("Hello,.,.World");
		st.push(new Character('X'));
		st.push(new Integer(521));
		st.push(new Integer(3));
		System.out.println(st);
		st.pop();
		st.pop();
		System.out.println(st);
		st.push(new Float(53.256));
		st.push(new Character('A'));
		st.push(new Character('9'));
		System.out.println(st);
		st.pop();
		st.push(new Character('1'));
		System.out.println(st);
		}
	
	
		LinkedStack<Object> st=new LinkedStack<Object>();
		System.out.println("\n Linked Stack Implementation :\n");
		System.out.println("Size            Contents");
		st.push(new Integer(5));
		st.push("Hello,.,.World");
		st.push(new Character('X'));
		st.push(new Integer(521));
		st.push(new Integer(3));
		System.out.println(st);
		st.pop();
		st.pop();
		System.out.println(st);
		st.push(new Float(53.256));
		st.push(new Character('A'));
		st.push(new Character('9'));
		System.out.println(st);
		st.pop();
		st.push(new Character('1'));
		System.out.println(st);	
	}
}
