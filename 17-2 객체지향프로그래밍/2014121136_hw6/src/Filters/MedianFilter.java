package Filters;
import IKImage.*;

public class MedianFilter extends Non_KernelFilter{
	MedianFilter(){
		super();
	}
	public MedianFilter(int n){
		super("Median", n);
	}
	
	protected int getPixelValue(int[][] arr) {
		int[] sortedArr = super.sortPixels(arr);
		int size = sortedArr.length;
		return sortedArr[size/2];
	}

}
