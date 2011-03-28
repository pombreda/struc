# Created @ 2011-01-20

import ctypes


unbound_fields = []


class StrucMeta(type):

    @staticmethod
    def __new__(cls, name, bases, attrs):
        rv = super(StrucMeta    , cls).__new__(cls, name, bases, attrs)

        if not unbound_fields:
            return rv

        class core(ctypes.Structure):
            _fields_ = unbound_fields[:]
            del unbound_fields[:]
        core.__name__ = name
        
        rv.core = core            
        return rv
        
    def __getattr__(self, name):
        unbound_fields.append((name, self.core))
        return self
        
    def __getitem__(self, index):
        name, core = unbound_fields.pop()
        unbound_fields.append((name, core * index))
        return self
        
            
class Struc(object):

    __metaclass__ = StrucMeta

    @staticmethod
    def __new__(cls, *args, **kw):
        return cls.core.__new__(cls.core, *args, **kw)

if __name__ == '__main__':
    import doctest
    


