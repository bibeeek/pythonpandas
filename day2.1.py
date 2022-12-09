Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

10//2
5
10/2
5.0
print(15//3)
5
print(15/3)
5.0
print(7/3)
2.3333333333333335
7//3
2
99//5
19
99%5
4
13//7
1
13/7
1.8571428571428572
9//5
1
9//2
4
9/2
4.5
7**2
49
6**2
36
9**2
81
9**9
387420489
25*2
50











25**2
625
15
15
15*2
30
15**2
225
x="a"
x**2
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
9+9+9+9
36
9+9+9+9+9+9+9+9+9+9+9+9
108

+9+9+9+9+9+9+9+9+9
81

5+5+5+5+5+5+5
35
x=0545405
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
x=56560
len(str(x))
5
name="python programming"
print(name)
python programming
lne(name(p))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    lne(name(p))
NameError: name 'lne' is not defined
type
<class 'type'>
type(name)
<class 'str'>
x="FG",23
type(x)
<class 'tuple'>
word
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    word
NameError: name 'word' is not defined. Did you mean: 'ord'?
ord(name)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    ord(name)
TypeError: ord() expected a character, but string of length 18 found
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
name.count
<built-in method count of str object at 0x000001D81E0FF230>
name.p
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    name.p
AttributeError: 'str' object has no attribute 'p'
name.count()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name.count()
TypeError: count() takes at least 1 argument (0 given)
name.count(p)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    name.count(p)
NameError: name 'p' is not defined
name
'python programming'
name.count('o)
           
SyntaxError: incomplete input
name.count("p")
           
2
print(name.count("P"),len(name))
           
0 18
print(name.count("p"),len(name))
           
2 18
a="no"
           
a
           
'no'
b="yes"
           
name.count(" ")
           
1
name.count("m")
           
2
name.count("m","p")
           
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    name.count("m","p")
TypeError: slice indices must be integers or None or have an __index__ method
name.count("l")
           
0
name="Python Programming"
           
name.count("P")
           
2
name.count(len("P"))
           
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    name.count(len("P"))
TypeError: must be str, not int
name.count("Pro")
           
1
name.count(len(P))
           
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    name.count(len(P))
NameError: name 'P' is not defined
name.count(len("P"))
           
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    name.count(len("P"))
TypeError: must be str, not int

name="hell lleh"
           
name.count("hell")
           
1
name.count("ll")
           
2
dir(name)
           
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(name.upper)
           
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

help(name.count)
           
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

upper(name)
           
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    upper(name)
NameError: name 'upper' is not defined. Did you mean: 'super'?
name.upper
           
<built-in method upper of str object at 0x000001D81E143BF0>
name.upper()
           
'HELL LLEH'
name.lower()
           
'hell lleh'
name="python"
           
help(name.title)
           
Help on built-in function title:

title() method of builtins.str instance
    Return a version of the string where each word is titlecased.
    
    More specifically, words start with uppercased characters and all remaining
    cased characters have lower case.

name.title()
           
'Python'
help(name.add)
           
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    help(name.add)
AttributeError: 'str' object has no attribute 'add'
help(name.split)
           
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.
    
      sep
        The separator used to split the string.
    
        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.
    
    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.

name.split(sep=2,maxsplit=3)
           
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    name.split(sep=2,maxsplit=3)
TypeError: must be str or None, not int
name.split(2,3)
           
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    name.split(2,3)
TypeError: must be str or None, not int
name.split()
           
['python']
age=18
           
dir(age)
           
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
type(age)
           
<class 'int'>
help(age.real)
           
Help on int object:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Built-in subclasses:
 |      bool
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original int
 |      and with a positive denominator.
 |      
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |  
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |      
 |      Also known as the population count.
 |      
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |  
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |      
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  to_bytes(self, /, length, byteorder, *, signed=False)
 |      Return an array of bytes representing an integer.
 |      
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

help(real.age)
           
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    help(real.age)
NameError: name 'real' is not defined

help(age.to_bytes)
Help on built-in function to_bytes:

to_bytes(length, byteorder, *, signed=False) method of builtins.int instance
    Return an array of bytes representing an integer.
    
    length
      Length of bytes object to use.  An OverflowError is raised if the
      integer is not representable with the given number of bytes.
    byteorder
      The byte order used to represent the integer.  If byteorder is 'big',
      the most significant byte is at the beginning of the byte array.  If
      byteorder is 'little', the most significant byte is at the end of the
      byte array.  To request the native byte order of the host system, use
      `sys.byteorder' as the byte order value.
    signed
      Determines whether two's complement is used to represent the integer.
      If signed is False and a negative integer is given, an OverflowError
      is raised.

age.to_bytes()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    age.to_bytes()
TypeError: to_bytes() missing required argument 'length' (pos 1)
age.to_bytes(2,1,*,1)
SyntaxError: iterable argument unpacking follows keyword argument unpacking
dir.age
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    dir.age
AttributeError: 'builtin_function_or_method' object has no attribute 'age'
dir(age)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
help(age.bit_count)
Help on built-in function bit_count:

bit_count() method of builtins.int instance
    Number of ones in the binary representation of the absolute value of self.
    
    Also known as the population count.
    
    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3

name="python programming"
len(name)
18
len(pythonprogramming)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    len(pythonprogramming)
NameError: name 'pythonprogramming' is not defined
len("pythonprogramming")
17
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help.rfind
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    help.rfind
AttributeError: '_Helper' object has no attribute 'rfind'
help(name.rfind)
Help on built-in function rfind:

rfind(...) method of builtins.str instance
    S.rfind(sub[, start[, end]]) -> int
    
    Return the highest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

name[0]
'p'
[name[14]
 name[14]
 
SyntaxError: '[' was never closed
name[14]
 
'm'
name
 
'python programming'
len(name)
 
18
name[-1]
 
'g'
name[-18]
 
'p'
name[5]
 
'n'
name[17]
 
'g'
name[--0]
 
'p'
name[4]
 
'o'
name[-3]
 
'i'
name[0,1,2]
 
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    name[0,1,2]
TypeError: string indices must be integers
name[0:2]
 
'py'
name[0:-2]
 
'python programmi'
name[0:-1]
 
'python programmin'
name[0:0]
 
''
name[9:14]
 
'ogram'
name[10:14]
 
'gram'
name[8:13]
 
'rogra'
name[8:12]
 
'rogr'
name[-9:-5]
 
'ogra'
name[-10:-4]
 
'rogram'
name[-10:-6]
 
'rogr'
name[9]
 
'o'
name
 
'python programming'
name[-1:0]
 
''
name[-1:-5]
 
''
name[0:]
 
'python programming'
name[5:]
 
'n programming'
name[1:}
 
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
name[1:]
 
'ython programming'
name[-18:]
 
'python programming'
name[-1:]
 
'g'
name[17]
 
'g'
name[:-1]
 
'python programmin'
name[:2]
 
'py'
name[:-19]
 
''
name[0:2:10]
 
'p'
name[0:3:9]
 
'p'
name[4:7:9]
 
'o'
name
 
'python programming'
name[2:3:4]
 
't'
name[0::2]
 
'pto rgamn'
name[5::7]
 
'na'
name
 
'python programming'
name[1::2]
 
'yhnpormig'
name[5::18]
 
'n'
name[17]
 
'g'
name[5::17]
 
'n'
name[3::4]
 
'hpri'
name="cat"
 
name[1::2]
 
'a'
name="python programming"
 
name[3::4]
 
'hpri'
hpri
 
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    hpri
NameError: name 'hpri' is not defined
name[0::5]
 
'pngi'
pngi
 
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    pngi
NameError: name 'pngi' is not defined
name[5:17]
 
'n programmin'
name[1::2]
 
'yhnpormig'
name[0:10:2]
 
'pto r'
pto r
 
SyntaxError: incomplete input
name[0::]
 
'python programming'
name[0:]
 
'python programming'
name[0:5:2]
 
'pto'
name[0::1]
 
'python programming'
name
 
'python programming'
name[-18:-12:2]
 
'pto'
name{-12]
 
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
name[-12]
 
' '
name[-13]
 
'n'
name[-18:-13:-1]
 
''
name[-18:-13]
 
'pytho'
name[-18:-13:2]
 
'pto'
name[-18:-13:-2]
 
''
name[-18:-5:3]
 
'ph oa'
name[-1::1]
 
'g'
name[-1:-18:-1]
 
'gnimmargorp nohty'
name[-1::-1]
 
'gnimmargorp nohtyp'
name[::-1]
 
'gnimmargorp nohtyp'
name[0::]
 
'python programming'
name[0::1]
 
'python programming'
name[::0]
 
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    name[::0]
ValueError: slice step cannot be zero
name[::1]
 
'python programming'
name[::-2]
 
'gimropnhy'
name[::]
 
'python programming'
dir(name)
 
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
name[::1]
 
'python programming'
name[0::1]
 
'python programming'
yes="true"
 
type(yes)
 
<class 'str'>
yes=true
 
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    yes=true
NameError: name 'true' is not defined. Did you mean: 'True'?
yes=True
 
type(yes)
 
<class 'bool'>
yes
 
True
no=False
 
type(no)
 
<class 'bool'>
print(yes)
 
True
no
 
False
true=h
 
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    true=h
NameError: name 'h' is not defined
True=t
 
SyntaxError: cannot assign to True
True=9
 
SyntaxError: cannot assign to True
x=True
 
x
 
True
yes=True
 
is
 
SyntaxError: incomplete input
is=
 
SyntaxError: invalid syntax
P in name
 
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    P in name
NameError: name 'P' is not defined
"P" in name
 
False
"p" in name
 
True
"x" is in name
 
SyntaxError: invalid syntax
"python" in name
 
True
" " in name
 
True
"x" not in name
 
True
"z" not in name
 
True
"z" in name
 
False
"hello" in name
 
False
"pton" in name
 
False
"p,y" in name
 
False
"p" not in name
 
False
"p" in name
 
True
"go" in name
 
False
"go" not in name
 
True
"p" is name
 
False
"python programming" is name
 
False
"python" is name
 
False
"p" is name
 
False
"p" is not name
 
True
"python programming" is not name
 
True
name="cat"
 
"c" is name
 
False
"cat" is name
 
True
"cat" is not name
 
False
name="python programming"
 
"pythonprogramming" is name
 
False
name is "python programming"
 
False
name
 
'python programming'
name is 'python programming'
 
False
name="dog:
 
SyntaxError: incomplete input
name="python"
 
"python' is name
 
SyntaxError: incomplete input
>>> "python" is name
...  
True
>>> name
...  
'python'
>>> name="dog and cat"
...  
>>> "dog and cat" is name
...  
False
>>> x="dog"
...  
>>> y="cat"
...  
>>> x is y
...  
False
>>> y="dog"
...  
>>> x is y
...  
True
>>> name is not x
...  
True
>>> name="python programming"
...  
>>> name1="python programming"
...  
>>> name is name1
...  
False
>>> name="python"
...  
>>> name1="python"
...  
>>> name is name1
...  
True
