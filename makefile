dkc := "metabase/metabase.yml"


up:
	docker-compose -f ${dkc} up --build -d
	@echo "Waiting"
	sleep 10
	@echo "Listening on port 3000"
	

network:
	docker network create metabase

clean:
	docker-compose -f ${dkc} kill
	docker-compose -f ${dkc} stop
	docker-compose -f ${dkc} down --rmi local --volumes
	docker-compose -f ${dkc} rm -f
	@echo "Docker containers have been stopped and deleted."

migrate:

	@echo "Loading data into the database..."

	docker cp $(path) mongo:/
	docker exec -it mongo  mongoimport --host=127.0.0.1 -u lappis -p lappis -d $(database) -c $(collection) --type csv --file data_example.csv --headerline --authenticationDatabase=admin