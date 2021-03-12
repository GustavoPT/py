#include <C:\Users\gustx\AppData\Local\Programs\Python\Python36\include\Python.h>

static PyObject*
second_module(PyObject *self,PyObject *args)
{
    const char *command;
    int sts;
    if(!PyArg_ParseTuple(args,"s",&command))
        return nullptr;
    sts = system(command);
    return PyLong_FromLong(sts);
}

int main(int argc,char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0],NULL);

    return 0;
}