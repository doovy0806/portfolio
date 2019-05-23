// TestImage: Test class for IKImage class library
// by In-Kwon Lee (iklee@yonsei.ac.kr) October 27, 2017.

package IKImage; 

import javax.swing.JFrame;
import javax.swing.JPanel;

public class TestImage extends JPanel{

	public static void main(String[] args) {
		
		IKImage image1 = new IKImage("dip.jpg");  // load first image file using constructor
		IKImage image2 = new IKImage();      	// object for second image file 
		image2.loadImage("brother.jpg");			// load second image file using method
		
		// first output image by size constructor
		IKImage image1out = new IKImage(image1.getWidth(), image1.getHeight(), 
										image1.getType(), "dip_out.jpg"); 
		// second output image by copy constructor
		IKImage image2out = new IKImage(image2, "brother_out.jpg"); 
		
		image1.show();
		image2.show(); 
		
		// make red component of all pixels in the first image zero 
		for (int i = 0; i < image1.getHeight(); i++) {
			for (int j = 0; j < image1.getWidth(); j++) {
				int green = image1.getPixel(i, j, IKImage.GREEN);
				int blue = image1.getPixel(i, j, IKImage.BLUE); 
				image1out.setPixelColor(i, j, 0, green, blue);
			}
		}
		
		// save the output of the first image
		image1out.show(); // showing the first image 
		image1out.saveImage();
		System.out.println(image1out);  // print the image information
		
		// color inversion of the second image
		for (int i = 0; i < image2.getHeight(); i++) {
			for (int j = 0; j < image2.getWidth(); j++) {
				int red = image2.getPixel(i, j, IKImage.RED);
				int green = image2.getPixel(i, j, IKImage.GREEN);
				int blue = image2.getPixel(i, j, IKImage.BLUE); 
				image2out.setPixelColor(i, j, 255 - red, 255 - green, 255 - blue);
			}
		}	
		
		// save the output of the second image
		image2out.saveImage("brother_out.jpg");	// showing the second image
		image2out.show(); 
		System.out.println(image2out); 
	}

}
