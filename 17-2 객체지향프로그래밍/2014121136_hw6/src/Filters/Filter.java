package Filters;

import Exceptions.EvenNumberException;
import IKImage.IKImage;

public abstract class Filter {
	protected int n;
	protected String type;
	
	protected Filter(){
		this.n=3;
		this.type = "Filter";
	}
	
	protected Filter(String type){
		this.type = type;
		this.n= 3;
	}
	protected Filter(String type, int n){
		this.type = type;
		try{
			if(n%2==0) throw new EvenNumberException();
			this.n=n;
		}catch(EvenNumberException e){
			System.out.println(e.getMessage());
		}
	}
	

	public abstract IKImage filterImage(IKImage ikiIn, IKImage ikiOut);	
}
