``zope.lifecycleevent`` Changelog
=================================

4.0.3 (2013-09-12)
------------------

- Dropped the dependency on ``zope.component`` as the interface and
  implementation of ``ObjectEvent`` is now in ``zope.interface``.
  Retained the dependency for the tests.

- Fixed: ``.moved`` tried to notify the wrong event.


4.0.2 (2013-03-08)
------------------

- Add Trove classifiers indicating CPython and PyPy support.


4.0.1 (2013-02-11)
------------------

- Added `tox.ini`.


4.0.0 (2013-02-11)
------------------

- Test coverage at 100%.

- Added support for Python 3.3 and PyPy.

- Replaced deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropped support for Python 2.4 and 2.5.


3.7.0 (2011-03-17)
------------------

- Added convenience functions to parallel zope.lifecycleevent.modified
  for the other events defined in this package.


3.6.2 (2010-09-25)
------------------

- Added not declared, but needed test dependency on `zope.component [test]`.

3.6.1 (2010-04-30)
------------------

- Removed dependency on undeclared zope.testing.doctest.

3.6.0 (2009-12-29)
------------------

- Refactor tests to loose zope.annotation and zope.dublincore as dependencies.

3.5.2 (2009-05-17)
------------------

- ``IObjectMovedEvent``, ``IObjectAddedEvent``,
  ``IObjectRemovedEvent`` interfaces and ``ObjectMovedEvent``,
  ``ObjectAddedEvent`` and ``ObjectRemovedEvent`` classes copied here
  from zope.container (plus tests).  The intent is to allow packages
  that rely on these interfaces or the event classes to rely on
  zope.lifecycleevent (which has few dependencies) instead of
  zope.container (which has many).

3.5.1 (2009-03-09)
------------------

- Remove deprecated code and thus remove dependency on zope.deferredimport.

- Change package's mailing list address to zope-dev at zope.org, as
  zope3-dev at zope.org is now retired.

- Update package's description and documentation.

3.5.0 (2009-01-31)
------------------

- Remove old module declarations from classes.

- Use zope.container instead of zope.app.container.

3.4.0 (2007-09-01)
------------------

Initial release as an independent package
