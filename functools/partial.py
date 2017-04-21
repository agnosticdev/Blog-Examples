#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

# Instead of importing from reprlib.py, I added this function in for clarity
def recursive_repr(fillvalue='...'):
    'Decorator to make a repr function return fillvalue for a recursive call'

    def decorating_function(user_function):
        repr_running = set()

        def wrapper(self):
            key = id(self), get_ident()
            if key in repr_running:
                return fillvalue
            repr_running.add(key)
            try:
                result = user_function(self)
            finally:
                repr_running.discard(key)
            return result

        # Can't use functools.wraps() here because of bootstrap issues
        wrapper.__module__ = getattr(user_function, '__module__')
        wrapper.__doc__ = getattr(user_function, '__doc__')
        wrapper.__name__ = getattr(user_function, '__name__')
        wrapper.__qualname__ = getattr(user_function, '__qualname__')
        wrapper.__annotations__ = getattr(user_function, '__annotations__', {})
        return wrapper

    return decorating_function

# Purely functional, no descriptor behaviour
class partial:

    __slots__ = "func", "args", "keywords", "__dict__", "__weakref__"

    # --- Python usage ---
    # __new__ creates a new instance of partial
    # __new__ is not the factory __init__ though, pay close attention to that
    # For a deep dive into partials use of __new__ checkout the C source 
    # behind this code in the _functoolsmodule.c module
    # 
    # --- C Soucre ---
    # static PyObject *
    # partial_new(PyTypeObject *type, PyObject *args, PyObject *kw)
    #
    # Also, checkout __new__ in typeobject.c
    #
    # static PyObject *
    # type_new(PyTypeObject *metatype, PyObject *args, PyObject *kwds) { ... }
    #
    def __new__(*args, **keywords):
        if not args:
            raise TypeError("descriptor '__new__' of partial needs an argument")
        if len(args) < 2:
            raise TypeError("type 'partial' takes at least one argument")
        cls, func, *args = args

        if not callable(func):
            raise TypeError("the first argument must be callable")
        args = tuple(args)

        # Assign instance variables by determining their avialability
        if hasattr(func, "func"):
            args = func.args + args
            # This is pretty awesome, the passed in func keywords are copied
            # The func keywords is then updated with the instance keywords
            # Keywords is then overwritten with the temporary keywords
            # The memory is then released for temporary keywords
            tmpkw = func.keywords.copy()
            tmpkw.update(keywords)
            keywords = tmpkw
            del tmpkw
            func = func.func
        # Following the PEP 8 standard to use cls instead of self
        self = super(partial, cls).__new__(cls)
        self.func = func
        self.args = args
        self.keywords = keywords
        return self
    
    # --- Python usage ---
    # __call__ gives the object returned from the partial the callable functionality
    # For example a = partial(func)
    # can now be called like this: a(f) because of __call__
    #
    # --- C Soucre ---
    # For a deep dive into partials use of __call__ checkout the C source 
    # behind this code in the _functoolsmodule.c module
    #
    # static PyObject *
    # partial_call(partialobject *pto, PyObject *args, PyObject *kwargs) { ... }
    #
    # Also, checkout __call__ checkout in typeobject.c
    #
    # static PyObject *
    # type_call(PyTypeObject *type, PyObject *args, PyObject *kwds) { ... }
    #
    def __call__(*args, **keywords):
        if not args:
            raise TypeError("descriptor '__call__' of partial needs an argument")
        self, *args = args
        newkeywords = self.keywords.copy()
        newkeywords.update(keywords)
        # Here is what makes the passed in func callable
        return self.func(*self.args, *args, **newkeywords)

    # --- Python usage ---
    # __repr__ is used to create an informal string representation of an instance.
    # Sometimes, a string cannot be created on a partial so <...> would be used.
    # 
    # One thing to note, is that this method uses f-string, which is a Python 3.6
    # feature only.  This allows formatted string literals
    #
    # Notice the @recursive_repr() decorator, this is represented above
    #
    # --- C Soucre ---
    # For a deep dive into partials use of __repr__ checkout the C source 
    # behind this code in the _functoolsmodule.c module
    # static PyObject *
    # partial_repr(partialobject *pto) { ... }
    #
    # Also, checkout __call__ checkout in typeobject.c
    #
    # static PyObject *
    # object_repr(PyObject *self) { ... }
    #
    # static PyObject *
    # type_repr(PyTypeObject *type) { ... }
    #
    @recursive_repr()
    def __repr__(self):
        # Build a string represenation of this instance
        qualname = type(self).__qualname__
        args = [repr(self.func)]
        args.extend(repr(x) for x in self.args)
        # This only works with python 3.6 and above because of f-strings
        args.extend(f"{k}={v!r}" for (k, v) in self.keywords.items())

        # If called to debug, a string representation of this instance will
        # be returned, very much like __str__ 
        if type(self).__module__ == "functools":
            return f"functools.{qualname}({', '.join(args)})"
        return f"{qualname}({', '.join(args)})"

    # --- Python usage ---
    # In case an instance needs to be pickled (serialized) and a specific
    # variable cannot be serialized down properly, __reduce__ will handle this
    # for us by dealing with this failure gracefully.
    #
    # --- C Soucre ---
    # For a deep dive into partials use of __reduce__ checkout the C source 
    # behind this code in the _functoolsmodule.c module
    #
    # static PyObject *
    # partial_reduce(partialobject *pto, PyObject *unused) {...}
    #
    def __reduce__(self):
        return type(self), (self.func,), (self.func, self.args,
               self.keywords or None, self.__dict__ or None)

    # --- Python usage ---
    # In case an instance needs to be pickled (serialized) __setstate__
    # can help setup the state of an object before it is pickled so
    # that the instance variables matche the state variables
    #
    # --- C Soucre ---
    # For a deep dive into partials use of __setstate__ checkout the C source 
    # behind this code in the _functoolsmodule.c module
    #
    # static PyObject *
    # partial_setstate(partialobject *pto, PyObject *state) { ... }
    #
    def __setstate__(self, state):
        if not isinstance(state, tuple):
            raise TypeError("argument to __setstate__ must be a tuple")
        # Check that the state variables match the instances variables
        if len(state) != 4:
            raise TypeError(f"expected 4 items in state, got {len(state)}")
        func, args, kwds, namespace = state
        if (not callable(func) or not isinstance(args, tuple) or
           (kwds is not None and not isinstance(kwds, dict)) or
           (namespace is not None and not isinstance(namespace, dict))):
            raise TypeError("invalid partial state")

        args = tuple(args) # just in case it's a subclass
        if kwds is None:
            kwds = {}
        elif type(kwds) is not dict: # XXX does it need to be *exactly* dict?
            kwds = dict(kwds)
        if namespace is None:
            namespace = {}

        self.__dict__ = namespace
        self.func = func
        self.args = args
        self.keywords = kwds

