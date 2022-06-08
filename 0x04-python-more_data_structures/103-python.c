#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print some basic info about Python bytes objects.
 * @p: pointer to a PyObject
 *
 * Return: void, nth
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0;
	char *str = NULL;
	int i = 0;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &str, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", str);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
		while (i < size + 1 && i < 10)
		{
			printf(" %02hhx", str[i]);
			i++;
		}
		printf("\n");
	}
}

/**
 * print_python_list - print some basic info about Python lists
 * @p: a pointer to a PyObject
 *
 * Return: void, nth
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *element;
	int i = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (i < size)
		{
			element = PyList_Get_ITEM(p, i);
			printf("Element %d: %s\n", i, element->ob_type->tp_name);
			if (PyBytes_Check(element))
				print_python_bytes(element);
			i++;
		}
	}
}
