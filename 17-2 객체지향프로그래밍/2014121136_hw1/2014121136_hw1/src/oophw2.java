import java.util.Scanner;
public class oophw2 {
	static String[][][][] train = new String[3][3][4][4];
	static int[][] seatLeft = { {0,0}, {0,0}, {0,0}};

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		String[][][][] train = new String[3][3][4][4];
//		int[][] seatLeft = { {0,0}, {0,0}, {0,0}};
		Scanner sc = new Scanner(System.in);
		
		
		int[] randArr1 = {0,1,2,3};
		int[] randArr2 = {0,1,2,3};
		//�迭�� �������� �����ϱ� ���� ���� �迭 ����
		
		
		for(int i =0; i<4; i++) {
			int rand = (int)(Math.random()*4);
			int temp = randArr1[rand];
			randArr1[rand] = randArr1[i];
			randArr1[i] = temp;
			rand = (int)(Math.random()*4);
			temp = randArr2[rand];
			randArr2[rand] = randArr2[i];
			randArr2[i] = temp;
		}
		for(int i = 0; i<train.length; i++) {
			for(int j=0; j<train[0].length; j++) {
				for(int k=0; k<train[0][0].length; k++) {
					for(int l=0; l<train[0][0][0].length; l++ )
					    train[i][j][k][l] = ""+(k+1)+((char)('A'+l));
					
				}
			}
		}
		
		for(int i = 0; i<seatLeft.length; i++) {
			for(int j=0; j<seatLeft[0].length; j++) {
				switch (j) {
					case 0:
						seatLeft[i][j] = 8;
						break;
					case 1: 
						seatLeft[i][j] = 32;
						break;
				}
			}
		}
		
		
		for(int i = 0; i<train.length; i++) {
			
			for(int j=0; j<train[0].length; j++) {
				for(int t=0; t<9; t++) {
					int mr1 = (int)(Math.random()*4);
					int mr2 = (int)(Math.random()*4);
					if(!train[i][j][mr1][mr2].equals("X ")) {
						train[i][j][mr1][mr2] = "X ";
					
						switch (j) {
						case 0:
							seatLeft[i][0]--;
							break;
						case 1:
							seatLeft[i][1]--;
							break;
								
						case 2:
							seatLeft[i][1]--;
							break;
								
						case 3:
							seatLeft[i][1]--;
							break;
								
						
							}
							
						
					}
					
					
				}
				
			}
			for(int j = 0; j<1; j++) {
				for(int k=2; k<4; k++) {
					for(int l=0; l<4; l++) {
						if(train[i][j][k][l].equals("X ")) seatLeft[i][0]++;
						train[i][j][k][l]="   ";
					}
				}
			}

		}

