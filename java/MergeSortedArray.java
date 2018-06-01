public class MergeSortedArray 
{
    public void merge(int[] nums1, int m, int[] nums2, int n) 
    {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        for (;i>=0 && j>=0;k--)
        {
        	if(nums1[i] > nums2[j])
        	{
        		nums1[k] = nums1[i];
        		i--;
        	}        		
        	else
        	{
        		nums1[k] = nums2[j];
        		j--;
        	}
        		
        }
        while (j >=0)   // when nums2 is longer than nums1
        	nums1[k--] = nums2[j--];
    }
}


// to not use extra space, we still use nums1 to store the sorted elements.
// Thus, we need to store elements from the end to the beginning.
// a good solutoin can be found here: 
// http://fisherlei.blogspot.com/2012/12/leetcode-merge-sorted-array.html