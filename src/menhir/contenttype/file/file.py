# -*- coding: utf-8 -*-

import dolmen.content as content
from dolmen.file import FileField
from dolmen.blob import BlobProperty
from dolmen.app.security import content as security
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('dolmen')


class IFile(content.IBaseContent):
    """A simple file object.
    """
    data = FileField(
        title = _(u"File"),
        required = True
        )


class File(content.Content):
    """A file content type storing the data in blobs.
    """
    content.name(_(u"File"))
    content.schema(IFile)
    content.icon("file.png")
    content.require(security.CanAddContent)

    data = BlobProperty(IFile['data'])
