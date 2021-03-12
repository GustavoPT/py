#include "mainwindow.h"
#include <QApplication>
#include <QProcess>
#include <thread>
#include <iostream>
#include<QDebug>
#include <QFile>
#include <QMessageBox>

// create a quicksort function

// do it with multithreading

// get the input from the user here

// and all the stuff read from a mysql database

// create a timer to anaylize how long it takes to do so

void foo(int z)
{

    // code to read from a text file
    QFile file("test.txt");
    if(!file.open(QIODevice::WriteOnly)){
        QMessageBox::information(0,"error",file.errorString());

    }
    QTextStream in(&file);

    while(!in.atEnd()){
        QString line = in.readLine();
        qInfo() << line;
        QStringList fields = line.split(",");

    }
    file.close();
}

void bar(int x)
{

}

//class fn_object_class{
//    void operator()(params){

//    }
//};


int main(int argc, char *argv[])
{
//    auto f = [](params){

//    };

//    std::thread first(foo,3);
//    std::thread second(bar,0);

//    first.join();
//    second.join();

    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();
}

