##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Life cycle events
"""
__docformat__ = 'restructuredtext'

from zope.interface.interfaces import ObjectEvent
from zope.interface import implementer, moduleProvides
from zope.event import notify

from zope.lifecycleevent.interfaces import IZopeLifecycleEvent
from zope.lifecycleevent.interfaces import IObjectCreatedEvent
from zope.lifecycleevent.interfaces import IObjectModifiedEvent
from zope.lifecycleevent.interfaces import IObjectCopiedEvent
from zope.lifecycleevent.interfaces import IObjectMovedEvent
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from zope.lifecycleevent.interfaces import IObjectRemovedEvent
from zope.lifecycleevent.interfaces import IAttributes
from zope.lifecycleevent.interfaces import ISequence


moduleProvides(IZopeLifecycleEvent)


@implementer(IObjectCreatedEvent)
class ObjectCreatedEvent(ObjectEvent):
    """An object has been created"""


def created(object):
    notify(ObjectCreatedEvent(object))


@implementer(IAttributes)
class Attributes(object):
    """Describes modified attributes of an interface."""

    def __init__(self, interface, *attributes):
        self.interface = interface
        self.attributes = attributes


@implementer(ISequence)
class Sequence(object):
    """Describes modified keys of an interface."""

    def __init__(self, interface, *keys):
        self.interface = interface
        self.keys = keys


@implementer(IObjectModifiedEvent)
class ObjectModifiedEvent(ObjectEvent):
    """An object has been modified"""

    def __init__(self, object, *descriptions):
        """Init with a list of modification descriptions."""
        super(ObjectModifiedEvent, self).__init__(object)
        self.descriptions = descriptions


def modified(object, *descriptions):
    notify(ObjectModifiedEvent(object, *descriptions))


@implementer(IObjectCopiedEvent)
class ObjectCopiedEvent(ObjectCreatedEvent):
    """An object has been copied"""

    def __init__(self, object, original):
        super(ObjectCopiedEvent, self).__init__(object)
        self.original = original


def copied(object, original):
    notify(ObjectCopiedEvent(object, original))


@implementer(IObjectMovedEvent)
class ObjectMovedEvent(ObjectEvent):
    """An object has been moved"""

    def __init__(self, object, oldParent, oldName, newParent, newName):
        ObjectEvent.__init__(self, object)
        self.oldParent = oldParent
        self.oldName = oldName
        self.newParent = newParent
        self.newName = newName


def moved(object, oldParent, oldName, newParent, newName):
    notify(ObjectMovedEvent(object, oldParent, oldName, newParent, newName))


@implementer(IObjectAddedEvent)
class ObjectAddedEvent(ObjectMovedEvent):
    """An object has been added to a container"""

    def __init__(self, object, newParent=None, newName=None):
        if newParent is None:
            newParent = object.__parent__
        if newName is None:
            newName = object.__name__
        ObjectMovedEvent.__init__(self, object, None, None, newParent, newName)


def added(object, newParent=None, newName=None):
    notify(ObjectAddedEvent(object, newParent, newName))


@implementer(IObjectRemovedEvent)
class ObjectRemovedEvent(ObjectMovedEvent):
    """An object has been removed from a container"""

    def __init__(self, object, oldParent=None, oldName=None):
        if oldParent is None:
            oldParent = object.__parent__
        if oldName is None:
            oldName = object.__name__
        ObjectMovedEvent.__init__(self, object, oldParent, oldName, None, None)


def removed(object, oldParent=None, oldName=None):
    notify(ObjectRemovedEvent(object, oldParent, oldName))
