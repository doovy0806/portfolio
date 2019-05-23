package Filters;
import IKImage.*;
import java.util.*;

import Exceptions.EvenNumberException;

public abstract class Non_KernelFilter extends Filter{
	Non_KernelFilter(){
		super("Non_Kernel", 3);
	}
	protected Non_KernelFilter(String type, int n){
		super(type, n);
	}
	
	
	public IKImage filterImage(IKImage ikiIn, IKImage ikiOut) {
		for(int i=0; i<ikiIn.getHeight(); i++) {
			for(int j=0; j<ikiOut.getWidth(); j++) {
				int[][] redArr = new int[n][n];
				int[][] greenArr = new int[n][n];
				int[][] blueArr = new int[n][n];
				for(int k=0; k<n; k++) {
					for(int l=0; l<n; l++) {
						if(i-(n/2)+k<0||j-(n/2)+l<0||i-(n/2)+k>=ikiIn.getHeight()||j-(n/2)+l>=ikiIn.getWidth()) {
							redArr[k][l] = ikiIn.getPixel(i, j, 0);
							greenArr[k][l] = ikiIn.getPixel(i, j, 1);
							blueArr[k][l] = ikiIn.getPixel(i, j, 2);
						}else {
							redArr[k][l] = ikiIn.getPixel(i-(n/2)+k, j-(n/2)+l, 0);
							greenArr[k][l] = ikiIn.getPixel(i-(n/2)+k, j-(n/2)+l, 1);
							blueArr[k][l] = ikiIn.getPixel(i-(n/2)+k, j-(n/2)+l, 2);
						}
						int medianRed = this.getPixelValue(redArr);
						int medianGreen = this.getPixelValue(greenArr);
						int medianBlue = this.getPixelValue(blueArr);
						ikiOut.setPixelColor(i, j, medianRed, medianGreen, medianBlue);
					}
				}
			}
		}
		return ikiOut;
	}

	protected abstract int getPixelValue(int [][] arr);
	
	protected int[] sortPixels(int[][] pixels) {
		int[] sortedArr = new int[n*n];
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				sortedArr[i*n+j] = pixels[i][j];
			}
		}
		Arrays.sort(sortedArr);
		return sortedArr;
	}
	
}
