#include <Python.h>

void print_python_list(PyObject *p)
{
        Py_ssize_t size, i;
        PyObject *item;

        if (!PyList_Check(p))
        {
                fprintf(stderr, "Invalid List Object\n");
                return;
        }

        size = PyList_Size(p);
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        for (i = 0; i < size; i++)
        {
                item = PyList_GetItem(p, i);
                printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
}

void print_python_bytes(PyObject *p)
{
        Py_ssize_t size, i;
        char *data;

        if (!PyBytes_Check(p))
        {
                fprintf(stderr, "Invalid Bytes Object\n");
                return;
        }

        size = PyBytes_Size(p);
        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", PyBytes_AsString(p));

        printf("  first 10 bytes: ");
        data = PyBytes_AsString(p);
        if (size < 10)
                printf("%s\n", data);
        else
        {
                for (i = 0; i < 10; i++)
                printf("%02x ", data[i] & 0xFF);
                printf("\n");
        }
}

