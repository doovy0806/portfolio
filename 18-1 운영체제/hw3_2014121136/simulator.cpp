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
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <queue>
#include <deque>
#include <map>
#include <cmath>
#include <tuple>

using namespace std;

class node {
public:
	int* framePid;
	int* frameAlloc;
	bool ifroot = false;
	int blockSize;
	int level;
	bool available = true; // check wheter it is empty or not and whether it is splited or not
	bool ifleaf = true;
	int startFrameIndex;
	int nodePid = -1;
	int nodeAlloc = -1;
	node* left = NULL;
	node* right = NULL;
	node* parent = NULL;
	node(int _blockSize, int _level, node* _parent) {
		blockSize = _blockSize;
		framePid = new int[blockSize];
		frameAlloc = new int[blockSize];
		for (int i = 0; i < blockSize; i++) {
			framePid[i] = -1;
			frameAlloc[i] = -1;
		}
		parent = _parent;
		level = _level;
	}

	void split() {
		available = false;
		ifleaf = false;

		left = new node(blockSize / 2, level + 1, this);
		right = new node(blockSize / 2, level + 1, this);
		for (int i = 0; i < blockSize / 2; i++) {
			(*left).framePid[i] = this->framePid[i];
			(*left).frameAlloc[i] = this->frameAlloc[i];
			(*right).framePid[i] = this->framePid[i + blockSize / 2];
			(*right).frameAlloc[i] = this->frameAlloc[i + blockSize / 2];
		}
		left->startFrameIndex = this->startFrameIndex;
		right->startFrameIndex = this->startFrameIndex + this->blockSize / 2;
	}
	bool ifchild() {
		if (left == NULL) return false;
		else return true;
	}

	bool ifmerge() {

		if (left->ifleaf && left->available && right->ifleaf && right->available) return true;
		else return false;
	}
};


class tree {
public:
	node * root;
	int memorySize;
	tree() {
		root = NULL;
		memorySize = 0;
	}
	tree(int _memorySize) {
		memorySize = _memorySize;
		root = new node(memorySize, 0, NULL);
		root->startFrameIndex = 0;
	}
	void merge() {
		mergeNode(root);
	}
	void mergeNode(node* n) {
		if ((*(*n).left).ifchild()) {
			mergeNode((*n).left);
		}
		if ((*(*n).right).ifchild()) mergeNode((*n).right);
		if ((*n).ifmerge()) {
			(*n).left = NULL;
			(*n).right = NULL;
			(*n).available = true;
			(*n).ifleaf = true;
			for (int i = 0; i < (*n).blockSize; i++) {
				(*n).framePid[i] = -1;
				(*n).frameAlloc[i] = -1;
			}
		}
	}
	node* findPlace(int pageNum) {
		node* n = this->find(root, pageNum);
		return n; //null인 경우 LRU돌려야 함
	}
	node* find(node* n, int pageNum) {

		if (!(n->available && pageNum <= n->blockSize)) {
			if (n->ifchild()) {
				node* returnNode = find(n->left, pageNum);
				if (returnNode == NULL) returnNode = find(n->right, pageNum);
				else return returnNode;
			}
			else {
				return NULL;
			}
		}
		else {
			for (; n->blockSize / 2 >= pageNum;) {
				n->available = false;
				n->ifleaf = false;
				n->split();
				n = n->left;
			}
			return n;
		}
	}
	node* pidAlloc(int pid, int alloc) {
		return findPidAlloc(root, pid, alloc);
	}

