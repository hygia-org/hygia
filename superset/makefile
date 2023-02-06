compose := "superset.yml"

up: 
	docker-compose -f ${compose} up --build -d

clean:
	docker-compose -f ${compose} kill
	docker-compose -f ${compose} stop
	docker-compose -f ${compose} down --rmi local --volumes
	docker-compose -f ${compose} rm 

init:
	chmod +x ./scripts/init.sh
	./scripts/init.sh


