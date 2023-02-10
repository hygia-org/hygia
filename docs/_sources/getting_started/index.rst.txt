.. Hygia documentation master file, created by
   sphinx-quickstart on Fri Jan  6 12:14:17 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Getting Started
=================================


Hygia is a Python package that provides fast, flexible, and expressive data pipeline configuration 
through a YAML file to make working with Machine Learning data easy and intuitive. It consists of 
helping developers and users to register, organize, compare and share all their ML model metadata in 
a single place, facilitating the generation of requirements in the ETL (Extract, Transform and Load) process. 
Thus, the migration can be scaled, automated, and accelerated for similar contexts.


Installing from PyPI
---------------------

.. panels::
    :card: + install-card
    :column: col-12 p-3


    How Install Hygia?
    ^^^^^^^^^^^^^^^^^^^
    Hygia can be found on `PyPi <https://pypi.org/project/hygia/>`_ for installation through pip:


    .. code-block:: bash

        pip install hygia

    ++++++++++++++++++++++
   
    After installation, you can certify the installation through the commands:

    .. code-block:: bash

        pip freeze

    or

    .. code-block:: bash

        pip show hygia



.. toctree::
   :maxdepth: 2

   user_guide/index
   doxygen/index
