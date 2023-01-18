<p align="center">
    <img src="./assets/img/horizontal_logo.PNG" alt="hygia-logo" style="width:500px;"/>
</p>

# A powerful Python ML playground toolkit

[![PyPI Latest Release](https://img.shields.io/pypi/v/hygia.svg)](https://pypi.org/project/hygia/)
[![License](https://img.shields.io/pypi/l/hygia.svg)](https://github.com/hygia-org/hygia/blob/main/LICENSE)
[![Coverage](https://codecov.io/github/hygia-org/hygia/coverage.svg?branch=main)](https://codecov.io/gh/hygia-org/hygia)

<!-- [![Package Status](https://img.shields.io/pypi/status/hygia.svg)](https://pypi.org/project/hygia/) -->

## What is it?

Hygia is a Python package that provides fast, flexible, and expressive data pipeline configuration through a YAML file to make working with Machine Learning data easy and intuitive. It consists of helping developers and users to register, organize, compare and share all their ML model metadata in a single place, facilitating the generation of requirements in the ETL (Extract, Transform and Load) process. Thus, the migration can be scaled, automated, and accelerated for similar contexts.

## Main Features

- Configure data pipeline through a YAML file
- Execute through command line or python import
- Pack the solution into a Python's Package Manager
- Visualize results in customized dashboards
- Test on different databases

## Where to get it

The source code is currently hosted on GitHub at: `https://github.com/hygia-org`

## Installation from sources

```
python -m venv env
source env/bin/activate
pip install -r requirements-dev.txt
```

### Boilerplate

```
examples/hygia_boilerplate.ipynb
```

### Testing

```
pytest --cov
```

### Documentation

We used sphinx to write the documentation

To run locally, you need to install sphinx:

```
pip install sphinx
```

Then install the theme used:

```
pip install pydata-sphinx-theme
```

And Run the project

```
sphinx-build -b html source ./
```

And open the index.html
