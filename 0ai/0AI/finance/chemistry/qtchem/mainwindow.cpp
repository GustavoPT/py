#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QApplication>
#include <QProcess>
#include <QTextStream>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    QTextStream out(stdout);
    QProcess p;
    p.start("py -3 test.py");
    p.waitForFinished(-1);
    QString p_stdout = p.readAllStandardOutput();
    out <<  p_stdout <<  endl;
    out << "we're here" << endl;
    ui->lineEdit->setText(p_stdout);
}
