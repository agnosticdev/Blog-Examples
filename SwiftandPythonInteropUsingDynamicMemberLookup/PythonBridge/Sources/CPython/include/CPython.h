// Point to the Python.h header file on Linux or macOS.
#ifdef __linux__
#include "/usr/include/python2.7/Python.h"
#elif __APPLE__
#include "/usr/include/python2.7/Python.h"
#else
#error Was not able to detect the operating system properly.
#endif