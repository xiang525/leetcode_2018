import java.util.Arrays;

public class plusOne 
{
    public int[] plusOne(int[] digits) 
    {
            int carry = 1;
            for (int i = digits.length - 1; i >= 0; i--) // implete add from the end of the array
            {
            	if((digits[i]+carry)==10)
            	{
            		digits[i] = 0;
            		carry = 1;
            	}
            	else
            	{
            		digits[i] = digits[i] + carry;
            		carry = 0;
            	}
            }
            if (carry==1)
            {
            	int[] re = new int[digits.length+1];
				System.arraycopy(digits,0,re,1,digits.length);
				re[0] = 1;
				return re;
            }
            else
            	return digits;
    }

    // public static void main(String[] args)
    // {
    // 	plusOne a = new plusOne();
    // 	int[] s = {1,2};
    // 	System.out.println(Arrays.toString(a.plusOne(s)));
    // }
}


   // 整数做加法，进位





