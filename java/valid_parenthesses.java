import java.util.Stack;

public class valid_parenthesses 
{
    public boolean isValid(String s) 
    {
    	Stack<Character> stack = new Stack<Character>();  //Looking at the documentation for Stack you see Stack<E> 
														  //This means that the <E> specifies the data type that is to 
    	                                                  //be held in the Stack. In your example it is the class Character. 
    	for(int i = 0; i < s.length(); i++)
    	{
    		char c = s.charAt(i);
    		
    		if (c =='('||c =='['||c =='{')
    			stack.push(c);
    		else if (stack.isEmpty())
    			return false;
    		else
    		{	
    			char top = stack.pop(); // must pop() one for judgement.
    			if(c==')' && top!='(')
    				return false;    			
	    		if(c=='['  && top!=']')
	    			return false;
	    		if(c=='{'   && top!='}')
	    			return false;
    		} 
    		

    	}
    	
    	
    	return stack.isEmpty();      
    }


	public static void main(String[] args)
	{
		valid_parenthesses a = new valid_parenthesses();
		
		System.out.println(a.isValid("()"));
	}

}


// [解题思路]
// 经典的栈匹配。一个栈，左符号入栈，右符号出栈。最后检查栈是否为空。


