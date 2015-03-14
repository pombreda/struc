# Introduction #

_struc_ is a syntax wrapper for _ctypes.Structure_

```
class User(Struc):
    BYTE.name[32]
    BYTE.password[32]
```
v.s.
```
class User(Structure):
    _fields_ = [
        ('name', c_ubyte * 32),
        ('password', c_ubyte * 32),
    ]
```

# Installation #
```
easy_install struc
```

# Download #

Visit http://pypi.python.org/pypi/struc/0.2

or

Download [struc-0.2.zip](http://pypi.python.org/packages/source/s/struc/struc-0.2.zip#md5=21b3a066c066ffb3ba5838a5fac5c46a) directly

or checkout the repo for the latest version