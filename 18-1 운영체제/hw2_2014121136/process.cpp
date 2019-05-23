/*
 * process.cpp
 *
 *  Created on: 2018. 4. 12.
 *      Author: Hanmo
 */
//============================================================================
// Name        : noparellel.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <limits>
#include <sys/time.h>


using namespace std;
class point {
public:
	float x;
	float y;
	int cluster;

};


int main() {
	//	cout << "Hello World!!!" << endl; // prints Hello World!!!

	int testcase = 0;
	cin >> testcase;

	int* iteration = new int [testcase];
	int* k_num = new int[testcase];
	int* n_num = new int[testcase];
	point ** mean;
	mean = new point*[testcase];
	point **points;
	points = new point*[testcase];
	//input all the numbers given
	for (int i = 0; i<testcase; i++) {

		cin >> iteration[i];

		cin >> k_num[i];

		cin >> n_num[i];
		point* apoints;
		apoints= new point[n_num[i]];
		point* amean;
		amean = new point[k_num[i]];

		mean[i] = amean;
		points[i] = apoints;


		// input all the points
		for (int j = 0; j<n_num[i]; j++) {

			float x_num, y_num;
			cin>>x_num>>y_num;
			points[i][j].x = x_num;
			points[i][j].y = y_num;



			if (j<k_num[i]) {
				mean[i][j].x = x_num;
				mean[i][j].y = y_num;
			}
		}
	}
	for(int i=0; i<testcase; i++){
		timespec tss;
		clock_gettime(CLOCK_REALTIME, &tss);// to measure the duration of the whole program

		point *newmean = new point[k_num[i]];


		int shmid_mean, shmid_points, shmid_clusters ;
		shmid_mean = shmget((key_t)5, sizeof(point)*(k_num[i]), IPC_CREAT | 0666);
		shmid_points = shmget((key_t)6, sizeof(point)*n_num[i], IPC_CREAT | 0666);


		//now attach those shared memories to the process
		void* shm_mean = shmat(shmid_mean, (void*)0, 0);
		void* shm_points = shmat(shmid_points, (void*)0, 0);


		point* shared_mean;
		point* shared_points;


		shared_mean = (point*)shm_mean;
		*shared_mean = *mean[i];
		for(int m = 0; m<k_num[i]; m++){
			shared_mean[m] = mean[i][m];
		}
		shared_points = (point*)shm_points;
		*shared_points = *points[i];
		for(int m = 0; m<n_num[i]; m++){
			shared_points[m] = points[i][m];
		}
//		for(int t=0; t<n_num; t++){
//			cout<<"point:"<<t<<" "<<shared_points[t].x<<", "<<shared_points[t].y<<endl;
//		}
		for(int it = 0; it<iteration[i]; it++) {
			int* points_in_clusters = new int[k_num[i]]();
			pid_t pid =  fork();

			if( pid ==0){
				// when it is a child, run k-means clustering for the latter half of the points array
				int minindex = 0;
				float prev = -1;
				shmid_mean = shmget((key_t)5, sizeof(int)*k_num[i], 0);
				shmid_points = shmget((key_t)6, sizeof(point)*n_num[i], 0);

				//check if you have to change 0 to IPC_CREAT|0666
				shm_mean = shmat(shmid_mean, (void*)0, IPC_CREAT|0666);
				shm_points = shmat(shmid_points,(void*)0, IPC_CREAT|0666);

				mean[i] = (point *)shm_mean;
				points[i] = (point *)shm_points;
//				for(int t=0; t<n_num; t++){
//					cout<<"(child process)point:"<<t<<" "<<points[t].x<<", "<<points[t].y<<endl;
//				}
				for (int j = 0; j<n_num[i]/2; j++) {
				//for each point until that has index f (n_num/2-1)
					for (int k = 0; k<k_num[i]; k++) {
					//for each mean
						float distance = sqrt((points[i][j].x - mean[i][k].x)*(points[i][j].x - mean[i][k].x) + (points[i][j].y - mean[i][k].y)*(points[i][j].y - mean[i][k].y));
						if (prev<0) {
							//for first distance
							prev = distance;
//							cout<<"point"<<j<<" distance:"<<distance<<" ,";
						}
						else {
							if (prev>distance) {
							//when previous distance is larger than the current one, swap the distance
								prev = distance;
								minindex = k;
//								cout<<distance<<" ,";

							}
						}

					}
//					cout<<endl;
				//allocate each point to each cluster

					points[i][j].cluster = minindex;
				// preparing for next loop
					minindex = 0;
					prev = -1;
				}
				exit(1);



			}else if(pid>0){
				//when it is a parent
				int minindex = 0;
				float prev = -1;
				mean[i] = (point *)shm_mean;
				points[i] = (point *)shm_points;
//				for(int t=0; t<k_num; t++){
//					cout<<"mean:"<<t<<" "<<mean[t].x<<", "<<mean[t].y<<endl;
//				}
				for (int j = n_num[i]/2; j<n_num[i]; j++) {
				//for each point that has index from n/2
					for (int k = 0; k<k_num[i]; k++) {
					//for each mean
						float distance = sqrt((points[i][j].x - mean[i][k].x)*(points[i][j].x - mean[i][k].x) + (points[i][j].y - mean[i][k].y)*(points[i][j].y - mean[i][k].y));
						if (prev<0) {
						//for first distance
							prev = distance;
//							cout<<"point"<<j<<" distance:"<<distance<<" ,";

						}
						else {
							if (prev>distance) {
							//when previous distance is larger than the current one, swap the distance
								prev = distance;

								minindex = k;
//								cout<<distance<<" ,";

							}
						}
//						cout<<endl;

					}
				//allocate each point to each cluster

					points[i][j].cluster = minindex;
				// preparing for next loop
					minindex = 0;
					prev = -1;
				}
				int status;
				//wait until the other process exits
				wait((int*)1);


			// comparing means with new means

				for(int k=0; k<k_num[i];k++){
					newmean[k].x=0;
					newmean[k].y=0;

				}
				for (int k=0; k<n_num[i]; k++){
					int pointcluster = points[i][k].cluster;
					newmean[pointcluster].x += points[i][k].x;
					newmean[pointcluster].y += points[i][k].y;
					points_in_clusters[pointcluster] ++;
				}
				for(int k=0; k<k_num[i]; k++){
					if(points_in_clusters[k]==0){
						newmean[k].x = numeric_limits<float>::max();
						newmean[k].y = numeric_limits<float>::max();

					}else{
						newmean[k].x /= (float)points_in_clusters[k];
						mean[i][k].x = newmean[k].x;
						newmean[k].y /= (float)points_in_clusters[k];

						mean[i][k].y = newmean[k].y;
					}
				}

			}


		}
		cout<<"Test Case#"<<i<<endl;
		timespec tse;
		clock_gettime(CLOCK_REALTIME, &tse);


		if(tse.tv_nsec-tss.tv_nsec>0){
			cout<<((long long)tse.tv_nsec-(long long)tss.tv_nsec)/(long long)1000<<" microseconds"<<endl;
		}else{
			cout<<(((long long)tse.tv_nsec-(long long)tss.tv_nsec)+1000000000)/(long long)1000<<" microseconds"<<endl;

		}



		for(int p=0; p<n_num[i]; p++){
			cout<<points[i][p].cluster<<endl;

		}
		shmctl(shmid_mean, IPC_RMID,0);
		shmctl(shmid_points,IPC_RMID,0);



	}
	return 0;
}



