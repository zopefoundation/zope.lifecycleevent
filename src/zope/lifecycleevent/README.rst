=============
 Quick Start
=============

This document describes the various event types defined by this
package and provides some basic examples of using them to inform parts
of the system about object changes.

All events have three components: an *interface* defining the event's
structure, a default *implementation* of that interface (the *event
object*), and a high-level *convenience function* (defined by the
:class:`~.IZopeLifecycleEvent` interface) for easily sending that
event in a single function call.

.. note:: The convenience functions are simple wrappers for
   constructing an event object and sending it via
   :func:`zope.event.notify`. We will only demonstrate some examples
   of this equivalence.

.. TODO: Need to refactor to move discussion of
   manually sending events somewhere else. That's an advanced usage.

.. note:: This document will not discuss actually *handling* these
   events (setting up *subscribers* for them). For more information on
   that topic, see `zope.event's documentation
   <http://zopeevent.readthedocs.io/en/latest/classhandler.html>`_
   (for basic uses) or :doc:`XXXWRITEME` for more flexible uses.

.. TODO: Need to talk about the fact that these are IObjectEvents and so
   will be re-dispatched based on the interface of the object in
   addition to the interface of the event. So it's usually not
   necessary to subclass the event types.

We will go through the events in approximate order of how they would
be used to follow the life-cycle of an object.


Creation
========

The first event is :class:`.~IObjectCreatedEvent`, implemented by
:class:`.~ObjectCreatedEvent`, which is used to communicate that a single object
has been created. It can be sent with the
:func:`zope.lifecycleevent.created` function.


For example:

    >>> from zope.event import notify
    >>> from zope.lifecycleevent import ObjectCreatedEvent

    >>> obj = {}
    >>> notify(ObjectCreatedEvent(obj))

Alternately, using the higher-level API, we could write that like
this:

    >>> from zope.lifecycleevent import created
    >>> created(obj)

Copying
=======

Copying an object is a special case of creating one. It can happen at
any time and is implemented with :class:`~.IObjectCopiedEvent`,
:class:`~.ObjectCopiedEvent`, or the API
:func:`zope.lifecycleevent.copied`.

    >>> import pickle
    >>> copy = pickle.loads(pickle.dumps(obj))

    >>> from zope.lifecycleevent import copied
    >>> copied(copy, obj)

Addition
========

After objects are created, it is common to *add* them somewhere for
storage or access. This can be accomplished with the
:class:`~IObjectAddedEvent` and its implementation
:class:`~.ObjectAddedEvent`, or the API
:func:`zope.lifecycleevent.added`.

    >>> from zope.lifecycleevent import ObjectAddedEvent
    >>> from zope.lifecycleevent import added

    >>> container = {}
    >>> container['name'] = obj
    >>> added(obj, container, 'name')

Modification
============

One of the most common types of events used from this package is the
:class:`IObjectModifiedEvent` (implemented by
:class:`ObjectModifiedEvent`) that represents object modification.

In the simplest case, it may be enough to simply notify interested
parties that the object has changed. Like the other events, this can
be done manually or through the convenience API
(:func:`zope.lifecycleevent.modified`):

    >>> obj['key'] = 42

    >>> from zope.lifecycleevent import ObjectModifiedEvent
    >>> notify(ObjectModifiedEvent(obj))

The above is equivalent to this:

    >>> from zope.lifecycleevent import modified
    >>> modified(obj)

Providing Additional Information
--------------------------------

Some event consumers like indexes (catalogs) and caches may need more
information to update themselves in an efficient manner. The necessary
information can be provided as optional "modification descriptions" of
the :class:`~.ObjectModifiedEvent` (or again, via the
:func:`.zope.lifecycleevent.moved` function).

This package doesn't strictly define what a "modification description"
must be. The most common (and thus most interoperable) descriptions
are based on interfaces.

We could simply pass an interface itself to say "something about the
way this object implements the interface changed":

    >>> from zope.interface import Interface, Attribute, implementer
    >>> class IFile(Interface):
    ...     data = Attribute("Data")
    >>> @implementer(IFile)
    ... class File(object):
    ...     pass

    >>> file = File()
    >>> file.data = "123"
    >>> notify(ObjectModifiedEvent(obj, IFile))

We can also be more specific in a case like this where we know exactly
what attribute of the interface we modified. There is a helper class
:class:`zope.lifecycleevent.Attributes` that assists:

    >>> file.data = "abc"
    >>> from zope.lifecycleevent import Attributes
    >>> modified(obj, Attributes(IFile, "data"))

.. TODO: Discuss modifying multiple attributes.

When an object is a sequence or container, we can specify
the individual indexes or keys that we changed using
:class:`zope.lifecycleevent.Sequence`.

First we'll need to define a sequence and create an instance:

    >>> from zope.interface.common.sequence import ISequence
    >>> class IFileList(ISequence):
    ...    "A sequence of IFile objects."
    >>> @implementer(IFileList)
    ... class FileList(list):
    ...   pass

    >>> files = FileList()
    >>> created(files)

Now we can modify the sequence by adding an object to it:

    >>> files.append(File())
    >>> from zope.lifecycleevent import Sequence
    >>> modified(files, Sequence(IFileList, len(files) - 1))

We can also replace an existing object:

    >>> files[0] = File()
    >>> modified(files, Sequence(IFileList, 0))

Of course these can be combined in any order and length necessary to
describe the modifications fully.

Movement
========

Sometimes objects move from one place to another. This can be
described with the interface :class:`.~IObjectMovedEvent`, its
implementation :class:`ObjectMovedEvent` or the API
:func:`zope.lifecycleevent.moved`.

   >>> container2 = {}
   >>> container2['new name'] = obj
   >>> del container['name']

   >>> from zope.lifecycleevent import moved
   >>> moved(obj, container, 'name', container2, 'new name')

Removal
=======

Finally, objects can be removed from the system altogether with
:class:`IObjectRemovedEvent`, :class:`ObjectRemovedEvent` and
:func:`zope.lifecycleevent.removed`.

.. note:: This is a special case of movement where the new parent and
   new name are always ``None``. Handlers for
   :class:`~.IObjectMovedEvent` can expect to receive events for
   :class:`~.IObjectRemovedEvent` as well.

    >>> del container2['new name']

    >>> from zope.lifecycleevent import removed
    >>> removed(obj, container2, 'new name')
