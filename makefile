dkc := "metabase/metabase.yml"

up:
	docker-compose -f ${dkc} up --build

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
	docker cp data/data_example.csv mongo:/
	docker exec -it mongo  mongoimport --host=127.0.0.1 -u lappis -p lappis -d Playload -c playload --type csv --file data_example.csv --headerline --authenticationDatabase=admin