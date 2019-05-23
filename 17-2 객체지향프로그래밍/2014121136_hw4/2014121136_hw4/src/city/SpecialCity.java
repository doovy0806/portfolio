package city;

public class SpecialCity extends GeneralCity{
	int nDistrict;
	String[] district;
	
	public SpecialCity(){
		this.nDistrict = 0;
		this.district = new String[100];
	}
	public SpecialCity(String name, int population, double area, String kind, Province province, int nDistrict){
		super(name, population, area, kind, province);
		this.nDistrict=nDistrict;
		this.district = new String [nDistrict];
		
	}
	
	void setNDistrict(int nDistrict) {
		this.nDistrict = nDistrict;
		
	}
	int getNDistrict() {
		return this.nDistrict;
	}
	void setDistrict(String district, int i) {
		this.district[i] = district;
	}
	String getDistrict(int i) {
	return this.district[i];
	}
	
	public String toString() {
		String ds ="\n\t districts("+this.nDistrict+")";
				
		for(int i = 0; i<nDistrict; i++) {
			ds+="\n\t"+this.district[i];
		}
		return "SPECIAL_CITY("+this.name+") ["+this.kind+"] province:"+this.province.getName()+" poputlation:"+this.population+" area:"+this.area+ds;
	}
	
	
}
