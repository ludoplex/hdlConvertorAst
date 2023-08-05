import sys

# [TODO] merge with py_ver_independent_str

if sys.version_info[0] <= 2:
    def is_str(x):
        return isinstance(x, (basestring, unicode))
else:
    def is_str(x):
        return isinstance(x, str)


def method_as_function(fn):
    return fn.im_func if sys.version_info[0] <= 2 else fn