try:
    from _functools import partial
except ImportError:
    pass


class Employee():

    # Initialize a new instance of the employee
	def __init__(self):
		self.__employee_name = ""
		self.__employee_number = -1
    # Setter for employee name
	def set_employee_name(self, name):
		if len(name) > 0:
			self.__employee_name = name
			return True
		else:
			return False
    # Getter for employee name
	def get_employee_name(self):
		return self.__employee_name
    # Setter for employee number
	def set_employee_number(self, number):
		if self.validate_numeric(number):
			self.__employee_number = number
			return True
		else:
			return False
    # Getter for employee number
	def get_employee_number(self):
		return self.__employee_number
    # Utility validation method
	def validate_numeric(self, num):
		if len(num) == 0:
			return False
		try:
			x = int(num)
			if x < 1:
				return False
			return True
		except ValueError:
			return False


def main():
	employee = Employee()
	instructions = [
		"Please enter an employee name: ",
		"Please enter an employee number: "
	]

    # Usage of our partial class from Python core above!
	func_dict = {
		0: partial(employee.set_employee_name),
		1: partial(employee.set_employee_number)
	}
	index = 0
	# Process user input
	while index < len(instructions):
		# Value comes off standard output as a string
		input_value = input(instructions[index])
		flag = func_dict[index](input_value)
		if flag:
			index += 1
		else:
			print("Not a valid input, please try again.")

	print("Employee name: " + employee.get_employee_name())
	print("Employee number: " + employee.get_employee_number())

# Execute the main function
if __name__ == '__main__':
    main()
