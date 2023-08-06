#include "mydist.h"
#include <Python.h>

static PyMethodDef module_methods[] = {
    {"mdist", (PyCFunction)mdist, METH_VARARGS | METH_KEYWORDS, "TODO"}};

PyMODINIT_FUNC PyInit_MAZAlib(void) {
  Py_Initialize();
  PyObject *module;
  static struct PyModuleDef moduledef = {PyModuleDef_HEAD_INIT,
                                         "MAZAlib",
                                         module_docstring,
                                         -1,
                                         module_methods,
                                         NULL,
                                         NULL,
                                         NULL,
                                         NULL};
  module = PyModule_Create(&moduledef);
  if (!module)
    return NULL;
  return module;
}

static double *mdist(PyObject *self, PyObject *args, PyObject *keywds) {

  double PyObject *input_data_py;

  static char *kwlist[] = {"x", "y", "shift"};
  double x{0.};
  double y{0.};
  double shift{0.};
  if (!PyArg_ParseTupleAndKeywords(args, keywds, "O(CCCi)(ii)", kwlist,
                                   &input_data_py, &x, &y)) {
    return NULL;
  }
  MyDist mdist(shift);

  return mdist.dist(x, y);
}