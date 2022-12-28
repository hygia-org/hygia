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

step 1: Open localhost:3000
step 2: Click Admin setting
step 3: Click Database
step 4: Add database authentication data

<div style="position: relative; width: 100%; height: 0; padding-top: 100.0000%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAFWAsbFONU&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>


