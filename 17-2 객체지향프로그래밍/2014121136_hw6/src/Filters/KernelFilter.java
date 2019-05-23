package Filters;

import IKImage.*;
import Exceptions.*;

public abstract class KernelFilter extends Filter{
	protected double[][] kernel;
	KernelFilter(){
		super("Kernel", 3);
	}
	KernelFilter(String type){
		super(type, 3);
	}
	protected KernelFilter(String type, int n){
		super(type,n);		
		this.kernel = new double[n][n];
	}
	public abstract IKImage filterImage(IKImage ikiIn, IKImage ikiOut);
	
	public String kernelToString() {
		String str ="{";
		for(int i=0; i<n; i++) {
			str+=" {";
					for(int j =0; j<n; j++) {
						str+=kernel[i][j]+", ";
					}
			str+="}, \n";
		}
		return str+=" }";
	}

}
