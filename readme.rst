Sphinx Sandbox
--------------

This repo contains a Sphinx project that was used to explore many of
the features available in that documentation system.  It was
originally developed from the Sphinx tutorial presented at Pycon 2021,
but was expanded to include additional functionality and worked
examples.  Consider this a living document.

To view the documentation, start a webserver in ``~/docs/_build/html``:

.. code:: bash

  > python -m http.server


To compile the documentation activate the virtual environment and run
sphinx:

.. code:: bash

  > workon sphinx_sandbox
  (venv)> cd docs
  (venv)> make html


Writing documentation is much easier with hot reloading provided by
the sphinx-autobuild package.

.. code:: bash

  > workon sphinx_sandbox
  (venv)> cd docs
  (venv)> sphinx-autobuild . ./_build/html
