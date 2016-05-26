Luigi Tree
==========

Luigi Tree is an example project basised on the `Luigi<http://luigi.readthedocs.io/en/stable/>`_
Python package. Once installed you can create `Pascal's triangle<https://en.wikipedia.org/wiki/Pascal%27s_triangle>`_ like dependancy graphs using the Luigi
scheduler. This project can be used as an example starting point for anyone who is working to
build a command line application baised on the Luigi framework.

Background
----------

Place holder.

Basic Usage/Instalation
-----------------------

.. code-block:: bash
    git clone ...
    cd luigi_tree
    virtualenv /PATH/TO/VENV/luigi_tree
    source /PATH/TO/VENV/luigi_tree/bin/activate
    pip install -e .
    luigi_tree --level 2

Basic Usage
-----------

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
                            localhost
      --port PORT           Port the luigi scheduler is running on, default is
                            8082

