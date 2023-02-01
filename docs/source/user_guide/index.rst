.. Hygia documentation master file, created by
   sphinx-quickstart on Fri Jan  6 12:14:17 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

User Guide
=================================

A user guide is a page that provides instructions and information on how to use Hylia Library.
It may include information on features, settings, troubleshooting, and step-by-step procedures for performing specific tasks.
The goal is to help users understand and effectively use the software.

.. note::
   In the `Hygia repository <https://github.com/hygia-org/hygia>`_ there are some `boilerplates <https://github.com/hygia-org/hygia/tree/main/examples>`_ to guide learning and understanding the use Hygia features.


The Hygia library offers two options for usage: (1) Utilizing the available functions directly in your development 
environment, such as a Jupyter Notebook. (2) Automating processes for different databases through a customizable .yaml file. 
This file allows you to define your pipeline and at the end, it provides a visualization of the processed data.

.. image:: ../../_static/Frame4.png
  :width: 1000
  :alt: Alternative text


Using YAML file
-----------------

Update the yaml file with your needed configs and run the notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


::

   import hygia as hg

   config_file = '../config/default_config.yaml'
   result = hg.run_with_config(config_file)
   result 


Predict Example
-----------------

Imports and classes instanciations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   import pandas as pd
   import hygia as hg

   pre_process_data = hg.PreProcessData()
   feature_engineering = hg.FeatureEngineering()
   rf_model = hg.RandomForestModel('../data/models/RandomForest_Ksmash_WordEmbedding_Regex.pkl')


Load Data
^^^^^^^^^^^^^^^^^^^^^^^^^

::

   file_path = '../data/tmp/AI_LATA_ADDRESS_MEX_modificado.csv'
   df = pd.read_csv(file_path, sep='¨', nrows=500_000, engine='python')


Add new columns
^^^^^^^^^^^^^^^^^^^^^^^^^

* Concatenate address

* All features columns

  * Key Smash

  * Regex

  * Word Embedding

::

   concatened_column_name = 'concat_STREET_ADDRESS_1_STREET_ADDRESS_2'
   df = pre_process_data.pre_process_data(df, ['STREET_ADDRESS_1', 'STREET_ADDRESS_2'], concatened_column_name)
   df = feature_engineering.extract_features(df, concatened_column_name)


Check new columns names
^^^^^^^^^^^^^^^^^^^^^^^^^

::

   ks_we_and_re_colummns = [col for col in df if col.startswith('feature_ks') or col.startswith('feature_we') or col.startswith('feature_re')]
   ks_we_and_re_colummns


Predict using pre-trained model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   df['prediction'] = rf_model.predict(df[ks_we_and_re_colummns].values)
   df['prediction'].value_counts()


Save predicted data
^^^^^^^^^^^^^^^^^^^^^^^^^

::

   df[['concat_STREET_ADDRESS_1_STREET_ADDRESS_2', 'prediction']].to_csv('data/tmp/prediction.csv')

