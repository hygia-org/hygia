Superset

**Environment check**

Check if docker exists, if not then [install it](https://docs.docker.com/engine/install/ubuntu/)
`docker -v `

Check if docker-compose exists, if not then [install it](https://docs.docker.com/compose/install/)
`docker-compose -v `


**Run metabase local**

In the root folder, run the command, run superset application.

`make up  `


Now run the script to initialize the scripts.

`make init`

**Connect the database to the superset**

- step 1: Open localhost:8088 (default username and password: admin/admin)
- step 2: Click Admin setting
- step 3: Database connections
- step 4: Add database
- setp 5: select postgres


![db](https://raw.githubusercontent.com/francisco1code/Files/main/gif/db.gif)


**Exemple postgres connect superset**
| metabase | credential |
|------------|-------------|
| host | db |
|dabase_name | superset|
| user | superset |
| password | superset |


**Create dataset**

![](https://raw.githubusercontent.com/francisco1code/Files/main/gif/dataset.gif)

**Create chats**

![](https://raw.githubusercontent.com/francisco1code/Files/main/gif/chat.gif)


**Create Dashboard**

![](https://raw.githubusercontent.com/francisco1code/Files/main/gif/dashboard.gif)




