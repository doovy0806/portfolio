package Filters;
import IKImage.*;

public abstract class Non_DerivativeKernelFilter extends KernelFilter {

	Non_DerivativeKernelFilter() {
		super("Non_DerivateKernelFilter", 3);
	}
	Non_DerivativeKernelFilter(String  type) {
		super(type, 3);
	}

	protected Non_DerivativeKernelFilter(String type, int n) {
		super(type, n);
	}
	
	public IKImage filterImage(IKImage ikiIn, IKImage ikiOut) {

		for(int i=0; i<ikiIn.getHeight(); i++) {
			for(int j=0; j<ikiIn.getWidth(); j++) {
				
						int red=0;
						int green=0;
						int blue=0;
						double dRed = 0;
						double dGreen = 0;
						double dBlue = 0;
						for(int k =0; k<n; k++) { 
							
							for(int l = 0; l<n; l++) {
								if(i-(n/2)+k<0||j-(n/2)+l<0||i-(n/2)+k>=ikiIn.getHeight()||j-(n/2)+l>=ikiIn.getWidth()) {
									dRed += (this.kernel[k][l])*(ikiIn.getPixel(i, j, 0));
									dGreen  += (this.kernel[k][l])*(ikiIn.getPixel(i, j, 1));
									dBlue += (this.kernel[k][l])*(ikiIn.getPixel(i, j, 2));
															
								
								}else {
									dRed += (this.kernel[k][l]*(ikiIn.getPixel(i-(n/2)+k, j-(n/2)+l, 0)));
									dGreen += (this.kernel[k][l]*(ikiIn.getPixel(i-(n/2)+k, j-(n/2)+l, 1)));
									dBlue += (this.kernel[k][l]*(ikiIn.getPixel(i-(n/2)+k, j-(n/2)+l, 2)));
								}
							}
						}
						red = (int)dRed;
						green = (int)dGreen;
						blue = (int)dBlue;
						ikiOut.setPixelColor(i, j, red, green, blue);
					
					}	
			}
		return ikiOut;
		}
	
	public abstract void setKernel(int n);


}
