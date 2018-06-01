public class Solution 
{
    public int removeDuplicates(int[] nums) 
    {
        if (nums.length==0)
        	return 0;
        int j = 1;
        for(int i = 1; i < nums.length;i++)
        {
        	if (nums[i]!=nums[j-1])
        	{
        	    nums[j] = nums[i];
        	    j++;
        	}
        }
        return j;
    }
}


// the key point is not using extra space thus two arrays are not allowed to use.
//解题思路：使用一个指针j，当i向后遍历数组时，如果遇到与A[j]不同的，将A[i]和A[j+1]交换，
//同时j=j+1，即j向后移动一个位置，然后i继续向后遍历。
// remember this solution

