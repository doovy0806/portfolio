package Filters;
import IKImage.*;

public class SobelOperator extends DerivativeOperator {
	public SobelOperator() {
		super("Sobel");
		this.setKernel(3);
	}
	
	protected void setKernel(int n) {
		for(int i=0; i<3; i++) {
			for(int j=0; j<3;j++) {
				kernel[i][j] = 1;
				if(j==1) kernel[i][j] = 2;
				if(i==1) kernel[i][j] = 0;
				if(i==0) kernel[i][j] *= -1;
			}
		}
		for(int i=0; i<3; i++) {
			for(int j=0; j<3;j++) {
				kernel2[i][j] = 1;
				if(i==1) kernel2[i][j] = 2;
				if(j==1) kernel2[i][j] = 0;
				if(j==0) kernel2[i][j] *= -1;
			}
		}
		
	}
	
	
}
