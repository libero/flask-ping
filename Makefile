.PHONY: tests
tests:
	docker-compose run --rm --service-ports flask-ping

shell:
	docker-compose run --rm --service-ports flask-ping /bin/bash

build:
	docker-compose build flask-ping
