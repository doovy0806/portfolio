import Filters.*;
import IKImage.*;

public class Homework6 {
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		IKImage image = new IKImage("bro.jpg");
		
		
		IKImage[] images = new IKImage[17];
		for(int i=0; i<17; i++) {
			if(i<3) {
				images[i] = new IKImage(image, "bro_box_"+(4*i+3)+".jpg");
			}else if(i<6) {
				images[i] = new IKImage(image, "bro_gaussian_"+(4*(i-3)+3)+".jpg");
			}else if( i==6) {
				images[i] = new IKImage(image, "bro_sobel.jpg");
			}else if(i==7) {
				images[i] = new IKImage(image, "bro_roberts.jpg");
			}else if(i<11) {
				images[i] = new IKImage(image, "bro_median_"+(4*(i-8)+3)+".jpg");
			}else if(i<14) {
				images[i] = new IKImage(image, "bro_min_"+(4*(i-11)+3)+".jpg");
			}else if(i<17) {
				images[i] = new IKImage(image, "bro_max_"+(4*(i-14)+3)+".jpg");
			}
		}
		
		Filter [] filters = new Filter[17];
		for(int i=0; i<17; i++) {
		
			if(i<3) {
				filters[i] = new BoxFilter(4*i+3);
			}else if(i<6) {
				filters[i] = new GaussianFilter(4*(i-3)+3);
			}else if( i==6) {
				filters[i] = new SobelOperator();
			}else if(i==7) {
				filters[i] = new RobertsOperator();
			}else if(i<11) {
				filters[i] = new MedianFilter(4*(i-8)+3);
			}else if(i<14) {
				filters[i] = new MinFilter(4*(i-11)+3);
			}else if(i<17) {
				filters[i]= new MaxFilter(4*(i-14)+3);
			}
		}
		
		for(int i=0; i<17; i++) {
			images[i] = filters[i].filterImage(image, images[i]);
			images[i].saveImage();
		}


	}
	

}
