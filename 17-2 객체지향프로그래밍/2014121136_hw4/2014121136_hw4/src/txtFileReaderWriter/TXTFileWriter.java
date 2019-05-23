package txtFileReaderWriter; 

import java.io.PrintWriter;
import java.io.FileOutputStream;
import java.io.FileNotFoundException;

public class TXTFileWriter {
	protected PrintWriter outputStream = null;
	protected String filename = null;
	
	public TXTFileWriter(String filename) {
		this.filename = filename; 
		try {
			outputStream = new PrintWriter(new FileOutputStream(filename));
		}
		catch (FileNotFoundException e) {
			System.out.println("Error opening the file " + filename);
			System.exit(0);
		}
	}
	
	public void write(int x, boolean newLine) {
		if (newLine) outputStream.println(x); 
		else outputStream.print(x);
	}
	
	public void write(double d, boolean newLine) {
		if (newLine) outputStream.println(d);
		else outputStream.print(d);
	}
	
	public void write(String s, boolean newLine) {
		if (newLine) outputStream.println(s);
		else outputStream.print(s);
	}
	
	public void write(char c, boolean newLine) {
		if (newLine) outputStream.println(c);
		else outputStream.print(c);
	}
	
	public void close() {
		outputStream.close(); 
	}
}
