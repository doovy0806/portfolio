package city;

import txtFileReaderWriter.*;

public class Homework4 {
	
	static private Province[] province = new Province[20];
	static private int numProvince = 0; 
	static private TXTFileReader reader; 
	static private TXTFileWriter writer;
	static int maxIndex = 0;

	// your code here	

	public static void main(String[] args) {
		
		readData();
		writer = new TXTFileWriter("Homework4_output.txt");
		
		for (int i = 0; i < numProvince; i++) {
			writer.write("-------------------------------------------------------", true);
			writer.write(province[i].toString(), true);
		}
		
		writer.write("\n\n==========================================================", true);
		writer.write("City of Highest Population Density", true); 
		City city = highestPopulationDensity(); 
		String tempStr = city.name + " Density: " + city.population / city.area; 
		writer.write(tempStr, true);
		writer.close(); 
	}
	
	static void readData() {
		//txtfilereader 이용해서 데이터 읽어오는 메소드가 되어야 할듯.
		reader = new TXTFileReader("Homework4_data_eng.txt");
		String temp1 ="";
		String temp2 ="";
		String temp3 ="";
		String temp4 = "";
		String line = "";
		int index = 0;
		do {
			temp1 = reader.readString();
			index = provinceContains(temp1);
			temp1 = reader.readString();
			String cityName = temp1;
			temp2 = reader.readString();
			String cityKind = temp2;
			temp3 = reader.readString();
			temp4 = reader.readString();
			int number=0;
			int population = Integer.parseInt(temp3);
			double area = Double.parseDouble(temp4);
			number = province[index].nCity;
//			City tempCity = putCity(temp1, temp2, population, area, index);
			if(!temp2.equals("General")&&!temp2.equals("Special-Self")) {
				String temp5 = reader.readString();
				int nD = Integer.parseInt(temp5);
				
				province[index].city[number] = new SpecialCity(cityName, population, area, cityKind, province[index], nD);
				SpecialCity tempSpecial = (SpecialCity)province[index].city[number]; 
				province[index].setNCity(number+1);;
				for(int i=0; i<nD; i++) {
					String temp6 = reader.readString();
					tempSpecial.setDistrict(temp6, i);
				}
				temp1 =reader.readLine();			
			}else {
				province[index].city[number] = new GeneralCity(cityName, population, area, cityKind, province[index]);
				GeneralCity tempGeneral = (GeneralCity)province[index].city[number];
				province[index].setNCity(number+1);
			}
			
//			System.out.println(province[index].city[number]);
		}while(temp1!=null);
		reader.close();
	
	}
	static City highestPopulationDensity() {
		City highPop = null;
		double density=0;
		double highestDensity=0;
		for (int i=0; i<numProvince; i++) {
			for(int j=0; j<province[i].nCity;j++) {
				density = province[i].city[j].getPopulation()/province[i].city[j].getArea();
				if(density>highestDensity) {
					highestDensity = density;
					highPop = province[i].getCity(j);
				
				}
			}
		}
		return highPop;
	}
	
	static int provinceContains(String s) {
		for(int i=0; i<province.length; i++) {
			if(province[i]!=null&&s.equals(province[i].getName())) return i;
			
		}
		province[maxIndex] = new Province(s);
		numProvince++;
		int temp = maxIndex;
		maxIndex++;
		return temp;
	}
//	static City putCity(String cityName, String kind, int population, double area,  int index) {
//		int number =province[index].nCity;
//		if(kind.equals("General")) {
//			province[index].city[number] = new GeneralCity(cityName, population, area, kind, province[index]);
//			province[index].setNCity(number+1);
//			
//		}else {
//			province[index].city[number] = new SpecialCity(cityName, population, area, kind, province[index], 0);
//			province[index].setNCity(number+1);
//			
//		}
//		return province[index].city[number];
//	}
}