		printTrain(train);
		boolean book;
		do {
			book = bookSeat();
			printTrain(train);
		}while(book);
//		System.out.println(""+seatLeft[0][0]+seatLeft[0][1]+seatLeft[1][0]+seatLeft[1][1]+seatLeft[2][0]+seatLeft[2][1]);
		
	

		
		
//		�� ȣ�� �� �Էµƴ��� Ȯ���ϴ� �ּ�		
//		for(int i = 0; i<train.length; i++) {
//			for(int j=0; j<train[0].length; j++) {
//				for(int k=0; k<train[0][0].length; k++) {
//					for(int l=0; l<train[0][0][0].length; l++){
//						System.out.print(train[i][j][k][l]+" ");
//					}
//					System.out.println("");
//
//				}
//				System.out.println("");
//			}
//			System.out.println("");
//		}
//		for(int a:randArr1) {
//			System.out.print(a+ " ");
//		}
//		for(int a:randArr2) {
//			System.out.print(a+ " ");
//		}
//
//
	}
	
	static void printTrain(String[][][][] a) {
		System.out.println("** 1���� (1:30) **");
		System.out.println("-- 1ȣ��(Ư) -- "+'\t'+"--- 2ȣ�� --- "+'\t'+'\t'+"--- 3ȣ�� ---");
			for(int k=0; k<a[0][0].length; k++) {
				for(int j=0; j<a[0].length ;j++) {
					for(int l=0; l<a[0][0][0].length; l++) {
						System.out.print(a[0][j][k][l]+" ");
					}
				System.out.print("\t");	
				
			}
			System.out.println("");
				
		}
		System.out.println("");
			
		System.out.println("** 2���� (2:30) **");
		System.out.println("-- 1ȣ��(Ư) -- "+'\t'+"--- 2ȣ�� --- "+ '\t' +'\t' +"--- 3ȣ�� ---");
			for(int k=0; k<a[1][0].length; k++) {
				for(int j=0; j<a[1].length ;j++) {
					for(int l=0; l<a[1][0][0].length; l++) {
						System.out.print(a[1][j][k][l]+" ");
					}
				System.out.print("\t");	
				
			}
			System.out.println("");
				
		}
			System.out.println("");

			System.out.println("** 3���� (3:30) **");
			System.out.println("-- 1ȣ��(Ư) -- " + '\t'+ "--- 2ȣ�� --- " + '\t' +'\t'+"--- 3ȣ�� ---");
				for(int k=0; k<a[2][0].length; k++) {
					for(int j=0; j<a[2].length ;j++) {
						for(int l=0; l<a[2][0][0].length; l++) {
							System.out.print(a[2][j][k][l]+" ");
						}
				    	System.out.print("\t");	
					
				}
				System.out.println("");
					
			}
				System.out.println("");

			
			
		
	}
	static boolean bookSeat() {
		int startTime ;
		
		int endTime;
		Scanner s = new Scanner(System.in);
		
		do {
			System.out.println("���� �˻� ���� �ð��� (1~3)?");
			startTime = s.nextInt();
			if(startTime==-1) {
				printTrain(train);
				return false;				
			}
			System.out.println("���� �˻� �� �ð��� (1~3)?");
			endTime = s.nextInt();
			if(endTime==-1) {
				printTrain(train);
				return false;				
			}
			
			
			switch (startTime) {
			//���۽ð��� 1���϶�
			case 1:
				switch(endTime-startTime) {
				//���۽ð��� 4��
				case 3:
					System.out.println("1����(1:30) Ư��("+seatLeft[0][0]+"), �Ϲݽ�("+seatLeft[0][1]+")");
					System.out.println("2����(2:30) Ư��("+seatLeft[1][0]+"), �Ϲݽ�("+seatLeft[1][1]+")");
					System.out.println("3����(3:30) Ư��("+seatLeft[2][0]+"), �Ϲݽ�("+seatLeft[2][1]+")");
					break;
				case 2:
					System.out.println("1����(1:30) Ư��("+seatLeft[0][0]+"), �Ϲݽ�("+seatLeft[0][1]+")");
					System.out.println("2����(2:30) Ư��("+seatLeft[1][0]+"), �Ϲݽ�("+seatLeft[1][1]+")");
					break;
				case 1:
					System.out.println("1����(1:30) Ư��("+seatLeft[0][0]+"), �Ϲݽ�("+seatLeft[0][1]+")");
					break;
				default:
					continue;
				}
				break;
			case 2:
				switch(endTime-startTime) {
				case 2:
					System.out.println("2����(2:30) Ư��("+seatLeft[1][0]+"), �Ϲݽ�("+seatLeft[1][1]+")");
					System.out.println("3����(3:30) Ư��("+seatLeft[2][0]+"), �Ϲݽ�("+seatLeft[2][1]+")");
					break;
				case 1:
					System.out.println("2����(2:30) Ư��("+seatLeft[1][0]+"), �Ϲݽ�("+seatLeft[1][1]+")");
					break;
				default : 
					continue;
				
				}
			case 3:
				switch(endTime-startTime) {
				case 1:
					System.out.println("3����(3:30) Ư��("+seatLeft[2][0]+"), �Ϲݽ�("+seatLeft[2][1]+")");
					break;
				default : 
					continue;
				}
				break;
			default: continue;					
			}
			
			
		}while(!(startTime>0 && endTime<5 && startTime<endTime));
		
		int wantedTrain;
		int wantedCoach;
		int wantedDirection;
		int wantedSide;
		
		int wi, wj, wk,wl;
		//Ư�� �¼��� �ε���
		String wantedSeat;
		
		System.out.println("���ϴ� ���� ��ȣ�� �Է��ϼ���:");
		wantedTrain = s.nextInt();
		if(wantedTrain==-1) {
			printTrain(train); return false;
		}
		System.out.println("Ư��(1)/�Ϲݽ�(2) ���θ� �Է��ϼ���:");
		
		wantedCoach =  s.nextInt();
		if(wantedCoach==-1) {
			printTrain(train); return false;
		}
		System.out.println("������(1)/������(2) ���θ� �Է��ϼ���:");
		wantedDirection = s.nextInt();
		if(wantedDirection==-1) {
			printTrain(train); return false;
		}
		System.out.println("â��(1)/������(2) ���θ� �Է��ϼ���:");
		wantedSide = s.nextInt();
		if(wantedSide==-1) {
			printTrain(train); return false;
		}
		wi = wantedTrain-1;
		if (wantedCoach==1) {
			//wj=0, �� Ư���ε�  - â�� �������� �� 1�� 2�ุ �ְ� �����⸸ ����!! wk�� 0�̰ų� 1�� ���
			wj=0;
			if(wantedDirection==2) { //������ ������ ��� - wk�� 2,3�� �����ϱ�..
				System.out.println("���࿡ �����Ͽ����ϴ�.");
				return true;
			}else {//wk�� 0,1�ΰ��
				if(wantedSide==1) {//â���� ��� wl�� 0�̰ų� 3�ΰ��
					for(wk=0; wk<2; wk++) {
						for(wl=0; wl<4; wl+=3) {
							if(!train[wi][wj][wk][wl].equals("X ")) {
								System.out.printf("%d���� (%d:30) %dȣ�� �¼� %s",wi+1,wi+1,wj+1,train[wi][wj][wk][wl]);
								train[wi][wj][wk][wl] = "X ";
								seatLeft[wi][wantedCoach-1]--;
								return true;
								
							}
						}
					}
					
				}else {//�������ΰ�� �� wl�� 1�̰ų� 2�ΰ��
					for(wk=0;wk<2;wk++) {
						for(wl=1; wl<3; wl++) {
							if(!train[wi][wj][wk][wl].equals("X ")) {
								System.out.printf("%d���� (%d:30) %dȣ�� �¼� %s \n",wi+1,wi+1,wj+1,train[wi][wj][wk][wl]);
								train[wi][wj][wk][wl] = "X ";
								seatLeft[wi][wantedCoach-1]--;
								return true;
							}
						}
					}
					
				}
			}
		}else if(wantedCoach==2) {//wj=1~3,�Ϲݽ�
			for(wj=1; wj<4; wj++) {
				wk = wantedDirection*2-2; //wk �������� 1�̸� 0����, �������� 2�̸� 2���� �����ؼ� 2���� �ݺ�
				for(int t=0;t<2;t++,wk++) {
					if(wantedSide==1) {//â���̾�����
						for(wl=0;wl<4;wl+=3) {
							if(!train[wi][wj][wk][wl].equals("X ")) {
								System.out.printf("%d���� (%d:30) %dȣ�� �¼� %s \n",wi+1,wi+1,wj+1,train[wi][wj][wk][wl]);
								train[wi][wj][wk][wl] = "X ";
								seatLeft[wi][wantedCoach-1]--;
								return true;
							}
						}
					}else if(wantedSide==2) {
						for(wl=1; wl<3; wl++) {
							if(!train[wi][wj][wk][wl].equals("X ")) {
								System.out.printf("%d���� (%d:30) %dȣ�� �¼� %s \n",wi+1,wi+1,wj+1,train[wi][wj][wk][wl]);
								train[wi][wj][wk][wl] = "X ";
								seatLeft[wi][wantedCoach-1]--;
								return true;
							}
						}
				
					}
				}
			}
		}
			
			
			
		System.out.println("���࿡ �����Ͽ����ϴ�.");
		return true;

	}
}
