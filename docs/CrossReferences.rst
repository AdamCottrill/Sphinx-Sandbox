Cross References
================

You can reference other parts of your document by creating bookmarks by adding a
directive using this syntax: ``.. _bookmark:`` where bookmark a the name you use
to reference this location in the documentation (Take note of the single leading
underscore and single trailing colon!)   You can then create a link to that
location using this syntax:  ``:ref:`bookmark  <bookmark>``` where the first
bookmark is the text that will be displayed, and second is the name of the
target created earlier.  For example here is a link to the images section in my
changelog file: :ref:`images <images>` and here is a link to whole page
reStructured Text Basics on :doc:`rstBasics`


Downloads
=========

You can create links to files that can be downloaded using similar syntax:
``:download:`DisplayName <../filename.txt>```.  For example here is a link to
download this file here: :download:`Cross References <./CrossReferences.rst>`


.. note::

  There cannot be a space between the directive and the back tick
  ``:download:`DisplayName <../filename.txt>``` is correct, this is *not*
  ``:download: `DisplayName <../filename.txt>```


External Documentation
======================

By adding the 'sphinx.ext.intersphinx' extension and adding intersphinx_mapping
(a dictionary) in the config.py it is possible to provide a link to external
projects that also documented with sphinx.  For example here is a link to the
Python docs for ``io.open``:

:py:func:`io.open`

.. note::

  Be sure update both the extension and mapping to get intersphinx to work.



:mod: `ascynio`


:class: `bool`