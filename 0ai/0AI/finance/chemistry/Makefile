CC = g++

all: Exe 

Exe : main.o Hello.o

    $(CC) -o Exe main.o Hello.o

main.o: main.cpp
    $(CC) -c main.cpp

Hello.o: Hello.cpp
    $(CC) -c Hello.cpp

clean:
    rm -rf *o main.o Hello.o