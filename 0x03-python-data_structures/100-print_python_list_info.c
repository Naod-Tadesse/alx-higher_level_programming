#include <Python.h>
/**
 * print_python_list_info - python list
 * @p: python object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int list_size;
	PyListObject *size_allocated;
	int i;
	PyObject *item;

	list_size = Py_SIZE(p);
	size_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", size_allocated);

	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name)
	}
}
