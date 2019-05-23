package txtFileReaderWriter;

import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.NoSuchElementException;

public class TXTFileReader {
	protected Scanner inputStream = null;
	protected String filename; 
	
	public TXTFileReader(String filename) {
		this.filename = filename;
		try {
			inputStream = new Scanner(new FileInputStream(filename));
		}
		catch (FileNotFoundException e) {
			System.out.println("File " + filename + " was not found");
			System.out.println("or could not be opened.");
			System.exit(0);
		}
	}
	
	public String readString() {
		String str; 
		try {
			str = inputStream.next(); 
		}
		catch(NoSuchElementException e) {
			return null; 
		}
		return str;
	}
	
	public String readLine() {
		String line; 
		try {
			line = inputStream.nextLine(); 
		}
		catch(NoSuchElementException e) {
			return null;
		}
		return line;
	}
	
	public void close() {
		inputStream.close();
	}
}
