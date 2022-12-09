Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="argentina will win the world cup"
dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
x.count(" ")
5
help(x.split)
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

x.split()
['argentina', 'will', 'win', 'the', 'world', 'cup']
x.split(' ')
['argentina', 'will', 'win', 'the', 'world', 'cup']
#x
#Use () on built in functions...
#no of words in the sentence is always [space count + 1]
x.put()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x.put()
AttributeError: 'str' object has no attribute 'put'
name.sput()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name.sput()
NameError: name 'name' is not defined
x.sput()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x.sput()
AttributeError: 'str' object has no attribute 'sput'. Did you mean: 'split'?
##############################################################################################################
y="hello/nthis/nis/n"
y
'hello/nthis/nis/n'
df
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    df
NameError: name 'df' is not defined
y="name\nis\nelon"
y
'name\nis\nelon'
tsdc
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tsdc
NameError: name 'tsdc' is not defined
sd
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sd
NameError: name 'sd' is not defined. Did you mean: 'id'?
y="name\n is\n p"
y
'name\n is\n p'
print(y)
name
 is
 p
y="this/n is /n elon/n musk/n "
print(y)
this/n is /n elon/n musk/n 
y="this\n is \n elon\n musk\n"
print(y)
this
 is 
 elon
 musk

y=" this\n is \n elon\n musk\n"
print(y)
 this
 is 
 elon
 musk

y="\tthis \tis \tis \telon \tmusk"
print(y)
	this 	is 	is 	elon 	musk
y="\tthis \tis \telon \tmusk"
print(y)
	this 	is 	elon 	musk
y.count(" ")
3
y.count("\t")
4
x
'argentina will win the world cup'
y
'\tthis \tis \telon \tmusk'
print
<built-in function print>

##\n is used as enter, \t as tab

y="\sthis\sis\sis\selon\smusk"
print(y)
\sthis\sis\sis\selon\smusk
y
'\\sthis\\sis\\sis\\selon\\smusk'
y='hello\sncit"
SyntaxError: incomplete input
y='hello\sncit'
print(y)
hello\sncit
y
'hello\\sncit'
######################################################### \s used as space
letters="sduhisduf hodfhdsufh hedifuvhdi fdiuvd diufvhd idfuvh duif vh difu vhfiu h u iu hi uh iudfiu hdif idfu hdifu  iu h duh  iu h iuh dfiu hci u iuh dfiu hicuvh icdfd hiu h iudhf iuhiu dfu h iduf hiu"
print(letters)
sduhisduf hodfhdsufh hedifuvhdi fdiuvd diufvhd idfuvh duif vh difu vhfiu h u iu hi uh iudfiu hdif idfu hdifu  iu h duh  iu h iuh dfiu hci u iuh dfiu hicuvh icdfd hiu h iudhf iuhiu dfu h iduf hiu
letters="""sduhisduf hodfhdsufh hedifuvhdi fdiuvd diufvhd idfuvh duif vh difu vhfiu h u iu hi uh iudfiu hdif idfu hdifu  iu h duh  iu h iuh dfiu hci u iuh dfiu hicuvh icdfd hiu h iudhf iuhiu dfu h iduf hiu"""
print(letters)
sduhisduf hodfhdsufh hedifuvhdi fdiuvd diufvhd idfuvh duif vh difu vhfiu h u iu hi uh iudfiu hdif idfu hdifu  iu h duh  iu h iuh dfiu hci u iuh dfiu hicuvh icdfd hiu h iudhf iuhiu dfu h iduf hiu
name="""erfger erv erv er ervv fv refbe erfe erf er fe rfe rf erf er ferferf er f erf er f erf er fe rf erf er fer j j k k  k k k k k k  hj h jh jh jh jh jh jh jh k j kjk jkj k jk jjk  jk"""
name
'erfger erv erv er ervv fv refbe erfe erf er fe rfe rf erf er ferferf er f erf er f erf er fe rf erf er fer j j k k  k k k k k k  hj h jh jh jh jh jh jh jh k j kjk jkj k jk jjk  jk'
print(name)
erfger erv erv er ervv fv refbe erfe erf er fe rfe rf erf er ferferf er f erf er f erf er fe rf erf er fer j j k k  k k k k k k  hj h jh jh jh jh jh jh jh k j kjk jkj k jk jjk  jk
"""erfger erv erv er ervv fv refbe erfe erf er fe rfe rf erf er ferferf er f erf er f erf er fe rf erf er fer j j k k  k k k k k k  hj h jh jh jh jh jh jh jh k j kjk jkj k jk jjk  jk"""
'erfger erv erv er ervv fv refbe erfe erf er fe rfe rf erf er ferferf er f erf er f erf er fe rf erf er fer j j k k  k k k k k k  hj h jh jh jh jh jh jh jh k j kjk jkj k jk jjk  jk'
erfger erv erv er ervv fv refbe erfe erf er fe rfe rf erf er ferferf er f erf er f erf er fe rf erf er fer j j k k  k k k k k k  hj h jh jh jh jh jh jh jh k j kjk jkj k jk jjk  jk"""erfger erv erv er ervv fv refbe erfe erf er fe rfe rf erf er ferferf er f erf er f erf er fe rf erf er fer j j k k  k k k k k k  hj h jh jh jh jh jh jh jh k j kjk jkj k jk jjk  jk"""
SyntaxError: invalid syntax


