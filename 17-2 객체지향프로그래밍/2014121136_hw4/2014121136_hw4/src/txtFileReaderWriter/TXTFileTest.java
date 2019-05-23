package txtFileReaderWriter; 

public class TXTFileTest {

	public static void main(String[] args) {
		
		TXTFileReader reader = new TXTFileReader("test.txt");
		String temp; 
		temp = reader.readString(); 
		int x = Integer.parseInt(temp); 
		temp = reader.readString(); 
		int y = Integer.parseInt(temp); 
		temp = reader.readString(); 
		int z = Integer.parseInt(temp); 
		temp = reader.readString(); 
		double d = Double.parseDouble(temp); 
		String s1 = reader.readString();
		String s2 = reader.readString();
		String s3 = reader.readString();
		temp = reader.readLine();   // read out the remaining newline character
		String line1 = reader.readLine();
		String line2 = reader.readLine();
		String line3 = reader.readLine(); 
		String s4 = reader.readString(); 
		if (s4 == null) System.out.println("null read");
		reader.close(); 
		
		TXTFileWriter writer = new TXTFileWriter("out.txt");
		writer.write(x,  false);
		writer.write(" ", false);
		writer.write(y,  true);
		writer.write(z,  true);
		writer.write(d,  true);
		temp = s1 + " " + s2 + " " + s3; 
		writer.write(temp, true);
		writer.write(line1, true);
		writer.write(line2,  true);
		writer.write(line3, true);
		writer.write('B', false);
		writer.write('O', false);
		writer.write('S', true);
		writer.close(); 
	}
	
}
