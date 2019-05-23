package Filters;
import IKImage.*;

public class MinFilter extends Non_KernelFilter{
	MinFilter(){
		super("Min",3);
	}
	public MinFilter(int n){
		super("Min", n);
	}
	
	protected int getPixelValue(int[][] arr) {
		int[] sortedArr = super.sortPixels(arr);
		return sortedArr[0];		
	}
}