"""erfger erv erv er ervv fv refbe erfe erf er fe rfe rf erf er ferferf er f erf er f erf er fe rf erf er fer j j k k  k k k k k k  hj h jh jh jh jh jh jh jh k j kjk jkj k jk jjk  jk"""
'erfger erv erv er ervv fv refbe erfe erf er fe rfe rf erf er ferferf er f erf er f erf er fe rf erf er fer j j k k  k k k k k k  hj h jh jh jh jh jh jh jh k j kjk jkj k jk jjk  jk'
""ferf ere""
SyntaxError: invalid syntax




age=20
if age<=20
SyntaxError: incomplete input
age=20
if age<18:
    print("true")
    else
    
SyntaxError: incomplete input
age=20
if age<30:
    print("true")
    else:
        
SyntaxError: invalid syntax
if age<30:
    print("true")
    else age>30:
        
SyntaxError: invalid syntax
if age<30:
    print("true")

    
true
age=31
if age<30:
    print("true")

    
if age<35:
    print("true")

    
true
age=21
if age<30:
    print("true value")

    
true value

if age<30:
    print("true")
    elif age>30 and age>=30:
        
SyntaxError: invalid syntax
if age<30:
    print("yes")

    
yes
else:
    
SyntaxError: invalid syntax
if age<30:
    print("true")
elif age>30 and age>=30:
    print("false")

    
true
age
21
age=35
if age<30:
    print("true")
elif age>30 and age>=30:
    print("false")
else:
    print("given value is wrong")

    
false
if age<30:
    print("true")
elif age>30 and age>=30:
    print("false")
else:
    print("given value is wrong")

    
false
age="B"
if age<30:
    print("true")
elif age>30 and age>=30:
    print("false")
else:
    print("given value is wrong")
    
SyntaxError: multiple statements found while compiling a single statement
age=a
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    age=a
NameError: name 'a' is not defined
age=88878787
age="B"
if age<30:
    print("true")
elif age>30 and age>=30:
    print("false")
else:
    print("given value is wrong")
    
SyntaxError: multiple statements found while compiling a single statement
a=5
if a==10:
    print("yes")
else:
    print("no")

    
no
a==10
False
a=10
a==10
True
a=9
a==10
False
age = 26
if age <= 20:
print("Age is < or = 20")
elif age>20 and age<=30:
print("Age is > 20 and <= 30")
else:
if age > 30:
print("Age is > 30")
else:
print("My Condition above didn't Matches")
SyntaxError: multiple statements found while compiling a single statement


a==10
False
a==26
False
a
9
a==9
True
age=35
a==10||a<=4
SyntaxError: invalid syntax
a==100|a<=4
False
##| used as or
a==10|a>=10
False

a=10
a==10|a>=10
True
a==10 & a<=10
True
a=122a==10 & a<=10
SyntaxError: invalid decimal literal
a=122a==10 & a<=10
SyntaxError: invalid decimal literal
a=122 a==10 & a<=10
SyntaxError: invalid syntax
a=122
a==10&a>==10
SyntaxError: invalid syntax
a==10&a>=10
False
a=9
a==10 and a<=10
False
a==10 or a<=10
True
age=99
if age==50 or a<=50
SyntaxError: incomplete input
if age==50 or a<=50:
    print("true value")
 elif age==100 or a>=100:
     
