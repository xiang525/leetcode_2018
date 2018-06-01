import java.util.Arrays;

public class rotate_array
{
    private void reverse(int[] nums,int begin,int end)
    {
        while (begin < end)
        {
            int temp = nums[begin];
            nums[begin] = nums[end];
            nums[end] = temp;
            begin++;
            end--;
        }
    }

    public void rotate(int[] nums, int k) 
    {
        k = k % nums.length;
        reverse(nums,0,nums.length-1);  // why this step must be done fist?
        reverse(nums,0,k-1);
        reverse(nums,k,nums.length-1);
        
    }

    
}