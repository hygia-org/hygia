# Playground



## Run metabase

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

**Load data into the database**

Open another terminal and run the command

```make migrate```

**Connect the database to the metabase**

- step 1: Open localhost:3000
- step 2: Click Admin setting
- step 3: Click Database
- step 4: Add database authentication data

![](https://raw.githubusercontent.com/francisco1code/Files/main/a.gif)