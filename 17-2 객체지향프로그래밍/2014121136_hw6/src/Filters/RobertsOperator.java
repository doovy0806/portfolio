package Filters;
import IKImage.*;

public class RobertsOperator extends DerivativeOperator{
	public RobertsOperator() {
		super("Roberts");
		this.setKernel(3);
	}
	
	protected void setKernel(int n) {
		for(int i =0; i<n; i++) {
			for(int j=0; j<n; j++) {
				this.kernel[i][j] =0;
				
			}
		}
		this.kernel[0][0] =-1;
		this.kernel[1][1] = 1;
		for(int i =0; i<n; i++) {
			for(int j=0; j<n; j++) {
				this.kernel2[i][j] =0;
				
			}
		}
		this.kernel2[0][2] =-1;
		this.kernel2[1][1] = 1;
	}
	


}
