package assign4;
//no import required since same package
public class PCQ4L {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedDeque<String> obj=new LinkedDeque<String>();	
		System.out.println("Size               front<--->Rear");
		System.out.println(obj);
		obj.addFirst(new String("Ireland"));
		System.out.println(obj);
		obj.removeLast();
		System.out.println(obj);
		obj.addLast(new String("England"));
		System.out.println(obj);
		obj.removeFirst();
		System.out.println(obj);
		obj.addLast(new String("Wales"));
		System.out.println(obj);
		obj.addFirst(new String("Scotland"));
		System.out.println(obj);
		obj.addLast(new String("France"));
		System.out.println(obj);
		obj.removeFirst();
		System.out.println(obj);
		obj.removeLast();
		System.out.println(obj);
		obj.addLast(new String("Germany"));
		System.out.println(obj);

		
		
		}

}
