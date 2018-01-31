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

int libcomcom_destroy(void);
int libcomcom_terminate(void);
""")
ffibuilder.set_source("_low_level",
r"""
#include <signal.h>
#include <libcomcom.h>

PyOS_sighandler_t old_sigterm, old_sigint; 

static void sigterm_handler(int sig)
{
    libcomcom_terminate();
    if(old_sigterm != SIG_IGN && old_sigterm != SIG_DFL) old_sigterm(sig);
}

static void sigint_handler(int sig)
{
    libcomcom_terminate();
    if(old_sigint != SIG_IGN && old_sigint != SIG_DFL) old_sigint(sig);
}

/* TODO: Remove SIGTERM&SIGINT handlers on de-initialization */
static int libcomcom_python_init(void)
{
    struct sigaction act_term;
    old_sigterm = PyOS_getsig(SIGTERM);
    act_term.sa_handler = sigterm_handler;
    act_term.sa_flags = 0;
    sigemptyset(&act_term.sa_mask);
    if(sigaction(SIGTERM, &act_term, NULL))
        return -1;
    
    struct sigaction act_int;
    old_sigint = PyOS_getsig(SIGINT);
    act_int.sa_handler = sigint_handler;
    act_int.sa_flags = 0;
    sigemptyset(&act_int.sa_mask);
    if(sigaction(SIGTERM, &act_term, NULL))
        return -1;
    
    struct sigaction act;
    act.sa_handler = PyOS_getsig(SIGCHLD);
    act.sa_flags = 0;
    sigemptyset(&act.sa_mask);
    
    return libcomcom_init2(&act);  
}
""", libraries=['comcom'])


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
