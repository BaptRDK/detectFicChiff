#!/usr/bin/env python
import magic
import sys

def isFicBrok(filename):

    ms = magic.open(magic.MAGIC_NONE)
    ms.load()

    ftype = ms.file(filename.decode('utf8'))

    ms.close()
    if ftype[:6] == "broken":
        return(True)
    else:
        return(False)
