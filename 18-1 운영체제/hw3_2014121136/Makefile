CXX     = g++
DEBUG   = -g
CXXFLAGS  = -Wall $(DEBUG) --std=c++11 -pthread
LDFLAGS = -lpthread

all: simulator

simulator: simulator.o
	g++ -std=c++0x simulator.cpp -o simulator

simulator.o : simulator.cpp
	g++ -std=c++0x simulator.cpp


clean:
	rm -f simulator simulator.o
