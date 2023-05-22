## Installation Guide

### Recommendation
We recommend Ubuntu 22.04, Python 3.09 and Jupyter Notebook to run.

### Requirements
#### Python
python3.9-dev
python3.9-venv

#### Poetry
```
pip install poetry
```
#### Pytest
```
pip install pytest
```

First you need to have env in your virtual machine. Check the documentation [available here](https://virtualenv.pypa.io/en/latest/installation.html).


Then create a venv and install the requirements.

```
python -m venv env
source env/bin/activate
pip install -r requirements-dev.txt
```

### Guide for users

### Guide for contributors

### Testing

To run and verify the tests run:

```
pytest --cov
```
### Common problems