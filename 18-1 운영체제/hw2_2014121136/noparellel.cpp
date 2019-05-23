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
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <sstream>
#include <cmath>
#include <ctime>
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
		for(int it = 0; it<iteration[i]; it++) {
			int* points_in_clusters = new int[k_num[i]]();
			//to count the points in each cluster.
			int minindex = 0;
			float prev = -1;
			for (int j = 0; j<n_num[i]; j++) {
				//for each point
				for (int k = 0; k<k_num[i]; k++) {
					//for each mean
					float distance = sqrt((points[i][j].x - mean[i][k].x)*(points[i][j].x - mean[i][k].x) + (points[i][j].y - mean[i][k].y)*(points[i][j].y - mean[i][k].y));
					if (prev<0) {
						//for first distance
						prev = distance;
					}
					else {
						if (prev>distance) {
							//when previous distance is larger than the current one, swap the distance
							prev = distance;

							minindex = k;
						}
					}
				}
				//allocate each point to each cluster


				points[i][j].cluster = minindex;

				// preparing for next loop
				minindex = 0;
				prev = -1;
			}

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

		cout<<"Test Case#"<<i<<endl;
		timespec tse;
		clock_gettime(CLOCK_REALTIME, &tse);


		if(tse.tv_nsec-tss.tv_nsec>0){
				cout<<((long long)tse.tv_nsec-(long long)tss.tv_nsec)/(long long)1000<<" microseconds"<<endl;
			}else{
				cout<<(((long long)tse.tv_nsec-(long long)tss.tv_nsec)+1000000000)/(long long)1000<<" microseconds"<<endl;

			}
//		for(int p=0; p<k_num; p++){
//			cout<<mean[p].x<<", "<<mean[p].y<<endl;
//		}
		for(int p=0; p<n_num[i]; p++){
			cout<<points[i][p].cluster<<endl;
		}
	}

	return 0;
}




