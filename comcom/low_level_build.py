# python = CDLL(None)

from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef(r"""
int libcomcom_python_init(void);

int libcomcom_run_command(const char *input, size_t input_len,
                          const char **output, size_t *output_len,
                          const char *file, char *const argv[],
                          char *const envp[],
                          int timeout);

int libcomcom_terminate(void);
""")

ffibuilder.set_source("_low_level",
r"""
#include <signal.h>
#include <libcomcom.h>

static int libcomcom_python_init(void)
{
    struct sigaction act;
    act.sa_handler = PyOS_getsig(SIGCHLD);
    act.sa_flags = 0;
    sigemptyset(&act.sa_mask);
    
    return libcomcom_init2(&act);  
}
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
