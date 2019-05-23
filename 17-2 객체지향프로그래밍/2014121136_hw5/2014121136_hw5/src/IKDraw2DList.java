// IKDraw2DList: simple 2D graphic class
// written by In-Kwon Lee (iklee@yonsei.ac.kr)  Nov 19, 2017

package Shapes;

public class IKDraw2DList {
	int nShape = 0;
	Shape[] shape = null;
	
	public IKDraw2DList() { }
	
	public void addShape(Shape shape) {
		Shape[] temp = this.shape; 
		this.nShape++;
		this.shape = new Shape[this.nShape];
		for (int i = 0; i < this.nShape - 1; i++) 
			this.shape[i] = temp[i]; 
		this.shape[this.nShape - 1] = shape; 
	}
	
	public void drawSquare(Square square) {
		addShape(square);
	}
	
	public void drawRectangle(Rectangle rect) {
		addShape(rect);
	}
	
	public void drawTriangle(Triangle tri) {
		addShape(tri);
	}
	
	public void drawRightTriangle(RightTriangle rtri) {
		addShape(rtri);
	}
	
	public void drawCircle(Circle circ) {
		addShape(circ);
	}
	
	public void drawEllipse(Ellipse ellipse) {
		addShape(ellipse);
	}
	
	public void drawPolygon(Polygon poly) {
		addShape(poly);
	}
}