SyntaxError: unindent does not match any outer indentation level
if age==50 or a<=50:
    print("true value")elif age==100 or a>=100:
        
SyntaxError: invalid syntax
if age==50 or a<=50:
    print("true value")
elif age==100 or a>=100:
    print("false value")
else:
    print("undefined value")

    
true value
a
9
if a==50 or a<=50:
    print("true value")
elif a==100 or a>=100:
    print("false value")
else:
    print("undefined value")

    
true value
a=99
if a==50 or a<=50:
    print("true value")
elif a==100 or a>=100:
    print("false value")
else:
    print("undefined value")

    
undefined value
if a==50 or a<=50:
    print("true value")
elif a==100 or a>=100:
    print("false value")
else:
    if age>50 and  age<100:
        print("undefined value")

        
undefined value
if a==50 or a<=50:
    print("true value")
elif a==100 or a>=100:
    print("false value")
else:
    if age>50 and  age<100:
        print("undefined vvalue")

        
undefined vvalue
age=50
if a==50 or a<=50:
    print("true value")
elif a==100 or a>=100:
    print("false value")
else:
    if age>50 and  age<100:
        print("undefined vvalue")

        

a=50
if a==50 or a<=50:
    print("true value")
elif a==100 or a>=100:
    print("false value")
else:
    if age>50 and  age<100:
        print("undefined vvalue")

        
true value

for i=1-10:
    
SyntaxError: invalid syntax
number=0
name="pyhton"
"t" in name
True
for t in name"
SyntaxError: incomplete input
for t in name:
    print

    
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
for x in name:
    print(x)

    
p
y
h
t
o
n
for z in name:
    print(z)

    
p
y
h
t
o
n
for i in range(4)
SyntaxError: incomplete input
for i in range(4):
    print(i)

    
0
1
2
3
for i in range(101):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
for i in range(1-101)
SyntaxError: incomplete input
for i in range(1,11):
    if i>5:
        print((+"5")
    if (i==6):
              
SyntaxError: incomplete input
for i in range(1,100)
              
SyntaxError: incomplete input
for i in range(1,100):
              if i>25:
              print((+"25")
                    
SyntaxError: expected an indented block after 'if' statement on line 2
for i in range(1,100):
              if i>25:
              print(+"25")
                    
SyntaxError: expected an indented block after 'if' statement on line 2
for i in range(1,100):
              if i>25:
              print((+"25")
                    
SyntaxError: expected an indented block after 'if' statement on line 2
i
                    
100
for u in range(1,100)
                    
SyntaxError: incomplete input
for str(u) in range(1,100):
                    
SyntaxError: cannot assign to function call
for r in range(1,100):
                    if str(r)>25:
                    print((+"25")
                          
SyntaxError: expected an indented block after 'if' statement on line 2
for r in range(1,100):
                    if str(r)>25:
                    print(i+"25")
                          
SyntaxError: expected an indented block after 'if' statement on line 2
for r in range(1,100):
                    if str(r)>25:
                    print(i+25)
                          
SyntaxError: expected an indented block after 'if' statement on line 2
i
                          
100

for i in range(1,100):
    if i<25:
        print(str(i)+"25")
    if (i==50):
        print("fifty")
    if (i>=80):
        if(i<=90):
            print(i)

                          
125
225
325
425
525
625
725
825
925
1025
1125
1225
1325
1425
1525
1625
1725
1825
1925
2025
2125
2225
2325
2425
fifty
80
81
82
83
84
85
86
87
88
89
90
for i in range(1,100):
    if i<25:
        print(str(i)+"--25")
    if (i==50):
        print("fifty")
    if (i>=80):
        if(i<=90):
            print(i)

                          
1--25
2--25
3--25
4--25
5--25
6--25
7--25
8--25
9--25
10--25
11--25
12--25
13--25
14--25
15--25
16--25
17--25
18--25
19--25
20--25
21--25
22--25
23--25
24--25
fifty
80
81
82
83
84
85
86
87
88
89
90
>>> for i in range(10):
...                           if(i%2==0):
...                           print("*")
...                           
SyntaxError: expected an indented block after 'if' statement on line 2
>>> for i in range(10):
