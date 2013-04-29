
from . import _urlparse as urlparse

import six
from functools import partial

def iterkeys(d, *a, **kw):
    return iter(getattr(d, six._iterkeys)(*a, **kw))

def itervalues(d, *a, **kw):
    return iter(getattr(d, six._itervalues)(*a, **kw))

def iteritems(d, *a, **kw):
    return iter(getattr(d, six._iteritems)(*a, **kw))

if six.PY3:
    _iterlists = 'lists'
    _iterlistvalues = 'listvalues'
else:
    _iterlists = 'iterlists'
    _iterlistvalues = 'iterlistvalues'

def iterlists(d, *a, **kw):
    return getattr(d, _iterlists)(*a, **kw)

def iterlistvalues(d, *a, **kw):
    return getattr(d, _iterlistvalues)(*a, **kw)

if six.PY3:
    def to_unicode(o, encoding='utf-8', errors='strict'):
        if isinstance(o, bytes):
            return o.decode(encoding, errors)
        return str(o)

    def to_bytes(o, encoding='utf-8', errors='strict'):
        if isinstance(o, bytes):
            return o
        return str(o).encode(encoding, errors)
else:
    def to_unicode(o, encoding='utf-8', errors='strict'):
        if isinstance(o, unicode):
            return o
        return str(o).decode(encoding, errors)

    def to_bytes(o, encoding='utf-8', errors='strict'):
        if isinstance(o, unicode):
            return o.decode(encoding, errors)
        return str(o)
