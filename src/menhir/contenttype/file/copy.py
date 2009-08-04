# -*- coding: utf-8 -*-

import grok
import shutil

from ZODB.blob import Blob
from zope.lifecycleevent import IObjectCopiedEvent
from menhir.contenttype.file import IFile


@grok.subscribe(IFile, IObjectCopiedEvent)
def copyFile(target, event):
    original = event.original
    target = event.object
    target.data._blob = Blob()

    fsrc = original.data._blob.open('r')
    fdst = target.data._blob.open('w')
    shutil.copyfileobj(fsrc, fdst)
    fdst.close()
    fsrc.close()