	node* findPidAlloc(node* n, int pid, int alloc) {
		if (n->nodePid == pid && n->nodeAlloc == alloc) {
			//현재의 노드가 해당되는 노드인 경우
			return n;
		}
		else {
			//만약 돌리고 있는 노드가 해당되는 노드가 아닐 경우
			node* returnNode = NULL;
			if (n->ifchild()) {
				returnNode = findPidAlloc(n->left, pid, alloc);
				if (returnNode != NULL) {
					return returnNode;
				}
				returnNode = findPidAlloc(n->right, pid, alloc);
				return returnNode;
			}
			//현재 돌리고 있는 노드가 해당되지도 않고, 자식도 없는 경우 null반환
			else return NULL;
		}
	}
	void printSystemtxt(ofstream* system) {
		*system << "|";
		printDFS(root, system);
		*system << endl;
	}
	void printDFS(node* n, ofstream* system) {
		if (!(n->ifchild())) {
			if (n->available) {
				char sep;
				for (int i = 0; i < n->blockSize; i++) {
					if (i == n->blockSize - 1) sep = '|';
					else sep = ' ';
					*system << "---" << sep;
				}
			}
			else {
				char sep;
				for (int i = 0; i < n->blockSize; i++) {
					if (i == n->blockSize - 1) sep = '|';
					else sep = ' ';
					*system << n->nodePid << "#" << n->nodeAlloc << sep;
				}
			}
		}
		else {
			printDFS(n->left, system);
			printDFS(n->right, system);
		}
	}

};

class process {
public:
	int remainQuantum;
	int remainFeed;
	int pid;
	string name;
	int currState = 0; //0:RRQ 1:sleep 2: I/oWait 3: Running
	int sleepQuantum = 0;
	int vmemSize;
	int *instructions;
	int *instructionPara;
	int opIndex = 0;
	int opNum;

	int* pages;
	//where you put allocation id
	int* pageTable;
	//where you put pageframes
	int* pageValid;
	//where you put valid bits for pages

	int allocationCount = 0;
	process() {
		pid = -1;
	}
	process(int _pid, string _name, int _remainQuantum, int _remainFeed, int _vmemSize, int _opNum) {
		pid = _pid;
		name = _name;
		remainQuantum = _remainQuantum;
		remainFeed = _remainFeed;
		opNum = _opNum;
		vmemSize = _vmemSize;
		pageTable = new int[vmemSize];
		pages = new int[vmemSize];
		pageValid = new int[vmemSize];
		for (int i = 0; i < vmemSize; i++) {
			pageTable[i] = -1;
			pages[i] = -1;
			pageValid[i] = 0;
		}
		//초기화 필요!!
		instructions = new int[opNum];
		instructionPara = new int[opNum];
	}


	bool operator==(const process &p)const {
		return (pid == p.pid);
	}

};


int timeQuantum;
int feedSize;
int vmemSize;
int pmemSize;
int totalInputOp = 0;
tree physicalMem;
int cycleCount = 0;

list<int*> LRUlist;

list<process> allProcess;
list<process*> roundRobin;
list<process*> sleepList;
list<process*> IOWaitList;
process *runningProc = NULL;

void feedProcess(list<process>);
process* processMake(int, string);
void allocateMemory(process*, int);
void accessMemory(process*, int);
void releaseMemory(process*, int);
bool quantumCheck(process*);
void LRU();


