zope.lifecycleevent Package Readme
==================================

Overview
--------

In Zope 3, events are used by components to inform each other about
relevant new objects and object modifications.

To keep all subscribers up to date it is indispensable that the life
cycle of an object is accompanied by various events.

For more details, see src/zope/lifecycleevent/README.txt

Changes
-------

See CHANGES.txt.

Installation
------------

See INSTALL.txt.


Developer Resources
-------------------

- Subversion browser:

  http://svn.zope.org/zope.lifecycleevent/

- Read-only Subversion checkout:

  $ svn co svn://svn.zope.org/repos/main/zope.lifecycleevent/trunk

- Writable Subversion checkout:

  $ svn co svn+ssh://userid@svn.zope.org/repos/main/zope.lifecycleevent/trunk

- Note that the 'src/zope/lifecycleevent package is acutally a 'svn:externals'
  link to the corresponding package in the Zope3 trunk (or to a specific tag,
  for released versions of the package).
