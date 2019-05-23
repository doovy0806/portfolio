package city;

public class GeneralCity extends City {
	Province province;
	public GeneralCity(){
		super();
	}
	public GeneralCity(String name, int population, double area, String kind, Province province){
		super(name, population, area, kind);
		this.province = province;
	}
	
	void setProvince(Province province) {
		this.province = province;
	}
	Province getProvince() {
		return this.province;
	}
	
	public String toString() {
		return "GENERAL_CITY"+ super.toString()+" province:"+this.province.getName()+" population:"+this.population+" area:"+this.area;
	}
}
