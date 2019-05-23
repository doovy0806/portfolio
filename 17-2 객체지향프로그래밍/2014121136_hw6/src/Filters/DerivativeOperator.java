package Filters;

import IKImage.*;
public abstract class DerivativeOperator extends KernelFilter {
//	protected double[][] kernel1;
	protected double[][] kernel2;
	
	
	DerivativeOperator(){
		super("Derivative",3);
		this.kernel2 = new double[3][3];
	}
	protected DerivativeOperator(String type) {
		super(type, 3);
		this.kernel2 = new double[3][3];
	}
	
	public IKImage greyScale(IKImage ikiIn) {
		for(int i=0; i<ikiIn.getHeight(); i++) {
			for(int j=0; j<ikiIn.getWidth(); j++) {
				int red = ikiIn.getPixel(i,j, 0);
				int green = ikiIn.getPixel(i,j, 1);
				int blue = ikiIn.getPixel(i,j, 2);
				int avg = (red+green+blue)/3;
				ikiIn.setPixelColor(i, j, avg, avg, avg);
			}
		}
		return ikiIn;
	}
	protected int absolute(int d) {
		return d> 0? d :  -d;
	}
	
	public IKImage filterImage(IKImage ikiIn, IKImage ikiOut) {	
		IKImage ikigrey = new IKImage(ikiIn);
		ikigrey = this.greyScale(ikigrey);
		for(int i=0; i<ikiIn.getHeight(); i++) {
			for(int j=0; j<ikiIn.getWidth(); j++) {
				
						int red=0;
						int green=0;
						int blue=0;
					
						int red1 = 0;
						int green1 = 0;
						int blue1 = 0;
						int red2 = 0;
						int green2 = 0;
						int blue2 = 0;
						for(int k =0; k<n; k++) { 
							for(int l = 0; l<n; l++) {
								if(i-(n/2)+k<0||j-(n/2)+l<0||i-(n/2)+k>=ikigrey.getHeight()||j-(n/2)+l>=ikigrey.getWidth()) {
									red1 += (this.kernel[k][l])*(ikigrey.getPixel(i, j, 0));
									green1  += (this.kernel[k][l])*(ikigrey.getPixel(i, j, 1));
									blue1 += (this.kernel[k][l])*(ikigrey.getPixel(i, j, 2));
									
									red2 += (this.kernel2[k][l])*(ikigrey.getPixel(i, j, 0));
									green2  += (this.kernel2[k][l])*(ikigrey.getPixel(i, j, 1));
									blue2 += (this.kernel2[k][l])*(ikigrey.getPixel(i, j, 2));
									
									
															
								
								}else {
									red1 += (this.kernel[k][l]*(ikigrey.getPixel(i-(n/2)+k, j-(n/2)+l, 0)));
									green1 += (this.kernel[k][l]*(ikigrey.getPixel(i-(n/2)+k, j-(n/2)+l, 1)));
									blue1 += (this.kernel[k][l]*(ikigrey.getPixel(i-(n/2)+k, j-(n/2)+l, 2)));
									
									red2 += (this.kernel2[k][l]*(ikigrey.getPixel(i-(n/2)+k, j-(n/2)+l, 0)));
									green2 += (this.kernel2[k][l]*(ikigrey.getPixel(i-(n/2)+k, j-(n/2)+l, 1)));
									blue2 += (this.kernel2[k][l]*(ikigrey.getPixel(i-(n/2)+k, j-(n/2)+l, 2)));
								}
								
								
							}
						}
						red = this.absolute(red1)+this.absolute(red2);
						red = red>= 255? 255 : (red<0? 0 : red);
						green = this.absolute(green1)+this.absolute(green2);
						green = green>= 255? 255 : (green<0? 0 : green);
						blue = this.absolute(blue1)+this.absolute(blue2);
						blue = blue>= 255? 255 : (blue<0? 0 : blue);
						ikiOut.setPixelColor(i, j, red, green, blue);
					
					}
			}
		return ikiOut;
	
		}
	
	protected abstract void setKernel(int n);
	public String kernel2ToString() {
		String str ="{";
		for(int i=0; i<n; i++) {
			str+=" {";
					for(int j =0; j<n; j++) {
						str+=kernel2[i][j]+", ";
					}
			str+="}, \n";
		}
		return str+=" }";
	}
}
