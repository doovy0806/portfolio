
public class Oophw3 {
	public static void main(String args[]) {
		final int SMALL =10000;
		final int MEDIUM = 12000;
		final int LARGE = 15000;
		
		Yomino pizza1 = new Yomino();
		Yomino pizza2 = new Yomino("YOM2", MEDIUM, 2,2,0);
		
		pizza1.setName("YOM1");
		pizza1.setSize(LARGE);
		pizza1.setNumCheeseTop(2);
		pizza1.setNumHamTop(1);
		
		pizza1.printYomino();
		pizza2.printYomino();
		
		pizza1.setNumPepTop(3);
		pizza2.setSize(SMALL);
		
		pizza1.printYomino();
		pizza2.printYomino();
		
		PizzaOrder order1 = new PizzaOrder();
		order1.setName("O1");
		order1.setNumPizza(2);
		order1.yomino[0] = pizza1;
		order1.yomino[1] = pizza2;
		order1.calcTotal();
		order1.printOrder();
		
		PizzaOrder order2 = new PizzaOrder("O2", 3);
		order2.yomino[0] = pizza1;
		order2.yomino[1] = pizza2;
		order2.yomino[2] = new Yomino("YOM3", LARGE, 1, 1, 2);
		order2.calcTotal();
		order2.printOrder();
		
	}
}

class Yomino{
	String name;
	int size;
	String stringSize;
	final int SMALL = 10000;
	final int MEDIUM = 12000;
	final int LARGE = 15000;
	int numCheeseTop, numPepTop, numHamTop;
	int cost;
	
	Yomino(){
		
	}
	
	Yomino(String name, int size, int numCheeseTop, int numPepTop, int numHamTop){
		this.name = name;
		this.size = size;
		switch(size) {
		case SMALL:
			this.stringSize = "SMALL";
			break;
		case MEDIUM:
			this.stringSize = "MEDIUM";
			break;
		case LARGE:
			this.stringSize = "LARGE";
			break;
		default:
			break;
		}
		this.numCheeseTop = numCheeseTop;
		this.numHamTop = numHamTop;
		this.numPepTop = numPepTop;
		
		this.cost = this.calCost();
	}
	
	public String getName() {
		return this.name;
	}
	public void setName(String name) {
		this.name = name;
	}
	
	public void setSize(int size) {
		this.size = size;
		switch(size) {
		case SMALL:
			this.stringSize = "SMALL";
			break;
		case MEDIUM:
			this.stringSize = "MEDIUM";
			break;
		case LARGE:
			this.stringSize = "LARGE";
			break;
		default:
			break;
			
		}
		this.calCost();
	}
	public int getSize() {
		return this.size;
	}
	
	public int getNumCheeseTop() {
		return this.numCheeseTop;
	}
	public int getNumHamTop() {
		return this.numHamTop;
	}
	public int getNumPepTop() {
		return this.numPepTop;
	}
	
	public void setNumCheeseTop(int numCheeseTop) {
		this.numCheeseTop = numCheeseTop;
		this.calCost();
	}
	public void setNumHamTop(int numHamTop) {
		this.numHamTop = numHamTop;
		this.calCost();
	}
	public void setNumPepTop(int numPepTop) {
		this.numPepTop = numPepTop;
		this.calCost();
	}
	
	public int getCost() {
		return this.cost;
	}
	public int calCost() {
		this.cost = this.size + (1000*(this.numCheeseTop+this.numHamTop+this.numPepTop));
		return this.cost;
	}
	
	public void printYomino() {
		System.out.println("YOMINO ("+this.name+") "+this.stringSize+" cost: "+this.cost+
				" Cheese("+this.numCheeseTop+") Pep("+this.numPepTop+") Ham("+this.numHamTop+")");
		
	}
	
}


class PizzaOrder{
	String name;
	int numPizza;
	int totalCost;
	Yomino[] yomino;
	
	PizzaOrder(){
		this.yomino = new Yomino[3];
		for(int i=0;i<3;i++) {
			yomino[i] = new Yomino();
		}
	}
	
	PizzaOrder(String name, int numPizza) {
		this.name = name;
		this.numPizza = numPizza;
		this.yomino = new Yomino[3];
		for(int i=0;i<numPizza;i++) {
			yomino[i] = new Yomino();
		}
	}
	
	public String getName() {
		return this.name;
	}
	public void setName(String name) {
		this.name = name;
	}
	
	public int getNumPizza() {
		return this.numPizza;
	}
	public void setNumPizza(int numPizza) {
		this.numPizza = numPizza;
	}
	public int getTotalCost() 	{
		return this.totalCost;
	}
	public int calcTotal() {
		int total =0;
		for(int i =0; i<yomino.length; i++) {
			
			if(yomino[i]!=null) { 
				
				total+=yomino[i].cost;
			
			}
		}
		this.totalCost = total;
		return total;
	}
	public void printOrder() {
		System.out.println("");
		System.out.printf("ORDER(%s) #Pizzas:%d total cost: %d\n", this.name, this.numPizza, this.totalCost);
		for(int i=0; i<this.numPizza; i++) {
			yomino[i].printYomino();
		}
		
	}
	
}