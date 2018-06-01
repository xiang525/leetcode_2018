public class Solution 
{
    public List<String> summaryRanges(int[] nums) 
    {
        List<String> res = new ArrayList<>();
        if(nums==null || nums.length<1) return  res;
        int first = 0, end = 0;
        while(end < nums.length())
        {
        	if (nums[end+1] == nums[end]+1)
        		end++;
        	else
        		if(first!=end)
        		{
        			String str = nums[first]+"->"+nums[end];
        			res.add(str);
        		}        			
        		else
        			res.add(Integer.toString(nums[first]));
        		++end;
        		first = end;
        }
    }

    public static void main(String[] args)
    {
    	Solution a = new Solution();
    	int[] t = {0,1,2,4,5,7};
    	//a.summaryRanges(t);
    	System.out.println(a.summaryRanges(t));
    }
}