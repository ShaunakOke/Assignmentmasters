package impl;

import java.lang.reflect.Array;
import java.util.Random;

import core.List;
import core.Position;
import java.lang.Math;
public class SortingUtils {
	@SuppressWarnings("unchecked")
	public static void singleDigitBucketSort(List<Integer> list) {
		List<Integer>[] buckets = (List<Integer>[]) Array.newInstance(List.class, 10);
		
		// Step 1: Copy the values from the list into the buckets.
		while (!list.isEmpty()) {
			int value = list.remove(list.first());
			if (value < 0 || value > 9) throw new UnsortableException("The list contains an invalid value: " + value);
			if (buckets[value] == null) {
				buckets[value] = new LinkedList<Integer>();
			}
			buckets[value].insertLast(value);
		}
		
		// Step 2: Copy the values from the buckets to the list.
		for (int i=0; i < buckets.length; i++) {
			if (buckets[i] != null) {
				while (!buckets[i].isEmpty()) {
					list.insertLast(buckets[i].remove(buckets[i].first()));
				}
			}
		}
		
	}

	public static void integerBucketSort(List<Integer> list, int lower, int upper) {
		if(lower>upper) throw new RuntimeException("lower cannot be greater than upper value");
		List<Integer>[] buckets = (List<Integer>[]) Array.newInstance(List.class, upper-lower+1);
		while (!list.isEmpty()) {
			int value = list.remove(list.first());
			//simply allow more values and set proper bucket index
			if (value < lower || value > upper) throw new UnsortableException("The list contains an invalid value: " + value);
			if (buckets[value-lower] == null) {
				buckets[value-lower] = new LinkedList<Integer>();
				}
				buckets[value-lower].insertLast(value);
			}
			for (int i=0; i < buckets.length; i++) {
				if (buckets[i] != null) {
					while (!buckets[i].isEmpty()) {
						list.insertLast(buckets[i].remove(buckets[i].first()));
						}
					}
			}
			System.out.println("Bucket sort: \n"+list);
	}
	
	public static void integerRadixSort(List<Integer> list, int digits) {
		//Assign in bins in multiple passes . one pass per digit.
		if(digits<1) throw new RuntimeException("Need maximum digits instead got negative digits");
		List<Integer>[] buckets = (List<Integer>[]) Array.newInstance(List.class, 10);
		for(int s=0;s<digits;s++){
			while (!list.isEmpty()) {
				int value = list.remove(list.first());
				if (value >= Math.pow(10,digits) || value < 0) throw new UnsortableException("The list contains an invalid value: " + value);
				int valindice=(value/(int)(Math.pow(10, s)))%10;
				if (buckets[valindice] == null) {
					buckets[valindice] = new LinkedList<Integer>();
					}
					buckets[valindice].insertLast(value);
				}
				for (int i=0; i < buckets.length; i++) {
					if (buckets[i] != null) {
						while (!buckets[i].isEmpty()) {
							list.insertLast(buckets[i].remove(buckets[i].first()));
						}
					}
				}
		}
			System.out.println("Radix integer sort \n"+list);
	}
	
	public static void stringRadixSort(List<String> list, int digits) {
		if(digits<1) throw new RuntimeException("Cant sort negative length string");
		List<String>[] buckets = (List<String>[]) Array.newInstance(List.class, 26);
		buckets[0] = new LinkedList<String>(); //initialize an extra list incase of unbalanced string lengths
		for(int s=digits-1;s>=0;s--){
			while (!list.isEmpty()) {
				String value = list.remove(list.first());
				if(value.length()>s)
				{
					//use char ASCII value for indexing and assigning buckets
				if ((value.charAt(s))<97  || (value.charAt(s))>122) throw new UnsortableException("The list contains an invalid value: " + value);
				if (buckets[value.charAt(s)-97] == null) {
					buckets[value.charAt(s)-97] = new LinkedList<String>();
					}
					buckets[value.charAt(s)-97].insertLast(value);
				}
				else
				{
					//insert at start if lower than the current length index 
					//since its a small string more chances of being at start
					buckets[0].insertLast(value);		
				}
			}
			for (int i=0; i < buckets.length; i++) {
				if (buckets[i] != null) {
					while (!buckets[i].isEmpty()) {
						list.insertLast(buckets[i].remove(buckets[i].first()));
						}
					}
				}
			}
		System.out.println("Radix string sort \n"+list);
	}

public static void ibsTest()
{
	Random rand = new Random(); 
	List<Integer> list = new LinkedList<Integer>();
	for(int i=0;i<500;i++)
	{
	list.insertLast(rand.nextInt(201)+50);
	}
	System.out.println("list for bucketsort 50-250\n"+list);	
	integerBucketSort(list,50,250);
	
}
public static void irsTest()
{
	Random rand = new Random();
	List<Integer> list2 = new LinkedList<Integer>();
	for(int i=0;i<500;i++)
		{
			list2.insertLast(rand.nextInt(1000));
		}
	System.out.println("\n \n \nlist for radix sort 0-999\n"+list2);
	integerRadixSort(list2,3);
}
public static void srsTest()
{
	List<String> list3= new LinkedList<String>();
	list3.insertLast("the");
	list3.insertLast("big");
	list3.insertLast("black");
	list3.insertLast("cat");
	list3.insertLast("sat");
	list3.insertLast("on");
	list3.insertLast("the");
	list3.insertLast("beautiful");
	list3.insertLast("brown");
	list3.insertLast("mat");
	System.out.println("\n \nString for sorting taken:\n"+list3);
	stringRadixSort(list3,9);
}

public static void main(String args[])
{
	ibsTest();
	irsTest();
	srsTest();
}

}
