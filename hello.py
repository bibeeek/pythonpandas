Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from collections import Counter
sentence = "the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"
print(dict(Counter(sentence)))
{'t': 18, 'h': 9, 'e': 8, ' ': 26, 'c': 3, 'a': 15, 's': 2, 'o': 2, 'n': 6, 'm': 3, 'w': 4, 'i': 4, 'r': 4, 'd': 2, 'p': 3, 'l': 1, 'y': 2, 'g': 1}
type(dict)
<class 'type'>
from datetime import datetime
import time
dir(datetime)
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
help(time.time)
Help on built-in function time in module time:

time(...)
    time() -> floating point number
    
    Return the current time in seconds since the Epoch.
    Fractions of a second may be present if the system clock provides them.

time
<module 'time' (built-in)>
today
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    today
NameError: name 'today' is not defined
print(time.ctime)
<built-in function ctime>
print(time.ctime())
Tue Dec  6 08:11:58 2022
print(date())
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(date())
NameError: name 'date' is not defined
print(datetime)
<class 'datetime.datetime'>
print(datetime.datetime)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(datetime.datetime)
AttributeError: type object 'datetime.datetime' has no attribute 'datetime'
print(time())
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(time())
TypeError: 'module' object is not callable
print(time)
<module 'time' (built-in)>
print(today)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(today)
NameError: name 'today' is not defined
today
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    today
NameError: name 'today' is not defined
datetime.datetime
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    datetime.datetime
AttributeError: type object 'datetime.datetime' has no attribute 'datetime'
print(datetime.today)
<built-in method today of type object at 0x00007FF870A888E0>
datetime.today
<built-in method today of type object at 0x00007FF870A888E0>
today=datetime.date.today()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    today=datetime.date.today()
AttributeError: 'method_descriptor' object has no attribute 'today'
print(today)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(today)
NameError: name 'today' is not defined
print(datetime.today())
2022-12-06 08:16:31.174361
print(datetime.today())
2022-12-06 08:16:57.467413
print(datetime.today())
2022-12-06 08:17:02.467256
print(today())
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(today())
NameError: name 'today' is not defined
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
import os
dir(os)
['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']
import sys
dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_getquickenedcount', '_git', '_home', '_stdlib_dir', '_vpath', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
>>> help(version)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    help(version)
NameError: name 'version' is not defined
>>> sys.version
'3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)]'
>>> sys.path
['', 'C:\\Program Files\\Python311\\Lib\\idlelib', 'C:\\Program Files\\Python311\\python311.zip', 'C:\\Program Files\\Python311\\Lib', 'C:\\Program Files\\Python311\\DLLs', 'C:\\Users\\HP\\AppData\\Roaming\\Python\\Python311\\site-packages', 'C:\\Users\\HP\\AppData\\Roaming\\Python\\Python311\\site-packages\\win32', 'C:\\Users\\HP\\AppData\\Roaming\\Python\\Python311\\site-packages\\win32\\lib', 'C:\\Users\\HP\\AppData\\Roaming\\Python\\Python311\\site-packages\\Pythonwin', 'C:\\Program Files\\Python311', 'C:\\Program Files\\Python311\\Lib\\site-packages']
>>> sys.version_info
sys.version_info(major=3, minor=11, micro=0, releaselevel='final', serial=0)
>>> sys.platform
'win32'
>>> sys.modules

