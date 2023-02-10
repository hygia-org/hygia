### Documentation

We utilized Sphinx and Doxygen to compose our documentation. To access it locally, you'll need to install both tools by running the following commands:

```
pip install sphinx
pip install doxygen-junit
```

Additionally, you'll need to install the theme we used:

```
pip install pydata-sphinx-theme
```

After completing these steps, navigate to the /docs folder and run the project.

To ensure that the documentation for classes and functions remains up-to-date, run:
```
doxygen
```

To generate the HTML version of the documentation, run:
```
sphinx-build -b html source ./
```

Finally, open the index.html file to access the documentation."
