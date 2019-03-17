package assignment3;
//testing array stack on the questions
public class PCQxA {
public static void A2()
{
	String popstr = "";
	Arraystack<Object> st=new Arraystack<Object>();
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
	Arraystack<Object> st=new Arraystack<Object>();
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


