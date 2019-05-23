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
		//배열을 무작위로 선택하기 위한 랜덤 배열 선택
		
		
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
		
	

		
		
//		각 호차 잘 입력됐는지 확인하는 주석		
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
		System.out.println("** 1열차 (1:30) **");
		System.out.println("-- 1호차(특) -- "+'\t'+"--- 2호차 --- "+'\t'+'\t'+"--- 3호차 ---");
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
			
		System.out.println("** 2열차 (2:30) **");
		System.out.println("-- 1호차(특) -- "+'\t'+"--- 2호차 --- "+ '\t' +'\t' +"--- 3호차 ---");
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

			System.out.println("** 3열차 (3:30) **");
			System.out.println("-- 1호차(특) -- " + '\t'+ "--- 2호차 --- " + '\t' +'\t'+"--- 3호차 ---");
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
			System.out.println("열차 검색 시작 시간은 (1~3)?");
			startTime = s.nextInt();
			if(startTime==-1) {
				printTrain(train);
				return false;				
			}
			System.out.println("열차 검색 끝 시간은 (1~3)?");
			endTime = s.nextInt();
			if(endTime==-1) {
				printTrain(train);
				return false;				
			}
			
			
			switch (startTime) {
			//시작시간이 1시일때
			case 1:
				switch(endTime-startTime) {
				//시작시간이 4시
				case 3:
					System.out.println("1열차(1:30) 특실("+seatLeft[0][0]+"), 일반실("+seatLeft[0][1]+")");
					System.out.println("2열차(2:30) 특실("+seatLeft[1][0]+"), 일반실("+seatLeft[1][1]+")");
					System.out.println("3열차(3:30) 특실("+seatLeft[2][0]+"), 일반실("+seatLeft[2][1]+")");
					break;
				case 2:
					System.out.println("1열차(1:30) 특실("+seatLeft[0][0]+"), 일반실("+seatLeft[0][1]+")");
					System.out.println("2열차(2:30) 특실("+seatLeft[1][0]+"), 일반실("+seatLeft[1][1]+")");
					break;
				case 1:
					System.out.println("1열차(1:30) 특실("+seatLeft[0][0]+"), 일반실("+seatLeft[0][1]+")");
					break;
				default:
					continue;
				}
				break;
			case 2:
				switch(endTime-startTime) {
				case 2:
					System.out.println("2열차(2:30) 특실("+seatLeft[1][0]+"), 일반실("+seatLeft[1][1]+")");
					System.out.println("3열차(3:30) 특실("+seatLeft[2][0]+"), 일반실("+seatLeft[2][1]+")");
					break;
				case 1:
					System.out.println("2열차(2:30) 특실("+seatLeft[1][0]+"), 일반실("+seatLeft[1][1]+")");
					break;
				default : 
					continue;
				
				}
			case 3:
				switch(endTime-startTime) {
				case 1:
					System.out.println("3열차(3:30) 특실("+seatLeft[2][0]+"), 일반실("+seatLeft[2][1]+")");
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
		//특정 좌석의 인덱스
		String wantedSeat;
		
		System.out.println("원하는 열차 번호를 입력하세요:");
		wantedTrain = s.nextInt();
		if(wantedTrain==-1) {
			printTrain(train); return false;
		}
		System.out.println("특실(1)/일반실(2) 여부를 입력하세요:");
		
		wantedCoach =  s.nextInt();
		if(wantedCoach==-1) {
			printTrain(train); return false;
		}
		System.out.println("정방향(1)/역방향(2) 여부를 입력하세요:");
		wantedDirection = s.nextInt();
		if(wantedDirection==-1) {
			printTrain(train); return false;
		}
		System.out.println("창측(1)/복도측(2) 여부를 입력하세요:");
		wantedSide = s.nextInt();
		if(wantedSide==-1) {
			printTrain(train); return false;
		}
		wi = wantedTrain-1;
		if (wantedCoach==1) {
			//wj=0, 즉 특실인데  - 창측 복도측만 은 1행 2행만 있고 정방향만 있음!! wk가 0이거나 1인 경우
			wj=0;
			if(wantedDirection==2) { //역방향 예약한 경우 - wk가 2,3은 없으니까..
				System.out.println("예약에 실패하였습니다.");
				return true;
			}else {//wk가 0,1인경우
				if(wantedSide==1) {//창측인 경우 wl이 0이거나 3인경우
					for(wk=0; wk<2; wk++) {
						for(wl=0; wl<4; wl+=3) {
							if(!train[wi][wj][wk][wl].equals("X ")) {
								System.out.printf("%d열차 (%d:30) %d호차 좌석 %s",wi+1,wi+1,wj+1,train[wi][wj][wk][wl]);
								train[wi][wj][wk][wl] = "X ";
								seatLeft[wi][wantedCoach-1]--;
								return true;
								
							}
						}
					}
					
				}else {//복도측인경우 즉 wl이 1이거나 2인경우
					for(wk=0;wk<2;wk++) {
						for(wl=1; wl<3; wl++) {
							if(!train[wi][wj][wk][wl].equals("X ")) {
								System.out.printf("%d열차 (%d:30) %d호차 좌석 %s \n",wi+1,wi+1,wj+1,train[wi][wj][wk][wl]);
								train[wi][wj][wk][wl] = "X ";
								seatLeft[wi][wantedCoach-1]--;
								return true;
							}
						}
					}
					
				}
			}
		}else if(wantedCoach==2) {//wj=1~3,일반실
			for(wj=1; wj<4; wj++) {
				wk = wantedDirection*2-2; //wk 정방향이 1이면 0부터, 역방향인 2이면 2부터 시작해서 2번만 반복
				for(int t=0;t<2;t++,wk++) {
					if(wantedSide==1) {//창측이었으면
						for(wl=0;wl<4;wl+=3) {
							if(!train[wi][wj][wk][wl].equals("X ")) {
								System.out.printf("%d열차 (%d:30) %d호차 좌석 %s \n",wi+1,wi+1,wj+1,train[wi][wj][wk][wl]);
								train[wi][wj][wk][wl] = "X ";
								seatLeft[wi][wantedCoach-1]--;
								return true;
							}
						}
					}else if(wantedSide==2) {
						for(wl=1; wl<3; wl++) {
							if(!train[wi][wj][wk][wl].equals("X ")) {
								System.out.printf("%d열차 (%d:30) %d호차 좌석 %s \n",wi+1,wi+1,wj+1,train[wi][wj][wk][wl]);
								train[wi][wj][wk][wl] = "X ";
								seatLeft[wi][wantedCoach-1]--;
								return true;
							}
						}
				
					}
				}
			}
		}
			
			
			
		System.out.println("예약에 실패하였습니다.");
		return true;

	}
}
