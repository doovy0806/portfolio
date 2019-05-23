package Filters;
import IKImage.*;

public class BoxFilter extends Non_DerivativeKernelFilter{
	BoxFilter(){
		super("Box", 3);
	}
	public BoxFilter( int n){
		super("Box", n);
		this.setKernel(n);
	}
	public void setKernel(int n) {
		n = this.n;
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				this.kernel[i][j] = (double)1 /(n*n);
			}
		}
	}

}
