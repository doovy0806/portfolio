package Filters;

import IKImage.*;
import java.util.*;
import java.math.*;

public class GaussianFilter extends Non_DerivativeKernelFilter {

	protected double sigma;
	
	 GaussianFilter(){
		super("Gaussian");
		this.sigma = 5.5;
	}
	public GaussianFilter(int n){
		super("Gaussian", n);
		this.sigma = 5.5;
		this.setKernel(n);

	}
	public GaussianFilter(int n, double sigma){
		super("Gaussian",n);
		this.sigma = sigma;
		this.setKernel(n);
		
	}
	public void setSigma(double sigma) {
		this.sigma = sigma;
	}
	public double getSigma() {
		return this.sigma;
	}
	
	public void setKernel(int n) {
		double kernelSum =0;
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				int newI = i- n/2;
				int newJ = j-n/2;
				this.kernel[i][j]= ((double)(1/(sigma*sigma*2*Math.PI	) )*Math.exp(- (newI*newI+newJ*newJ)/(2*sigma*sigma)));
				kernelSum+=this.kernel[i][j];
			}
		}	
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				this.kernel[i][j] /= kernelSum;
			}
		}
		
	}
	

	
}
