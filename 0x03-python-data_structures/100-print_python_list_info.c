#include "lists.h"
#include <Python.h>

/**
 * print_python_list_info - print info
 * @p: ptr *p
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *opj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n",alloc);

	for (i = 0, i < size, i++)
	{
		printf("Element %d: ", i);

		opj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(opj)->tp_name);
	}
}