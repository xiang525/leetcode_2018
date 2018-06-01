public class Solution 
{
    public List<List<Integer>> generate(int numRows) 
    {
        ArrayList<ArrayList<Integer>> ans = new ArrayList<ArrayList<Integer>>();
        if(numRows==0)
        	return ans;
        ArrayList<Integer> last = new ArrayList<Integer>();
        last.add(1);
        ans.add(last);
        for(int r = 2; r<=numRows;r++) //前两行不用进行如下计算
        {
        	ArrayList<Integer> row = new ArrayList<Integer>();
        	row.add(1);
        	for(int j=1;j<=r-2;j++)
        		row.add(last.get(j-1)+last.get(j));
        	row.add(1);
        	last = row;
        	ans.add(last);
        }
    }
    return ans;
}


//这道题比较简单，属于基础的数组操作。基本思路是每层保存前一行的指针，然后当前航数据根据上一行来得到，
//每个元素就是上一行两个相邻元素相加（第一个和最后一个元素是1）。算法时间复杂度应该是O(1+2+3+...+n)=O(n^2)，
//空间上只需要二维数组来存储结果，不需要额外空间.
//此方法cost extra space


public class Solution 
{
    public List<Integer> getRow(int rowIndex) 
    {
        ArrayList<Integer> row = new ArrayList<Integer>();
        for (int r = 0;r<=rowIndex;r++)
        {
        	for (int j=r-1;j>=1;j--)
        		row.set(j,row.get(j-1)+row.get(j));
        	row.add(1);  //所有的计算都是从1开始的， 所以不满足条件的就set=1.
        }
        return row;
    }

}


// 这道题跟Pascal's Triangle很类似，只是这里只需要求出某一行的结果。Pascal's Triangle中因为是求出全部结果，
//以我们需要上一行的数据就很自然的可以去取。而这里我们只需要一行数据，就得考虑一下是不是能只用一行的空间来存储结果
//不需要额外的来存储上一行呢？这里确实是可以实现的。对于每一行我们知道如果从前往后扫，第i个元素的值等于上一行的
//res[i]+res[i+1]，可以看到数据是往前看的，如果我们只用一行空间，那么需要的数据就会被覆盖掉。所以这里采取的方
//法是从后往前扫，这样每次需要的数据就是res[i]+res[i-1]，我们需要的数据不会被覆盖，因为需要的res[i]只在当前步
//用，下一步就不需要了。这个技巧在动态规划省空间时也经常使用，主要就是看我们需要的数据是原来的数据还是新的数据来
//决定我们遍历的方向。时间复杂度还是O(n^2)，而空间这里是O(k)来存储结果，仍然不需要额外空间。

//?? 没想明白为什么被覆盖




















