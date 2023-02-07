## Instalation Guide

For those who are already familiar with the library and are already part of it, we have this installation guide for you to enjoy.

First you need to have env in your virtual machine. Check the documentation [available here](https://virtualenv.pypa.io/en/latest/installation.html).


Then create a venv and install the requirements.

```
python -m venv env
source env/bin/activate
pip install -r requirements-dev.txt
```

### Testing

To run and verify the tests run:

```
pytest --cov
```
