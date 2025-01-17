/*Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]*/

import java.util.Scanner;

public class Products_Of_Array_Except_self{
    
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int ar[]= new int[5];
        int op[]= new int[5];
        int n=ar.length;
        for (int i = 0; i < n; i++) 
        {
            op[i] = 1;
        }
        for(int i=0;i<n;i++)
        {
            System.out.println("Enter element into array");
            ar[i]=sc.nextInt();
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(i!=j)
                {
                    op[i]*=ar[j];
                }
                
            }
            System.out.println(op[i]);
        }
    }

}


