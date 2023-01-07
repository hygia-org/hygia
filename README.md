# Playground

### Instaling Requirements

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Running

```
python src/main.py
```

### Testing

```
pytest --cov
```

### Metabase

The metabase will help us visualize and monitor data processing, feature engineering and model monitoring, accompanying us throughout the cycle.

| Keywords  | Description |
|-----------|-------------|
|   CSV     | A CSV file is a plain text file that stores table and spreadsheet information. CSV files can be easily imported and exported using programs that store data in tables.|
| Collection| A collection is a grouping of MongoDB documents. Documents within a collection can have different fields. A collection is the equivalent of a table in a relational database system.|
|  Database | A database stores one or more collections of documents.|
| Mongo| It is a NoSQL database developed by MongoDB Inc. MongoDB database is built to store a huge amount of data and also perform fast.|

**Environment check**

Check if docker exists, if not then [install it](https://docs.docker.com/engine/install/ubuntu/) 
```docker -v ```

Check if docker-compose exists, if not then [install it](https://docs.docker.com/compose/install/) 
```docker-compose -v ```

when running the first time create the network 

```make network```

**Run metabase local**

In the root folder, run the command

```make up```

**Loading data into a non-relational database**

This command is used to load the .csv file into the local database, where it is necessary to pass the file path, database and collection as an argument

- path = .csv file path
- database = database name
- collection = collection name

exemple:


```make migrate path=data/data_example.csv database=general  collection=order```



**Connect the database to the metabase**

- step 1: Open localhost:3000
- step 2: Click Admin setting
- step 3: Click Database
- step 4: Add database authentication data

![](https://raw.githubusercontent.com/francisco1code/Files/main/a.gif)

**Exemple mongo connect metabase**
|  metabase  | credential  |
|------------|-------------|
|    host    |  mongo  |
|dabase_name | use the name you define in make migrate|
|    user    |   lappis    |
|  password  |   lappis    |


### Documentation

We used sphinx to write the documentation

To run locally, you need to install sphinx:

```pip install sphinx```

Then install the theme used:

```pip install pydata-sphinx-theme```

And Run the project

```sphinx-build -b html source ./``` 

And open the index.html