int main(int argc, char ** argv) {

	string inputFileString(argv[1]);
	//	string inputFileString = "input";
	ifstream openFile(inputFileString.data());
	int totalEventNum, pageSize, feedFreq;
	openFile >> totalEventNum >> timeQuantum >> vmemSize >> pmemSize >> pageSize >> feedFreq >> feedSize;
	cout << totalEventNum << " " << timeQuantum << " " << vmemSize << " " << pmemSize << " " << pageSize << " " << feedFreq << " " << feedSize << endl;


	int pidCount = 0;
	int recentDistribution = 0;

	//physical memory => pmem Size로 설정
	physicalMem = *(new tree(pmemSize));






	//queue<string> eventList;
	//queue<int> eventCycleList;

	list<string> procEvents;
	list<int>procEventCycles;
	list<int>inputEvents;
	list<int>inputEventCycles;

	ofstream schedulertxt;
	schedulertxt.open("scheduler.txt");
	schedulertxt.close();
	ofstream memorytxt;
	memorytxt.open("memory.txt");
	memorytxt.close();




	//processEvent리스트 + 프로세스 사이클 리스트 와 input event리스트 를 따로 만들어서 관리하자. 어


	for (int i = 0; i<totalEventNum; i++) {
		int eventCycle;
		openFile >> eventCycle;
		//		cout<<eventCycle<<endl;

		string str;
		openFile >> str;
		if (str.compare("INPUT") == 0) {
			//INPUT ->pid into array
			inputEventCycles.push_back(eventCycle);
			int inputPid;
			openFile >> inputPid;
			inputEvents.push_back(inputPid);
		}
		else {
			//when it is not INPUT -> push into processmake list
			procEventCycles.push_back(eventCycle);
			procEvents.push_back(str);
		}

	}
	do {
		// feed to every process when cycle is recent distribution + feedFreq
		if (!allProcess.empty() && cycleCount == recentDistribution + feedFreq) {
			feedProcess(allProcess);
			recentDistribution = cycleCount;
		}
		//starting feedSize-cycles

		//1.sleep Proc
		for (list<process*>::iterator pr = sleepList.begin(); pr != sleepList.end(); pr++) {
			process* p = *pr;
			if(p!=NULL) (*p).sleepQuantum--;

		}
		for (list<process*>::iterator pr = sleepList.begin(); pr != sleepList.end(); pr++) {
			process* p = *pr;
			if (p!=NULL&&(*p).sleepQuantum<1) {
				pr = sleepList.erase(pr);
				roundRobin.push_back(p);
				(*p).remainQuantum = timeQuantum;
				(*p).currState = 0;
				if (pr == sleepList.end()) break;

			}
		}

		//2. input IO instructions
		if (!inputEventCycles.empty() && inputEventCycles.front() == cycleCount) {

			int ioPid = inputEvents.front();
			inputEvents.pop_front();
			inputEventCycles.pop_front();
			for (list<process*>::iterator pr = IOWaitList.begin(); pr != IOWaitList.end(); pr++) {
				process* p = *pr;
				if ((*p).pid == ioPid) {
					roundRobin.push_back(p);
					(*p).currState = 0;
					(*p).remainQuantum = timeQuantum;
					IOWaitList.erase(pr);

					break;
				}
			}


		} // 3. process making
		else if (!procEventCycles.empty() && procEventCycles.front() == cycleCount) {

			string newFile = procEvents.front();
			procEvents.pop_front();
			procEventCycles.pop_front();
			//making new process
			process* newProcess = processMake(pidCount, newFile);
			allProcess.push_back(*newProcess);
			//determine whether it is in rr Q or wait list
			roundRobin.push_back(newProcess);
			(*newProcess).currState = 0;
			pidCount++;

		}//done 3
		 //4. now we have to acquire process from round robin if there is no process running
		if (runningProc == NULL) {
			//when there is no process running

			//look for a process available
			int rrSize = roundRobin.size();
			for (int i = 0; i < rrSize; i++) {
				process* p = roundRobin.front();
				if ((*p).remainQuantum != 0 && (*p).remainFeed != 0) {
					runningProc = p;
					(*p).currState = 3;

					schedulertxt.open("scheduler.txt", ios::app);
					schedulertxt << cycleCount << "\t" << (*p).pid << "\t" << p->name << endl;
					schedulertxt.close();
					roundRobin.pop_front();
					break;
				}
				else {
					//if p has no time quantum left - push p back into the rr Q
					roundRobin.push_back(p);
					roundRobin.pop_front();

				}
			}
			//when there is no process available although we checked Roundrobin queue and round robin is not empty,
			//we have to distribute cycles another time
			if (runningProc == NULL && !roundRobin.empty()) {
				//if still, there is no process available for running - then feed all processes and update distribution cycle
				feedProcess(allProcess);
				recentDistribution = cycleCount;
				process* p = roundRobin.front();
				runningProc = p;
				(*p).currState = 3;
				schedulertxt.open("scheduler.txt", ios::app);
				schedulertxt << cycleCount << "\t" << (*p).pid << "\t" << p->name << endl;
				schedulertxt.close();
				roundRobin.pop_front();
			}
			else if (roundRobin.empty() && runningProc == NULL) {
				runningProc = NULL;
			}
		}

		//5. print out the information on system.txt
		ofstream *systemtxt;
		ofstream system;
		if (cycleCount == 0) {

			system.open("system.txt");
			systemtxt = &system;
		}
		else {
			system.open("system.txt", ios::app);
			systemtxt = &system;
		}
		//line1
		if (runningProc != NULL) {
			int index = (*runningProc).opIndex;
			process p = *runningProc;
			*systemtxt << cycleCount << " Cycle: " << "Process#" << (*runningProc).pid << " running code " << (*runningProc).name << " line " << index + 1
				<< "(op " << (*runningProc).instructions[index] << ", arg " << (*runningProc).instructionPara[index] << ")" << endl;
		}
		else {
			*systemtxt << cycleCount << " Cycle: " << endl;
		}
		//line2
		if (roundRobin.empty()) {
			*systemtxt << "RunQueue: Empty" << endl;
		}
		else {
			*systemtxt << "RunQueue: ";
			for (list<process*>::iterator pr = roundRobin.begin(); pr != roundRobin.end(); pr++) {
				process* p = *pr;
				*systemtxt << (*p).pid << "(" << (*p).name << ") ";
			}
			*systemtxt << endl;
		}
		//line3
		*systemtxt << "SleepList: ";
		if (sleepList.empty()) {
			*systemtxt << "Empty" << endl;
		}
		else {
			for (list<process*>::iterator pr = sleepList.begin(); pr != sleepList.end(); pr++) {
				process* p = *pr;
				*systemtxt << (*p).pid << "(" << (*p).name << ") ";

			}
			*systemtxt << endl;
		}
		//line4
		*systemtxt << "IOWait List: ";
		if (IOWaitList.empty()) {
			*systemtxt << "Empty" << endl;
		}
		else {
			for (list<process*>::iterator pr = IOWaitList.begin(); pr != IOWaitList.end(); pr++) {
				process* p = *pr;
				*systemtxt << (*p).pid << "(" << (*p).name << ") ";
			}
			*systemtxt << endl;
		}
		//line5 : physical memory
		physicalMem.printSystemtxt(systemtxt);
		//line6: physical Memory LRU
		(*systemtxt) << "LRU:";
		for (list<int*>::iterator l = LRUlist.begin(); l != LRUlist.end(); l++) {
			(*systemtxt) << " (" << (*l)[0] << ":" << (*l)[1] << ")";
		}
		(*systemtxt) << endl;
		(*systemtxt) << endl;
		(*systemtxt).close();

		//6. instruct a code for the process acquired or, we may have to skip this step
		//I think it might be better to take this action as various functions
		if (runningProc != NULL) {
			int opLine = (*runningProc).opIndex;
			int operation = (*runningProc).instructions[opLine];
			int argument = (*runningProc).instructionPara[opLine];
			(*runningProc).remainFeed--;
			(*runningProc).remainQuantum--;
			ofstream pidtxt;
			int pid = runningProc->pid;
			string pidname = to_string(pid) + ".txt";
			switch (operation) {
			case 0:
				//memory Allocation
				allocateMemory((runningProc), argument);
				if (runningProc->opIndex == 0) {
					pidtxt.open(pidname);
				}
				else {
					pidtxt.open(pidname, ios::app);
				}
				pidtxt << cycleCount << " Cycle#Instruction op " << operation << " arg " << argument << endl;
				pidtxt << "AllocID|";
				for (int i = 0; i < vmemSize; i++) {
					if (runningProc->pages[i] < 0) {
						//when page doesn't have data
						pidtxt << "-";
					}
					else {
						pidtxt << runningProc->pages[i];
					}
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << "Valid  |";
				for (int i = 0; i < vmemSize; i++) {
					pidtxt << runningProc->pageValid[i];
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << endl;
				pidtxt.close();

				(*runningProc).opIndex += 1;


				if ((*runningProc).opIndex >= (*runningProc).opNum) {
					// *** release all pages -
					for (int i = 0; i < runningProc->allocationCount; i++) {
						releaseMemory(runningProc, i);
					}

					//and then close the process
					allProcess.remove((*runningProc));
					runningProc = NULL;
				}
				else if (!quantumCheck(runningProc)) runningProc = NULL;

				break;

			case 1:
				//memory access
				accessMemory((runningProc), argument);
				if (runningProc->opIndex == 0) {
					pidtxt.open(pidname);
				}
				else {
					pidtxt.open(pidname, ios::app);
				}
				pidtxt << cycleCount << " Cycle#Instruction op " << operation << " arg " << argument << endl;
				pidtxt << "AllocID|";
				for (int i = 0; i < vmemSize; i++) {
					if (runningProc->pages[i] < 0) {
						//when page doesn't have data
						pidtxt << "-";
					}
					else {
						pidtxt << runningProc->pages[i];
					}
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << "Valid  |";
				for (int i = 0; i < vmemSize; i++) {
					pidtxt << runningProc->pageValid[i];
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << endl;
				pidtxt.close();

				(*runningProc).opIndex += 1;

				if ((*runningProc).opIndex >= (*runningProc).opNum) {
					// *** release all pages -
					for (int i = 0; i < runningProc->allocationCount; i++) {
						releaseMemory(runningProc, i);
					}
					//and then close the process
					allProcess.remove((*runningProc));
					runningProc = NULL;
				}
				else if (!quantumCheck(runningProc)) runningProc = NULL;



				break;
			case 2:
				//memory release
				releaseMemory((runningProc), argument);
				if (runningProc->opIndex == 0) {
					pidtxt.open(pidname);
				}
				else {
					pidtxt.open(pidname, ios::app);
				}
				pidtxt << cycleCount << " Cycle#Instruction op " << operation << " arg " << argument << endl;
				pidtxt << "AllocID|";
				for (int i = 0; i < vmemSize; i++) {
					if (runningProc->pages[i] < 0) {
						//when page doesn't have data
						pidtxt << "-";
					}
					else {
						pidtxt << runningProc->pages[i];
					}
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << "Valid  |";
				for (int i = 0; i < vmemSize; i++) {
					pidtxt << runningProc->pageValid[i];
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << endl;
				pidtxt.close();

				(*runningProc).opIndex += 1;

				if ((*runningProc).opIndex >= (*runningProc).opNum) {
					// *** release all pages -
					for (int i = 0; i < runningProc->allocationCount; i++) {
						releaseMemory(runningProc, i);
					}
					//and then close the process
					allProcess.remove((*runningProc));
					runningProc = NULL;
				}
				else if (!quantumCheck(runningProc)) runningProc = NULL;
				break;
			case 3:
				// non-memory instruction
				if (runningProc->opIndex == 0) {
					pidtxt.open(pidname);
				}
				else {
					pidtxt.open(pidname, ios::app);
				}
				pidtxt << cycleCount << " Cycle#Instruction op " << operation << " arg " << argument << endl;
				pidtxt << "AllocID|";
				for (int i = 0; i < vmemSize; i++) {
					if (runningProc->pages[i] < 0) {
						//when page doesn't have data
						pidtxt << "-";
					}
					else {
						pidtxt << runningProc->pages[i];
					}
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << "Valid  |";
				for (int i = 0; i < vmemSize; i++) {
					pidtxt << runningProc->pageValid[i];
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << endl;
				pidtxt.close();
				(*runningProc).opIndex += 1;

				if ((*runningProc).opIndex >= (*runningProc).opNum) {

					// *** release all pages -
					for (int i = 0; i < runningProc->allocationCount; i++) {
						releaseMemory(runningProc, i);
					}

					//and then close the process
					allProcess.remove((*runningProc));
					runningProc = NULL;
				}
				else if (!quantumCheck(runningProc)) runningProc = NULL;
				break;
			case 4:
				// sleep
				if (runningProc->opIndex == 0) {
					pidtxt.open(pidname);
				}
				else {
					pidtxt.open(pidname, ios::app);
				}
				pidtxt << cycleCount << " Cycle#Instruction op " << operation << " arg " << argument << endl;
				pidtxt << "AllocID|";
				for (int i = 0; i < vmemSize; i++) {
					if (runningProc->pages[i] < 0) {
						//when page doesn't have data
						pidtxt << "-";
					}
					else {
						pidtxt << runningProc->pages[i];
					}
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << "Valid  |";
				for (int i = 0; i < vmemSize; i++) {
					pidtxt << runningProc->pageValid[i];
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << endl;
				pidtxt.close();
				(*runningProc).opIndex += 1;

				if ((*runningProc).opIndex >= (*runningProc).opNum) {
					//when sleep is the last operation of the process

					// *** release all pages -
					for (int i = 0; i < runningProc->allocationCount; i++) {
						releaseMemory(runningProc, i);
					}
					//and then close the process
					allProcess.remove((*runningProc));
					runningProc = NULL;
				}
				else {
					(*runningProc).sleepQuantum = argument;

					sleepList.push_back(runningProc);
					runningProc = NULL;
				}
				break;
			case 5:
				//io wait
				if (runningProc->opIndex == 0) {
					pidtxt.open(pidname);
				}
				else {
					pidtxt.open(pidname, ios::app);
				}
				pidtxt << cycleCount << " Cycle#Instruction op " << operation << " arg " << argument << endl;
				pidtxt << "AllocID|";
				for (int i = 0; i < vmemSize; i++) {
					if (runningProc->pages[i] < 0) {
						//when page doesn't have data
						pidtxt << "-";
					}
					else {
						pidtxt << runningProc->pages[i];
					}
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << "Valid  |";
				for (int i = 0; i < vmemSize; i++) {
					pidtxt << runningProc->pageValid[i];
					if (i % 4 == 3) pidtxt << "|";
				}
				pidtxt << endl;
				pidtxt << endl;
				pidtxt.close();
				(*runningProc).opIndex += 1;

				if ((*runningProc).opIndex >= (*runningProc).opNum) {
					//when sleep is the last operation of the process

					// *** release all pages -
					for (int i = 0; i < runningProc->allocationCount; i++) {
						releaseMemory(runningProc, i);
					}
					//and then close the process
					allProcess.remove((*runningProc));
					runningProc = NULL;
				}
				else {
					IOWaitList.push_back(runningProc);
					runningProc = NULL;
				}
				break;
			}



		}
		else {

		}
		// at the and of cycle
		cycleCount++;
	} while (!(runningProc == NULL && roundRobin.empty() && sleepList.empty() && IOWaitList.empty() && inputEvents.empty() && procEvents.empty()));




	return 0;
}

void feedProcess(list<process> ap) {
	for (list<process*>::iterator pr = roundRobin.begin(); pr != roundRobin.end(); pr++) {
		(*pr)->remainFeed += feedSize;
		(*pr)->remainQuantum = timeQuantum;
	}
	for (list<process*>::iterator pr = sleepList.begin(); pr != sleepList.end(); pr++) {
		(*pr)->remainFeed += feedSize;
		(*pr)->remainQuantum = timeQuantum;
	}
	for (list<process*>::iterator pr = IOWaitList.begin(); pr != IOWaitList.end(); pr++) {
		(*pr)->remainFeed += feedSize;
		(*pr)->remainQuantum = timeQuantum;
	}
	if (runningProc != NULL) {
		runningProc->remainFeed += feedSize;
		runningProc->remainQuantum = timeQuantum;
	}

}
process* processMake(int pid, string name) {
	ifstream openInputFile(name.data());
	int codeNum;
	openInputFile >> codeNum;
	process *newProcess;
	newProcess = new process(pid, name, timeQuantum, feedSize, vmemSize, codeNum);

	for (int i = 0; i<codeNum; i++) {
		int instruction, parameter;
		openInputFile >> instruction >> parameter;
		(*newProcess).instructions[i] = instruction;
		(*newProcess).instructionPara[i] = parameter;
	}
	totalInputOp += codeNum;

	return newProcess;
}

bool quantumCheck(process* p) {
	if ((*p).remainFeed == 0 || (*p).remainQuantum == 0) {
		roundRobin.push_back(p);
		(*p).remainQuantum = timeQuantum;
		(*p).currState = 0;
		return false;
	}
	else return true;
}
void printPidTxt(process * p) {
	ofstream pidtxt;
	string pname = (*p).name;
	if ((*p).opIndex == 0) {
		pidtxt.open(pname + ".txt");
	}
	else {
		pidtxt.open(pname + ".txt", ios::app);
	}


}
void allocateMemory(process* proc, int pageNum) {
	//finding page index in process page table
	int page_index = -1;
	int pageAvailable = 0;
	for (int i = 0; i < vmemSize; i++) {
		if ((*proc).pages[i] < 0 && page_index<0) {
			page_index = i;
			pageAvailable = 1;
		}
		else if ((*proc).pages[i] < 0) {
			pageAvailable += 1;
			if (pageAvailable >= pageNum) break;
		}
		else { // if pages > 0 즉, 페이지수가 확보되기 전에 연속된 페이지가 잘리고 중간에 못쓰는 페이지를 만나면
			page_index = -1;
			pageAvailable = 0;
		}
	}
	double k = 0;
	int frameSize = 1;
	while (pow(2.0, k) < pageNum) {
		k++;
	}
	frameSize = pow(2.0, k);
	node* n = physicalMem.findPlace(frameSize);
	if (n != NULL) {
		n->nodeAlloc = proc->allocationCount;
		n->nodePid = proc->pid;
		n->available = false;
		for (int i = 0; i < frameSize; i++) {
			//allocate to physical memory
			n->framePid[i] = proc->pid;
			n->frameAlloc[i] = proc->allocationCount;

			if (i < pageNum) {
				//allocate to virtual memory
				proc->pages[page_index + i] = proc->allocationCount;
				proc->pageTable[page_index + i] = n->startFrameIndex + i;
				proc->pageValid[page_index + i] = 1;
			}
		}

		int* tmp = new int[2];
		tmp[0] = proc->pid;
		tmp[1] = proc->allocationCount;
		LRUlist.push_back(tmp);
		ofstream memorytxt("memory.txt", ios::app);
		memorytxt.open("memory.txt", ios::app);
		memorytxt << cycleCount << "\t" << proc->pid << "\t" << proc->allocationCount << "\t" << 0 << endl;
		proc->allocationCount++;
	}
	else {//when they don't have enough frames to save the data
		do {
			LRU();
			n = physicalMem.findPlace(pageNum);
		} while (n == NULL);
		n->nodeAlloc = proc->allocationCount;
		n->nodePid = proc->pid;
		n->available = false;
		for (int i = 0; i < pageNum; i++) {
			//allocate to physical memory

			n->framePid[i] = proc->pid;
			n->frameAlloc[i] = proc->allocationCount;
			if (i < pageNum) {
				//allocate to virtual memory

				proc->pages[page_index + i] = proc->allocationCount;
				proc->pageTable[page_index + i] = n->startFrameIndex + i;
				proc->pageValid[page_index + i] = 1;
			}
		}

		int* tmp = new int[2];
		tmp[0] = proc->pid;
		tmp[1] = proc->allocationCount;
		LRUlist.push_back(tmp);

		ofstream memorytxt;
		memorytxt.open("memory.txt", ios::app);
		memorytxt << cycleCount << "\t" << proc->pid << "\t" << proc->allocationCount << "\t" << 0 << endl;

		proc->allocationCount++;

	}


}

void accessMemory(process* proc, int allocID) {
	int processPid = proc->pid;
	node* n = NULL;
	//page index를 받고
	int page_index = -1;
	int pageNum = 0;
	for (int i = 0; i < vmemSize; i++) {
		if (proc->pages[i] == allocID) {
			page_index = i;
			pageNum += 1;
		}
	}
	page_index = page_index - pageNum + 1;
	//valid bit부터 1인지 확인
	if (proc->pageValid[page_index] == 1) {
		//valid하니까 그대로 접근

		//update lru for the frames
		for (list<int*>::iterator i = LRUlist.begin(); i != LRUlist.end(); i++) {
			if ((*i)[0] == processPid && (*i)[1] == allocID) {
				LRUlist.erase(i);
				int* tmp = new int[2];
				tmp[0] = processPid; tmp[1] = allocID;
				LRUlist.push_back(tmp);
				break;
			}
		}
	}
	else if ((n = physicalMem.findPlace(pageNum)) != NULL) {
		//not valid but there is space available
		int frameSize = n->blockSize;
		n->nodePid = processPid;
		n->nodeAlloc = allocID;
		for (int i = 0; i < frameSize; i++) {
			//allocate to physical memory
			n->framePid[i] = processPid;
			n->frameAlloc[i] = allocID;
			if (i < pageNum) {
				//allocate to virtual memory
				proc->pageValid[page_index + i] = 1;
			}
		}
		n->available = false;
		int* tmp = new int[2];
		tmp[0] = processPid;
		tmp[1] = allocID;
		LRUlist.push_back(tmp);
	}
	else {
		//not valid but there is no space available

		do {
			LRU();
			n = physicalMem.findPlace(pageNum);
		} while (n == NULL);
		int frameSize = n->blockSize;
		n->nodePid = processPid;
		n->nodeAlloc = allocID;
		for (int i = 0; i < frameSize; i++) {
			//allocate to physical memory
			n->framePid[i] = processPid;
			n->frameAlloc[i] = allocID;
			if (i < pageNum) {
				//allocate to virtual memory
				proc->pageValid[page_index + i] = 1;
			}
		}
		n->available = false;
		int* tmp = new int[2];
		tmp[0] = processPid;
		tmp[1] = allocID;
		LRUlist.push_back(tmp);
	}
	ofstream memorytxt;
	memorytxt.open("memory.txt", ios::app);
	memorytxt << cycleCount << "\t" << proc->pid << "\t" << allocID << "\t" << 1 << endl;
}
void releaseMemory(process* proc, int allocID) {
	int processPid = proc->pid;

	//page index를 받고
	int page_index = -1;
	int pageNum = 0;
	for (int i = 0; i < vmemSize; i++) {
		if (proc->pages[i] == allocID) {
			page_index = i;
			pageNum += 1;
		}
	}
	page_index = page_index - pageNum + 1;
	//valid bit부터 1인지 확인
	if (proc->pageValid[page_index] == 1) {
		//valid하니까 그대로 삭제
		node * n = physicalMem.pidAlloc(proc->pid, allocID);
		for (int i = 0; i < n->blockSize; i++) {
			n->framePid[i] = -1;
			n->frameAlloc[i] = -1;
			if (i < pageNum) {
				proc->pages[page_index + i] = -1;
				proc->pageTable[page_index + i] = -1;
				proc->pageValid[page_index + i] = 0;
			}
		}
		n->nodeAlloc = -1;
		n->nodePid = -1;
		n->available = true;
		physicalMem.merge();

		//lru list에서 해당 frame lru찾아서 삭제
		for (list<int*>::iterator i = LRUlist.begin(); i != LRUlist.end(); i++) {
			if ((*i)[0] == processPid && (*i)[1] == allocID) {
				LRUlist.erase(i);
				break;
			}
		}
	}
	else {
		for (int i = 0; i < pageNum; i++) {
			proc->pages[page_index + i] = -1;
			proc->pageTable[page_index + i] = -1;
			proc->pageValid[page_index + i] = 0;
		}
		//valid하지않다면 그냥 page내에서만 해제해줌.
	}
	ofstream memorytxt;
	memorytxt.open("memory.txt", ios::app);
	memorytxt << cycleCount << "\t" << proc->pid << "\t" << allocID << "\t" << 2 << endl;
}
void LRU() {
	int leastPid = LRUlist.front()[0];
	int leastAlloc = LRUlist.front()[1];
	process* proc = NULL;
	for (list<process>::iterator pr = allProcess.begin(); pr != allProcess.end(); pr++) {
		if ((*pr).pid == leastPid) {
			proc = &(*pr);
			break;
		}
	}
	//page index를 받고
	int page_index = -1;
	int pageNum = 0;
	for (int i = 0; i < vmemSize; i++) {
		if (proc->pages[i] == leastAlloc) {
			page_index = i;
			pageNum += 1;
		}
	}
	page_index = page_index - pageNum + 1;
	//valid bit부터 1인지 확인
	if (proc->pageValid[page_index] == 1) {
		//valid하니까 그대로 valid bit만 바꿔주고, frame은 초기값으로 돌려준다.
		node * n = physicalMem.pidAlloc(proc->pid, leastAlloc);
		for (int i = 0; i < n->blockSize; i++) {
			n->framePid[i] = -1;
			n->frameAlloc[i] = -1;
			if (i < pageNum) {
				proc->pageValid[page_index + i] = 0;
			}
		}
		ofstream memorytxt;
		memorytxt.open("memory.txt", ios::app);
		memorytxt << cycleCount << "\t" << proc->pid << "\t" << leastAlloc << "\t" << 2 << endl;
		n->nodeAlloc = -1;
		n->nodePid = -1;
		n->available = true;
		physicalMem.merge();

		//lru list에서 해당 frame lru찾아서 삭제
		LRUlist.pop_front();
	}


}




