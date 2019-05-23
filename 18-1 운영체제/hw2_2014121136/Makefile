CXX     = g++
DEBUG   = -g
CXXFLAGS  = -Wall $(DEBUG) --std=c++11 -pthread
LDFLAGS = -lpthread

all: process noparellel thread 

process: process.o
	g++ process.cpp -o process

process.o : process.cpp
	g++ process.cpp

noparellel: noparellel.o
	g++ noparellel.cpp -o noparellel

noparellel.o : noparellel.cpp
	g++ noparellel.cpp

thread: thread.o 
	$(CXX) $(CXXFLAGS) thread.cpp -o thread
     
thread.o : thread.cpp
	g++ $(CXXFLAGS) thread.cpp 

clean:
	rm -f thread process noparellel thread.o process.o noparellel.o
