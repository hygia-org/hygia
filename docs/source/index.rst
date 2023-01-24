.. Hygia documentation master file, created by
   sphinx-quickstart on Fri Jan  6 12:14:17 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Hygia's documentation
=================================

`Hygia` is an open source, MIT-licensed library providing high-performance,
easy-to-use playground to organize, compare, register and share Machine Learning experiments on Databases developed in `Python <https://www.python.org/>`__
programming language.

Features
=================================

With `Hygia`, you can configure your data pipeline, customize the operations executed in each stage of the pipeline. The main features are:

- Be able to experiment on several databases
- Customize data pipeline for each database
- Custom visualization 
- Accelerate new hythoses evaluation
- Search, debug, and compare experiments, datasets, and models
- Organize and display experiments and model metadata however you want
- Share and collaborate on experiment results and models across the org

.. panels::
    :card: + intro-card text-center
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex

    ---
    :img-top: _static/index_getting_started.svg

    Getting started
    ^^^^^^^^^^^^^^^

    New to *Hygia*? Check out the getting started guides. They contain an
    introduction to *Hygia'* main concepts and links to additional tutorials.

    +++

    .. link-button:: getting_started
            :type: ref
            :text: To the getting started guides
            :classes: btn-block btn-secondary stretched-link

    ---
    :img-top: _static/index_user_guide.svg

    User guide
    ^^^^^^^^^^

    The user guide provides in-depth information on the
    key concepts of Hygia with useful background information and explanation.

    +++

    .. link-button:: user_guide
            :type: ref
            :text: To the user guide
            :classes: btn-block btn-secondary stretched-link

.. toctree::
   :maxdepth: 2
   :hidden:
   :titlesonly:
   
   user_guide/index
   doxygen/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
