// IKImage: IKImage class library for loading, saving, modifying, and displaying jpg image
// by In-Kwon Lee (iklee@yonsei.ac.kr) October 27, 2017.

package IKImage;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.*;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.ImageIcon; 
import javax.swing.SwingUtilities;
import javax.swing.JLabel;

public class IKImage {
	
	   public final static int RED = 0;
	   public final static int GREEN = 1; 
	   public final static int BLUE = 2; 
	
	   protected BufferedImage  image;
	   protected int width;
	   protected int height;
	   protected int type; 
	   protected String name; 
	   
	   // Constructors
	   public IKImage() { }  // default constructor
	   
	   public IKImage(String fileName) { // load an image file and make image 
		   loadImage(fileName);
	   }
	   
	   // make an empty image (width x size) with given type
	   public IKImage(int width, int height, int type) { 
		   this.width = width;
		   this.height = height; 
		   this.type = type; 
		   this.name = "noname.jpg";
		   image = new BufferedImage(width, height, type);
	   }
	   
	// constructor with size, type, and name
	   public IKImage(int width, int height, int type, String name) { 
		   this(width, height, type);
		   this.name = name; 
	   }
	   
	   public IKImage(IKImage ikImage) {  // copy constructor
		   this(ikImage.width, ikImage.height, ikImage.getType());
		   this.width = ikImage.width;
		   this.height = ikImage.height; 
		   name = "noname.jpg";
		   image = new BufferedImage(width, height, ikImage.image.getType());
		   for (int i = 0; i < height; i++) 
			   for (int j = 0; j < width; j++) {
				   int red = ikImage.getPixel(i, j, IKImage.RED);
				   int green = ikImage.getPixel(i, j, IKImage.GREEN);
				   int blue = ikImage.getPixel(i, j, IKImage.BLUE);
				   setPixelColor(i, j, red, green, blue);
			   }
	   }
	   
	   public IKImage(IKImage ikImage, String name) { // copy constructor with new name
		   this(ikImage);
		   this.name = name; 
	   }
	   
	   // set and get methods
	   
	   public void setWidth(int width) {
		   this.width = width; 
	   }
	   
	   public void setHeight(int height) {
		   this.height = height; 
	   }
	   
	   public void setType(int type) {
		   this.type = type; 
	   }
	   
	   public void setName(String name) {
		   this.name = name; 
	   }
	   
	   public int getWidth() {
		   return width;
	   }
	   
	   public int getHeight() {
		   return height; 
	   }
	   
	   public int getType() {
		   return type; 
	   }
	   
	   public String getName() {
		   return name; 
	   }
	   
	   // set the color of specific pixel (row, column) in the image
	   public void setPixelColor(int row, int column, int red, int green, int blue) {
           Color newColor = new Color(red, green, blue); 
           image.setRGB(column, row, newColor.getRGB());
	   }
	   
	   public int getPixel(int row, int column, int chan) {
           Color c = new Color(image.getRGB(column, row)); 
           int color = 0; 
           switch (chan) {
               case IKImage.RED: color = (int)c.getRed(); break;
               case IKImage.GREEN: color = (int)c.getGreen(); break;
               case IKImage.BLUE: color = (int)c.getBlue(); 
           }
           return color; 
	   }
	   	   
	   // Methods
	   public void loadImage(String fileName) {
		      try {
		          File input = new File(fileName);
		          image = ImageIO.read(input);
		          width = image.getWidth();
		          height = image.getHeight();
		          type = image.getType(); 
		          name = fileName; 
		      } catch (Exception e) {
		    	  	System.out.println("Image file loading error...");
		    	  	System.exit(1);
		      }
	   }
	   
	   public void saveImage() {
		   saveImage(name);
	   }
	   
	   public void saveImage(String fileName) {
		   try { 
		         File ouptut = new File(fileName);
		         ImageIO.write(image, "jpg", ouptut);
		      } catch (Exception e) {
		    	  	System.out.println("Image file saving error...");
		    	  	System.exit(1);
		      }
	   }
	   
	   public void show() {
		   SwingUtilities.invokeLater(new Runnable() {
			   public void run() {
				   JFrame frame = new JFrame(name); 
				   frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
				   ImageIcon imgIcon = new ImageIcon(image);
				   JLabel lbl = new JLabel();
				   lbl.setIcon(imgIcon);
				   frame.getContentPane().add(lbl,BorderLayout.CENTER);
				   frame.pack();
				   frame.setLocationRelativeTo(null);
				   frame.setVisible(true);
			   }
		   });
	   }
	   
	   public String toString() {
		   return "IKImage(" + name + "): " + width + " x " + height;
	   }
}
