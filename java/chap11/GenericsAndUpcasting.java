/*
 * Please read ApplesAndOrangesWithGenerics.java first.
 */

import java.util.*;

class Base {	
}
class Derv_1 extends Base {	
}
class Derv_2 extends Base {	
}
class Derv_3 extends Base {	
}
class Derv_4 extends Base {	
}
class SecondOrder extends Derv_4 {	
}
public class GenericsAndUpcasting {
	public static void main(String[] args) {
		ArrayList<Base> baseList = new ArrayList<Base>();
		baseList.add(new Base());
		baseList.add(new Derv_1());
		baseList.add(new Derv_2());
		baseList.add(new Derv_3());
		baseList.add(new Derv_4());
		baseList.add(new SecondOrder());
		
		for(Base c : baseList)
			System.out.println(c);
	}
}

/*
 * Thus, you can add a subtype of Apple to a container that is specified to hold Apple objects.
 * The output is produced from the default toString() method of Object, which prints the class name
 * followed by the unsigned hexadecimal representation of the hash code of the object (generated by the hashCode() method).
 * 
 * Please read Must_Read_2.txt next
 */
