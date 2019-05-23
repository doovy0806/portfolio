package Exceptions;

public class EvenNumberException extends Exception{
	public EvenNumberException(){
	    super("홀수만 입력 가능합니다.");	
	}
	public  EvenNumberException(String msg){
		super(msg);
	}

}
