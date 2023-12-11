#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_bytes - prints information about python lists
 * @p: address of pyobject struct
 */
void print_python_bytes(PyObject *p)
{
	size_t n, len, size;
	char *str;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	len =  size + 1 > 10 ? 10 : size + 1;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes: ", len);
	for (n = 0; n < len; n++)
		printf("%02hhx%s", str[n], n + 1 < len ? " " : "");
	printf("\n");
}

/**
 * print_python_list - prints information about a python list
 * @p: address of pyobject struct
 */
void print_python_list(PyObject *p)
{
	int n;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (n = 0; n < ((PyVarObject *)p)->ob_size; n++)
	{
		printf("Element %d: %s\n", n,
				((PyListObject *)p)->ob_item[n]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[n]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[n]);


	}
}
