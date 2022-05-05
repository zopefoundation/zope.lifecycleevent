=========================
 ``zope.lifecycleevent``
=========================

.. image:: https://github.com/zopefoundation/zope.lifecycleevent/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/zopefoundation/zope.lifecycleevent/actions/workflows/tests.yml
        :alt: Build Status

.. image:: https://readthedocs.org/projects/zopelifecycleevent/badge/?version=latest
         :target: http://zopelifecycleevent.readthedocs.io/en/latest/?badge=latest
         :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/zopefoundation/zope.lifecycleevent/badge.svg?branch=master
         :target: https://coveralls.io/github/zopefoundation/zope.lifecycleevent?branch=master
         :alt: Coverage Status


Overview
========

In a loosely-coupled system, events can be used by parts of the system
to `inform each other`_ about relevant occurrences. The `zope.event`_
package (optionally together with `zope.interface`_ and
`zope.component`_) provides a generic mechanism to dispatch objects
representing those events to interested subscribers (e.g., functions).
This package defines a specific set of event objects and API functions
for describing the life-cycle of objects in the system: object
creation, object modification, and object removal.

.. _inform each other: https://zopeevent.readthedocs.io/en/latest/api.html#zope.event.notify
.. _zope.event: https://zopeevent.readthedocs.io/en/latest/
.. _zope.component: https://zopecomponent.readthedocs.io/en/latest/
.. _zope.interface: https://zopeinterface.readthedocs.io/en/latest/

Documentation is hosted at https://zopelifecycleevent.readthedocs.io
