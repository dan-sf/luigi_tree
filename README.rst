Luigi Tree
==========

Luigi Tree is an example project based on the Luigi_ Python package. Once
installed you can create `Pascal triangle`_ like dependency graphs using the
Luigi scheduler. This project can be used as an example starting point for
anyone who is working to build a command line application based on the Luigi
framework.

.. _Luigi: http://luigi.readthedocs.io/en/stable/
.. _Pascal triangle: https://en.wikipedia.org/wiki/Pascal%27s_triangle

Background
----------

This project was created in an effort to help anyone getting started working
with Luigi. I have tried my best to make this project as "real world" as
possible by using Python's setuptools for requirements and directory structure.
I have also included unit tests which can be run with the following command:

.. code-block:: bash

    python setup.py test

Check out the Luigi_ documentation for more code examples and use cases. I also
did a blog post which goes into more detail about the usage and reasoning for
this project here_.

.. _here: http://www.dsfcode.com/pascals-triangle-with-luigi/

Installation
------------

Clone luigi_tree and install it using a virtual environment:

.. code-block:: bash

    git clone https://github.com/dsfcode/luigi_tree.git
    cd luigi_tree
    virtualenv /PATH/TO/VENV/luigi_tree
    source /PATH/TO/VENV/luigi_tree/bin/activate
    pip install .
    # Optionally run the luigi server (defaults to http://localhost:8082/static/visualiser/index.html)
    luigid
    # Run luigi_tree with default options
    luigi_tree

Usage
-----

.. code-block:: bash

    usage: luigi_tree [-h] [--level LEVEL] [--sleep SLEEP]
                      [--output-dir OUTPUT_DIR] [--server SERVER] [--port PORT]

    optional arguments:
      -h, --help            show this help message and exit
      --level LEVEL         Set the number of levels the tree will have, default
                            is 2
      --sleep SLEEP         Set how many seconds each task will sleep for, default
                            is 2
      --output-dir OUTPUT_DIR
                            Directory path to write output targets to, default is
                            /tmp
      --server SERVER       Server the luigi scheduler is running on, default is
                            localhost. If there is no server running luigi_tree
                            will run using the local-scheduler
      --port PORT           Port the luigi scheduler is running on, default is
                            8082

