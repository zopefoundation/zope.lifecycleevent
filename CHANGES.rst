=========
 Changes
=========

4.4 (2022-05-09)
================

- Add support for Python 3.8, 3,9, 3.10.

- Drop support for Python 3.4.


4.3 (2018-10-05)
================

- Add support for Python 3.7.


4.2.0 (2017-07-12)
==================

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6 and 3.3.

- Documentation is hosted at https://zopelifecycleevent.readthedocs.io

4.1.0 (2014-12-27)
==================

- Add support for PyPy3.

- Add support for Python 3.4.


4.0.3 (2013-09-12)
==================

- Drop the dependency on ``zope.component`` as the interface and
  implementation of ``ObjectEvent`` is now in ``zope.interface``.
  Retained the dependency for the tests.

- Fix: ``.moved`` tried to notify the wrong event.


4.0.2 (2013-03-08)
==================

- Add Trove classifiers indicating CPython and PyPy support.


4.0.1 (2013-02-11)
==================

- Add `tox.ini`.


4.0.0 (2013-02-11)
==================

- Test coverage at 100%.

- Add support for Python 3.3 and PyPy.

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.


3.7.0 (2011-03-17)
==================

- Add convenience functions to parallel ``zope.lifecycleevent.modified``
  for the other events defined in this package.


3.6.2 (2010-09-25)
==================

- Add not declared, but needed test dependency on ``zope.component [test]``.

3.6.1 (2010-04-30)
==================

- Remove dependency on undeclared ``zope.testing.doctest``.

3.6.0 (2009-12-29)
==================

- Refactor tests to lose ``zope.annotation`` and ``zope.dublincore`` as
  dependencies.

3.5.2 (2009-05-17)
==================

- Copy ``IObjectMovedEvent``, ``IObjectAddedEvent``,
  ``IObjectRemovedEvent`` interfaces and ``ObjectMovedEvent``,
  ``ObjectAddedEvent`` and ``ObjectRemovedEvent`` classes here
  from ``zope.container`` (plus tests).  The intent is to allow packages
  that rely on these interfaces or the event classes to rely on
  ``zope.lifecycleevent`` (which has few dependencies) instead of
  ``zope.container`` (which has many).

3.5.1 (2009-03-09)
==================

- Remove deprecated code and therefore dependency on ``zope.deferredimport``.

- Change package's mailing list address to zope-dev at zope.org, as
  zope3-dev at zope.org is now retired.

- Update package's description and documentation.

3.5.0 (2009-01-31)
==================

- Remove old module declarations from classes.

- Use ``zope.container`` instead of ``zope.app.container``.

3.4.0 (2007-09-01)
==================

Initial release as an independent package
