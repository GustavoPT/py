#include <iostream>
#include "Atom.h"
#include "Proton.h"
#include <ctime>
#include <cstdlib>
#include <map>
#include <vector>
using namespace std;

int main()
{
    std::map<std::string,int>m;
    vector<Atom> atoms;
    auto lambda = []() { cout << "Code within a lambda expression" << endl; };
    Atom* a1 = new Atom();
    Proton* p1 = new Proton();

    // you can have many orbitals 
    // each orbital will have its 
    // array of electrons 
    // array of protons 
    // array of atoms 
    // 
    srand(time(0));

    int r = (rand() % 10) + 1;

    cout << r << endl;

    return 0;
}