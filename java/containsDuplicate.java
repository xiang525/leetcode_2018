public class Solution 
{
    public boolean containsDuplicate(int[] nums) 
    {
        
        Set<Integer> set = new HashSet<Integer>();
        for(int i:nums)
        	if (!set.add(i))
        		return true;
        	else
        		return false;
        

    }
}

// java 中注意如何定义set