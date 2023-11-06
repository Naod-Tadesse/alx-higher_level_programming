#include <Python.h>
/**
 * print_python_list_info - python list
 * @p: python object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
        PyObject *ob;
	long int list_size;
	PyListObject *size_allocated;
	int i;

	list_size = Py_SIZE(p);
	size_allocated = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", size_allocated->allocated);

	for (i = 0; i < list_size; i++)
	{
		ob = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(ob)->tp_name);
	}
}
