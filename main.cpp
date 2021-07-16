#include <C:\Users\gustx\AppData\Local\Programs\Python\Python36\include\Python.h>


static PyObject*
threader_object(PyObject *self,PyObject *args)
{
    const char *command;
    int sts;
    if(!PyArg_ParseTuple(args,"s",&command))
        return nullptr;
    sts = system(command);
    return PyLong_FromLong(sts);
}

int main(int argc,char* argv[])
{
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    PyRun_SimpleString("from time import time");

    Py_Finalize();
    return 0;
}