package city;

public class City {

	String name;
	int population;
	double area;
	String kind;
	
	public City(){
		this.name="";
		this.population=0;
		this.area=0;
		this.kind="";
		
	}
	public City(String name, int population, double area, String kind){
		this.name= name;
		this.population = population;
		this.area = area;
		this.kind = kind;
	}
	void setName(String name) {
		this.name = name;
		
	}
	void setPopulation(int population) {
		this.population = population;
	}
	void setArea (double area) {
		this.area = area;
	}
	void setKind(String kind) {
		this.kind = kind;
	}
	
	String getName() {
		return this.name;
	}
	int getPopulation() {
		return this.population;
	}
	double getArea() {
		return this.area;
	}
	String getKind() {
		return this.kind;
	}
	
	public String toString() {
		return "("+ this.name+") ["+this.kind+"]";
	}
	
}
