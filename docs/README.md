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

### Problems solution building documentation in WSL

When running the command to generate the HTML version of the documentation, an error may occur in the breathe module.

![breathe](https://github.com/hygia-org/hygia/assets/58870950/8ed9a50b-43b6-4ec0-a8cb-62b507ed9c8f)

To solve just run the command:

```
pip install breathe
```

After running the command, it may give an error in the sphinx extension

![sphinx](https://github.com/hygia-org/hygia/assets/58870950/0066b82a-6a0f-4027-a249-15089a067648)

In this case, use the command:

```
pip install sphinx-panels
```
