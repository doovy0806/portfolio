// IKDraw2D: simple 2D graphic class
// written by In-Kwon Lee (iklee@yonsei.ac.kr)  Nov 19, 2017

package Shapes;

import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.Ellipse2D;
import javax.swing.JFrame;
import javax.swing.JPanel;

class IKDraw2DSurface extends JPanel {
	int nShape = 0; 
	Shape[] shape = null; 
	int sizeX = 100;
	int sizeY = 100; 
	
	public IKDraw2DSurface() { } 
	public IKDraw2DSurface(int sizeX, int sizeY, int nShape, Shape[] shape) {
		this.sizeX = sizeX; 
		this.sizeY = sizeY; 
		this.nShape = nShape; 
		this.shape = shape; 
	}
	
	private void doDrawing(Graphics g) {
		Graphics2D g2d = (Graphics2D) g; 
        g2d.setPaint(new Color(150, 150, 150));  // background color

        RenderingHints rh = new RenderingHints(
                RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        rh.put(RenderingHints.KEY_RENDERING,
               RenderingHints.VALUE_RENDER_QUALITY);

        g2d.setRenderingHints(rh);

		for (int i = 0; i < nShape; i++) {
			switch (shape[i].type) {
				case "SQUARE":
					Square square = (Square) shape[i]; 
					g2d.drawRect((int)square.lowLeft.x, 
								 sizeY - (int)(square.lowLeft.y + square.width), 
								 (int)square.width, (int)square.width); 
					break; 
				case "RECTANGLE":
					Rectangle rect = (Rectangle) shape[i]; 
					g2d.drawRect((int)rect.lowLeft.x, 
							     sizeY - (int)(rect.lowLeft.y + rect.height), 
							     (int)rect.width, (int)rect.height); 
					break;
				case "TRIANGLE":
				case "R-TRIANGLE":
					Triangle tri = (Triangle) shape[i];
					int xPoints[] = { (int)tri.p[0].x, (int)tri.p[1].x, (int)tri.p[2].x }; 
					int yPoints[] = { sizeY - (int)tri.p[0].y, sizeY - (int)tri.p[1].y, 
									  sizeY - (int)tri.p[2].y }; 
					g2d.drawPolygon(xPoints, yPoints, 3);
					break;
				case "CIRCLE":
					Circle circ = (Circle) shape[i]; 
					g2d.drawArc((int)(circ.center.x - circ.radius), 
							    sizeY - (int)(circ.center.y + circ.radius), 
							    	(int)(circ.radius * 2.0), (int)(circ.radius * 2.0), 0, 360); 
					break; 
				case "ELLIPSE":
					Ellipse elli = (Ellipse) shape[i]; 
					g2d.drawArc((int)(elli.center.x - elli.radius), 
						    sizeY - (int)(elli.center.y + elli.radius2), 
						    	(int)(elli.radius * 2.0), (int)(elli.radius2 * 2.0), 0, 360); 
					break; 
				case "POLYGON":
					Polygon poly = (Polygon) shape[i]; 
					int nPoints = poly.getNPoints();
					int[] xP = new int[nPoints];
					int[] yP = new int[nPoints];
					for (int j = 0; j < nPoints; j++) {
						xP[j] = (int) poly.p[j].x;
						yP[j] = sizeY - (int) poly.p[j].y;
					}
					g2d.drawPolygon(xP, yP, nPoints);
					break; 
			} /* switch */
		} /* for i */
	} /* doDrawing */
	
	@Override
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		doDrawing(g);
	}
}

public class IKDraw2D extends JFrame {
	int sizeX = 500; 
	int sizeY = 500; 
	IKDraw2DList list; 

	public IKDraw2D(int sizeX, int sizeY, IKDraw2DList list) { 
		add(new IKDraw2DSurface(sizeX, sizeY, list.nShape, list.shape));
		setTitle("IKDraw2D");
		setSize(sizeX, sizeY);
		setLocationRelativeTo(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.sizeX = sizeX; 
		this.sizeY = sizeY; 
		this.list = list; 
	}
	
	public void drawAll() {
		
        EventQueue.invokeLater(new Runnable() {
            
            @Override
            public void run() {
                IKDraw2D ex = new IKDraw2D(sizeX, sizeY, list);
                ex.setVisible(true);
            }
        });
		
	}

}
