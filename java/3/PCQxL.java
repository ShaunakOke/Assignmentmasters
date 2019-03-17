package assignment3;
//Class for testing questions on linked stack
public class PCQxL {
	
public static void A2()
{
	String popstr = "";
	LinkedStack<Object> st=new LinkedStack<Object>();
	System.out.println("Size            Contents");
	System.out.println(st);
	st.push(new Character('e'));
	System.out.println(st);
	st.push(new Character('s'));
	System.out.println(st);
	st.push(new Character('c'));
	System.out.println(st);
	popstr+=st.pop().toString();
	System.out.println(st);
	st.push(new Character('u'));
	System.out.println(st);
	st.push(new Character('a'));
	System.out.println(st);
	popstr+=st.pop().toString();
	System.out.println(st);
	st.push(new Character('o'));
	System.out.println(st);
	st.push(new Character('t'));
	System.out.println(st);
	popstr+=st.pop().toString();
	System.out.println(st);
	st.push(new Character('h'));
	System.out.println(st);
	System.out.println("\n\n popped word is:"+popstr);
	}

public static void A3()
{
	String popstr = "";
	LinkedStack<Object> st=new LinkedStack<Object>();
	System.out.println("Size            Contents");
	System.out.println(st);
	st.push(new String("Ireland"));
	System.out.println(st);
	popstr+=st.pop().toString()+"  ";
	System.out.println(st);
	st.push(new String("England"));
	System.out.println(st);
	popstr+=st.pop().toString()+"  ";
	System.out.println(st);
	st.push(new String("Wales"));
	System.out.println(st);
	popstr+=st.pop().toString()+"  ";
	System.out.println(st);
	st.push(new String("Scotland"));
	System.out.println(st);
	popstr+=st.pop().toString()+"  ";
	System.out.println(st);
	st.push(new String("France"));
	System.out.println(st);
	st.push(new String("Germany"));
	System.out.println(st);
	
	System.out.println("\n\n popped countries are:"+popstr);
	}


	public static void main(String[] args) {
		System.out.println("A2:");
		A2();
		System.out.println("A3:");
		A3();
	}
		
	}


