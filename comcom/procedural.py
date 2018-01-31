import ctypes
import os

from _low_level import ffi

lib = ffi.dlopen('comcom')
we = ffi.dlopen(None)

def init():
    if we.libcomcom_python_init() == -1:
        raise OSError(ctypes.get_errno())

def run_command(input, file, argv, env=os.environ, timeout=-1):
    output = ffi.new("char **")
    output_len = ffi.new("size_t *")
    argv2 = ffi.new("char **", [ffi.new("char[]", v) for v in argv+[None]])
    envp2 = ffi.new("char **", [ffi.new("char[]", "%s=%s" % p) for p in env.items()])
    if lib.libcomcom_run_command(input, len(input), output, output_len, file, argv2, envp2, timeout) == -1:
        raise OSError(ctypes.get_errno())
    return ffi.string(output[0], output_len[0])

def terminate():
    if lib.libcomcom_terminate() == -1:
        raise OSError(ctypes.get_errno())
