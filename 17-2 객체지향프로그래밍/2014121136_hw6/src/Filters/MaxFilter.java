package Filters;
import IKImage.*;

public class MaxFilter extends Non_KernelFilter {

	MaxFilter(){
		super("Max", 3);
	}
	public MaxFilter(int n) {
		super("Max", n);
	}
	
	@Override
	protected int getPixelValue(int[][] arr) {
		// TODO Auto-generated method stub
		int [] sortedArr = super.sortPixels(arr);
		int size = sortedArr.length;
		return sortedArr[size-1];
	}

}
