package city;

public class Province {

	String name;
	int nCity;
	City[] city;
	
	public Province(){
		
	}
	public Province(String name){
		this.name = name;
		city = new City[100];
		this.nCity = 0;
	}
	public Province(String name, int nCity){
		this.name = name; this.nCity = nCity;
		city = new City[nCity];
	}
	
	void setName(String name) {
		this.name = name;
	}
	void setNCity(int nCity) {
		this.nCity = nCity;
	}
	void setCity(City city, int i) {
		this.city[i] = city;
	}
	String getName() {
		return this.name;
	}
	int getNCity() {
		return this.nCity;
	}
	City getCity(int i) {
		return this.city[i];
	}
	public String toString() {
		String ct = "";
		for(int i=0; i<nCity; i++) {
			ct+= " "+this.city[i].toString()+"\n";
		}
		
		String stprv ="PROVINCE(" + this.name +")"  +" cities:"+this.nCity+"\n"+ct;
				
		
		return stprv;
	}
	
	
}
